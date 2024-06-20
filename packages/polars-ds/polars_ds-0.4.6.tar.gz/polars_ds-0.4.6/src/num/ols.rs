/// OLS using Faer.
use faer::{prelude::*, Side};
use faer_ext::IntoFaer;
// use faer_ext::IntoFaer;
use crate::utils::rechunk_to_frame;
use itertools::Itertools;
use ndarray::{s, Array2};
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use serde::Deserialize;

#[derive(Deserialize, Debug)]
pub(crate) struct LstsqKwargs {
    pub(crate) bias: bool,
    pub(crate) skip_null: bool,
}

fn report_output(_: &[Field]) -> PolarsResult<Field> {
    let index = Field::new("idx", DataType::UInt16); // index of feature
    let coeff = Field::new("coeff", DataType::Float64); // estimated value for this coefficient
    let stderr = Field::new("std_err", DataType::Float64); // Std Err for this coefficient
    let t = Field::new("t", DataType::Float64); // t value for this coefficient
    let p = Field::new("p>|t|", DataType::Float64); // p value for this coefficient
    let v: Vec<Field> = vec![index, coeff, stderr, t, p];
    Ok(Field::new("lstsq_report", DataType::Struct(v)))
}

fn pred_residue_output(_: &[Field]) -> PolarsResult<Field> {
    let pred = Field::new("pred", DataType::Float64);
    let residue = Field::new("resid", DataType::Float64);
    let v = vec![pred, residue];
    Ok(Field::new("pred", DataType::Struct(v)))
}

fn coeff_output(_: &[Field]) -> PolarsResult<Field> {
    Ok(Field::new(
        "coeffs",
        DataType::List(Box::new(DataType::Float64)),
    ))
}

/// Returns the coefficients for lstsq as a nrows x 1 matrix
/// The uses Cholesky decomposition as default method to compute inverse,
/// and falls back to LU decomposition
fn faer_cholesky_lstsq(x: MatRef<f64>, xt: MatRef<f64>, y: MatRef<f64>) -> Mat<f64> {
    let xtx = xt * x;
    let inv = match xtx.cholesky(Side::Lower) {
        Ok(cho) => cho.inverse(),
        // Fall back to LU decomp
        Err(_) => xtx.partial_piv_lu().inverse(),
    };
    let coeffs = inv * xt * y;
    coeffs
}

/// Returns a Array2 ready for linear regression, and a mask, indicating valid rows
#[inline(always)]
fn series_to_mat_for_lstsq(
    inputs: &[Series],
    add_bias: bool,
    skip_null: bool,
) -> PolarsResult<(Array2<f64>, BooleanChunked)> {
    let nrows = inputs[0].len();
    // minus 1 because target is also in inputs
    let n_features = inputs.len().abs_diff(1);
    // Create null mask
    let mut has_null = inputs[0].has_validity();
    let mut mask = inputs[0].is_not_null();
    for s in inputs.iter() {
        has_null |= s.has_validity();
        mask = mask & s.is_not_null();
    }
    // Return a mask where true is kept (true means not null).

    if has_null && !skip_null {
        Err(PolarsError::ComputeError(
            "Lstsq: Data must not contain nulls when skip_null is False.".into(),
        ))
    } else {
        let mut df = if add_bias {
            let mut series_vec = inputs.to_vec(); // cheap copy
            series_vec.push(Series::from_iter(std::iter::repeat(1f64).take(nrows)));
            rechunk_to_frame(&series_vec)
        } else {
            rechunk_to_frame(inputs)
        }?;
        if has_null && skip_null {
            df = df.filter(&mask)?;
        }
        if df.height() < n_features {
            Err(PolarsError::ComputeError(
                "Lstsq: #Data < #features. No conclusive result.".into(),
            ))
        } else {
            // Error here
            // println!("{:?}", df.shape());
            let mat = df.to_ndarray::<Float64Type>(IndexOrder::Fortran)?;
            // println!("B");
            Ok((mat, mask))
        }
    }
}

#[polars_expr(output_type_func=coeff_output)]
fn pl_lstsq(inputs: &[Series], kwargs: LstsqKwargs) -> PolarsResult<Series> {
    let add_bias = kwargs.bias;
    let skip_null = kwargs.skip_null;
    // Target y is at index 0
    match series_to_mat_for_lstsq(inputs, add_bias, skip_null) {
        Ok((mat, _)) => {
            let nrows = mat.nrows();
            let y = mat.slice(s![0..nrows, 0..1]);
            let y = y.view().into_faer();
            let x = mat.slice(s![0..nrows, 1..]);
            let xt = x.t().into_faer();
            let x = x.view().into_faer();
            // Solving Least Square
            let coeffs = faer_cholesky_lstsq(x, xt, y);
            let mut builder: ListPrimitiveChunkedBuilder<Float64Type> =
                ListPrimitiveChunkedBuilder::new("betas", 1, coeffs.nrows(), DataType::Float64);

            builder.append_slice(&coeffs.col_as_slice(0));
            let out = builder.finish();
            Ok(out.into_series())
        }
        Err(e) => Err(e),
    }
}

