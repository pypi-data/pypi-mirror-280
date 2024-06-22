use std::collections::HashMap;
use std::io;
use std::path::{Path, PathBuf};
use std::str::FromStr;
use std::sync::Arc;
use futures::stream::{self, StreamExt};
use futures_util::stream::{FuturesUnordered};
use reqwest::{Client, Error as ReqwestError};
use reqwest::header::CONTENT_LENGTH;
use tokio::fs::{self, File};
use tokio::io::AsyncWriteExt;
use tokio::sync::{mpsc, Semaphore};

pub struct Downloader {
    client: Client,
}

impl Downloader {
    // 初始化 Downloader，可在这里配置Client，如启用连接池等
    pub fn new() -> Self {
        Self {
            client: Client::builder()
                // 可根据需要配置连接池大小等参数
                .build()
                .expect("Client builder failed"),
        }
    }

    pub async fn download_files(&self, urls_paths: Vec<(String, HashMap<String, String>, PathBuf)>, chunk_size: u64, max_concurrent_downloads: usize) -> Result<(), io::Error> {
        let semaphore = Arc::new(Semaphore::new(max_concurrent_downloads));

        stream::iter(urls_paths.into_iter())
            .for_each_concurrent(max_concurrent_downloads.clone(), |(url, headers, path)| {
                let semaphore = semaphore.clone();
                // 注意这里已经直接使用每个URL的对应路径了
                async move {
                    let _permit = semaphore.acquire().await.expect("Failed to acquire semaphore permit");
                    // 确保目录存在
                    if let Some(parent) = path.parent() {
                        if fs::create_dir_all(parent).await.is_err() {
                            eprintln!("Failed to create directories for {:?}", parent);
                        }
                    }
                    let start_time = std::time::Instant::now();
                    match self.download_file_with_chunks(&url, headers, &path, chunk_size).await {
                        Ok(_) => {
                            println!("Successfully downloaded {} in {:.2?}", url, start_time.elapsed());
                        }
                        Err(e) => eprintln!("Failed to download {}: {} in {:.2?}", url, e, start_time.elapsed()),
                    }
                }


            })
            .await;

        Ok(())
    }

    async fn download_file_with_chunks(&self, url: &str, headers: HashMap<String, String>, path: &Path, chunk_size: u64) -> Result<(), io::Error> {
        let response = self.client.head(url).send().await.unwrap();
        let content_length = response.headers().get(CONTENT_LENGTH)
            .and_then(|value| value.to_str().ok())
            .and_then(|value| u64::from_str(value).ok())
            .unwrap_or(0);

        if content_length == 0 {
            println!("{url} content_length is 0");
            return Ok(());
        }

        let (tx, mut rx) = mpsc::channel(100); // 在这里设定合适的缓冲区大小

        let mut futures = FuturesUnordered::new();

        for start in (0..content_length).step_by(chunk_size as usize) {
            let end = std::cmp::min(start + chunk_size.clone() - 1, content_length.clone() - 1);
            let tx = tx.clone();
            let headers = headers.clone();
            futures.push(async move {
                match self.download_chunk(url, headers,start.clone(), end).await {
                    Ok((start, data)) => {
                        // let len = data.len();
                        // println!("download_chunk start={start} data_size={len}");
                        tx.send((start, data)).await.expect("Failed to send chunk");
                    }
                    Err(e) => {
                        eprintln!("Error downloading chunk: {}", e);
                    }
                }
            });
        }

        // Drop the extra tx handle to indicate there are no more sends.
        drop(tx);

        futures.collect::<Vec<_>>().await;

        let file = File::create(path).await?;
        tokio::pin!(file);

        // 使用一个 BTreeMap 来收集并排序下载的块
        use std::collections::BTreeMap;

        let mut chunks = BTreeMap::new();
        let mut expected_start = 0;

        while let Some((start, chunk)) = rx.recv().await {
            chunks.insert(start, chunk);

            // 立即写入按顺序的块
            while let Some(chunk) = chunks.get(&expected_start) {
                file.write_all(chunk).await?;
                chunks.remove(&expected_start);
                expected_start += chunk_size.clone();
            }
        }


        Ok(())
    }


    async fn download_chunk(&self, url: &str, headers: HashMap<String, String>, start: u64, end: u64) -> Result<(u64, Vec<u8>), ReqwestError> {
        // println!("download_chunk {url} {start}-{end}");
        let mut request_builder = self.client.get(url).header("Range", format!("bytes={}-{}", start, end));
        // 遍历headers HashMap并添加到请求中
        for (key, value) in headers.iter() {
            request_builder = request_builder.header(key, value);
        }
        // 发送请求并等待响应
        let response = request_builder
            .send()
            .await?
            .error_for_status()?;

        Ok((start, response.bytes().await?.to_vec()))
    }
}
