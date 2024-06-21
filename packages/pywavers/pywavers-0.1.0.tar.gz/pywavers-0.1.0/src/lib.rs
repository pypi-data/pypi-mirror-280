//! # PyWavers
//! A Python library for reading and writing wav files using Rust.
//!
//! ## Installation
//! ```bash
//! pip install pywavers
//! ```
//!
//! ## Supported DTypes
//! - i16
//! - i32
//! - f32
//! - f64
//! - The Rust version of Wavers supports i24 but numpy does not have a dtype for it.
//!
//! ## Usage
//! ```python
//! import numpy as np
//! import pywavers
//!
//! # Read a wav file
//! data, sample_rate = pywavers.read_i16("path/to/file.wav")
//!
//! # Write a wav file
//! data = np.random.rand(1000, 2).astype(np.float32)
//! pywavers.write_f32(fp="path/to/file.wav", data=data, sample_rate=44100)
//!
//! # Get information about a wav file
//! spec = pywavers.wav_spec("path/to/file.wav")
//! print(spec.sample_rate)
//! print(spec.n_channels)
//! print(spec.duration)
//! print(spec.encoding)
//! ```
//!
//! ## Functions
//! - read
//! - write
//! - wav_spec
//!

use wavers::{format_info_to_wav_type, write, FmtChunk, IntoNdarray, Wav, WavType};

use numpy::{IntoPyArray, PyArray2, PyArrayMethods, PyUntypedArrayMethods};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

macro_rules! _read {
    ($($T:ident), *) => {
        $(
            paste::item! {
                /// Read a wav file into a numpy array as the specified type
                #[pyfunction]
                pub fn [<read_ $T>](py: Python, fp: String) -> PyResult<(Bound<'_, PyArray2<$T>>, i32)> {
                    let wav: Wav<$T> = Wav::<$T>::from_path(&fp).map_err(|e| PyValueError::new_err(format!("Error opening wav file: {}", e)))?;

                    let (samples, sample_rate) = wav.into_ndarray().map_err(|e| PyValueError::new_err(format!("Error converting wav file to ndarray: {}", e)))?;

                    Ok((samples.into_pyarray_bound(py), sample_rate))
                }
            }
        )*
    };
}

_read!(i16, i32, f32, f64);

macro_rules! _write {
    ($($T:ident), *) => {
        $(
            paste::item! {
                /// Writes a wav file to disk as the specified type
                #[pyfunction]
                pub fn [<write_$T>](_py: Python, fp: String, data: &Bound<'_, PyArray2<$T>>, sample_rate: u32) -> PyResult<()> {
                    let shape: &[usize] = data.shape();
                    let d = unsafe { data.as_array() };

                    let slice_data = match d.as_slice() {
                        Some(s) => s,
                        None => {
                            return Err(PyValueError::new_err(
                                "Error converting numpy array to slice",
                            ))
                        }
                    };

                    write::<$T, &str>(&fp, slice_data, sample_rate as i32, shape[1] as u16)
                        .map_err(|e| PyValueError::new_err(format!("Error writing wav file: {}", e)))
                                }
                            }
                        )*
                    };
}

_write!(i16, i32, f32, f64);

/// A struct containing information about a wav file
#[pyclass]
pub struct WavSpec {
    #[pyo3(get)]
    pub sample_rate: i32,
    #[pyo3(get)]
    pub n_channels: u16,
    #[pyo3(get)]
    pub duration: u32,
    #[pyo3(get)]
    pub encoding: WavType,
}

/// Function to retrieve information on a wav file without reading the audio data.
#[pyfunction]
pub fn wav_spec(fp: String) -> PyResult<WavSpec> {
    let (duration, header) = wavers::wav_spec(&fp)
        .map_err(|e| PyValueError::new_err(format!("Error reading wav file: {}", e)))?;

    let fmt_chunk: &FmtChunk = &header.fmt_chunk;
    let wav_type: WavType = format_info_to_wav_type((
        fmt_chunk.format,
        fmt_chunk.bits_per_sample,
        fmt_chunk.format,
    ))
    .map_err(|e| {
        PyValueError::new_err(format!("Error converting format info to wav type: {}", e))
    })?;

    Ok(WavSpec {
        sample_rate: fmt_chunk.sample_rate,
        n_channels: fmt_chunk.channels,
        duration,
        encoding: wav_type,
    })
}

#[pymodule]
fn pywavers(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<WavSpec>()?;
    m.add_class::<WavType>()?;
    m.add_function(wrap_pyfunction!(wav_spec, m)?)?;
    m.add_function(wrap_pyfunction!(read_i16, m)?)?;
    m.add_function(wrap_pyfunction!(read_i32, m)?)?;
    m.add_function(wrap_pyfunction!(read_f32, m)?)?;
    m.add_function(wrap_pyfunction!(read_f64, m)?)?;

    m.add_function(wrap_pyfunction!(write_i16, m)?)?;
    m.add_function(wrap_pyfunction!(write_i32, m)?)?;
    m.add_function(wrap_pyfunction!(write_f32, m)?)?;
    m.add_function(wrap_pyfunction!(write_f64, m)?)?;
    Ok(())
}
