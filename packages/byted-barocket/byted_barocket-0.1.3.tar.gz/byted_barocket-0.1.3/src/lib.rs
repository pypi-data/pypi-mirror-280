use pyo3::prelude::*;
use tokio::runtime::Runtime; // 用于创建异步运行时
use std::path::{Path, PathBuf};
use std::collections::HashMap;

mod downloader;

use downloader::Downloader;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// 异步下载文件并等待完成
/// import ba_rocket
/// ba_rocket.download_files([("https://tosv.byted.org/obj/labcv.ftp/tests/output1.mp4", "./test.jpg")], 1024 * 1024, 10)
#[pyfunction]
fn download_files(py: Python, urls_paths: Vec<(String, HashMap<String, String>, String)>, chunk_size: u64, max_concurrent_downloads: usize) -> PyResult<()> {
    py.allow_threads(move || {
        let rt = Runtime::new().unwrap(); // 创建Tokio运行时
        rt.block_on(async {
            let downloader = Downloader::new();
            // 将Python传入的路径字符串转换为PathBuf
            let urls_paths: Vec<(String, HashMap<String, String>, PathBuf)> = urls_paths.into_iter().map(|(url, headers, path)| (url, headers, PathBuf::from(path))).collect();
            // 运行下载逻辑
            if let Err(e) = downloader.download_files(urls_paths, chunk_size, max_concurrent_downloads).await {
                return Err(PyErr::new::<pyo3::exceptions::PyIOError, _>(format!("Error downloading files: {}", e)));
            }
            Ok(())
        })
    })
}

/// A Python module implemented in Rust.
#[pymodule]
fn ba_rocket(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(download_files, m)?)?;
    Ok(())
}
