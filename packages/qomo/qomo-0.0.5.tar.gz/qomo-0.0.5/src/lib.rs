use pyo3::prelude::*;

#[pyfunction]
fn sum_as_str(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pymodule]
#[pyo3(name = "qomo")]
fn python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_str, m)?)?;
    Ok(())
}