#[polars_expr(output_type_func=pred_residue_output)]
fn pl_lstsq_pred(inputs: &[Series], kwargs: LstsqKwargs) -> PolarsResult<Series> {
    let add_bias = kwargs.bias;
    let skip_null = kwargs.skip_null;
    // Copy data
    // Target y is at index 0
    match series_to_mat_for_lstsq(inputs, add_bias, skip_null) {
        Ok((mat, mask)) => {
            // Mask = True indicates the the nulls that we skipped.
            let nrows = mat.nrows();
            let y = mat.slice(s![0..nrows, 0..1]);
            let y = y.view().into_faer();
            let x = mat.slice(s![0..nrows, 1..]);
            let xt = x.t().into_faer();
            let x = x.view().into_faer();
            // Solving Least Square
            let coeffs = faer_cholesky_lstsq(x, xt, y);

            let pred = x * &coeffs;
            let resid = y - &pred;
            let pred = pred.col_as_slice(0);
            let resid = resid.col_as_slice(0);
            // Need extra work when skip_null is true and there are nulls
            let (p, r) = if skip_null && mask.any() {
                let mut p_builder: PrimitiveChunkedBuilder<Float64Type> =
                    PrimitiveChunkedBuilder::new("pred", mask.len());
                let mut r_builder: PrimitiveChunkedBuilder<Float64Type> =
                    PrimitiveChunkedBuilder::new("resid", mask.len());
                let mut i: usize = 0;
                for mm in mask.into_no_null_iter() {
                    // mask is always non-null, mm = true means is not null
                    if mm {
                        p_builder.append_value(pred[i]);
                        r_builder.append_value(resid[i]);
                        i += 1;
                    } else {
                        p_builder.append_value(f64::NAN);
                        r_builder.append_value(f64::NAN);
                    }
                }
                (p_builder.finish(), r_builder.finish())
            } else {
                let pred = Float64Chunked::from_slice("pred", pred);
                let residue = Float64Chunked::from_slice("resid", resid);
                (pred, residue)
            };
            let p = p.into_series();
            let r = r.into_series();
            let out = StructChunked::new("", &[p, r])?;
            Ok(out.into_series())
        }
        Err(e) => Err(e),
    }
}

#[polars_expr(output_type_func=report_output)]
fn pl_lstsq_report(inputs: &[Series], kwargs: LstsqKwargs) -> PolarsResult<Series> {
    let add_bias = kwargs.bias;
    let skip_null = kwargs.skip_null;
    // Copy data
    // Target y is at index 0
    match series_to_mat_for_lstsq(inputs, add_bias, skip_null) {
        Ok((mat, _)) => {
            let ncols = mat.ncols() - 1;
            let nrows = mat.nrows();

            let y = mat.slice(s![0..nrows, 0..1]);
            let y = y.view().into_faer();
            let x = mat.slice(s![0..nrows, 1..]);
            let xt = x.t().into_faer();
            let x = x.view().into_faer();
            // Solving Least Square
            let xtx = xt * &x;
            let xtx_inv = match xtx.cholesky(Side::Lower) {
                Ok(cho) => cho.inverse(),
                Err(_) => xtx.partial_piv_lu().inverse(),
            };
            let coeffs = &xtx_inv * xt * y;
            let betas = coeffs.col_as_slice(0);
            // Degree of Freedom
            let dof = nrows as f64 - ncols as f64;
            // Residue
            let res = y - x * &coeffs;
            let res2 = res.transpose() * &res; // total residue, sum of squares
            let res2 = res2.read(0, 0) / dof;
            // std err
            let std_err = (0..ncols)
                .map(|i| (res2 * xtx_inv.read(i, i)).sqrt())
                .collect_vec();
            // T values
            let t_values = betas
                .iter()
                .zip(std_err.iter())
                .map(|(b, se)| b / se)
                .collect_vec();
            // P values
            let p_values = t_values
                .iter()
                .map(
                    |t| match crate::stats_utils::beta::student_t_sf(t.abs(), dof) {
                        Ok(p) => 2.0 * p,
                        Err(_) => f64::NAN,
                    },
                )
                .collect_vec();
            // Finalize
            let idx_series = UInt16Chunked::from_iter((0..ncols).map(|i| Some(i as u16)));
            let idx_series = idx_series.with_name("idx").into_series();
            let coeffs_series = Float64Chunked::from_slice("coeff", betas);
            let coeffs_series = coeffs_series.into_series();
            let stderr_series = Float64Chunked::from_vec("std_err", std_err);
            let stderr_series = stderr_series.into_series();
            let t_series = Float64Chunked::from_vec("t", t_values);
            let t_series = t_series.into_series();
            let p_series = Float64Chunked::from_vec("p>|t|", p_values);
            let p_series = p_series.into_series();
            let out = StructChunked::new(
                "lstsq_report",
                &[idx_series, coeffs_series, stderr_series, t_series, p_series],
            )?;
            Ok(out.into_series())
        }
        Err(e) => Err(e),
    }
}
