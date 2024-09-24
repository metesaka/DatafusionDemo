use datafusion::prelude::*;
use object_store::aws::AmazonS3Builder;
use url::Url;
use std::sync::Arc;
use anyhow::{anyhow, Result};

#[tokio::main]


async fn main() -> Result<()> {
    let ctx: SessionContext = SessionContext::new();
    let base_url = Url::parse("http://localhost:8333").unwrap();
    let weed: object_store::aws::AmazonS3 = AmazonS3Builder::new()
    .with_endpoint("http://localhost:8333")
    .with_allow_http(true)
    .with_bucket_name("tpchDummy")
    .with_access_key_id("admin")
    .with_secret_access_key("admin")
    .build()?;
    let supp_url = Url::parse("s3://tpchDummy").unwrap();

    ctx.register_object_store(&supp_url, Arc::new(weed));
    ctx.register_parquet("supplier", "s3://tpchDummy/supplier/supplier1.parquet", ParquetReadOptions::default()).await?;
  
    // create a plan to run a SQL query
    let df = ctx.sql("SELECT * FROM supplier LIMIT 10").await?;
  
    // execute and print results
    df.show().await?;
    Ok(())
  }