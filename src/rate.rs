use redis::{Client, Commands, RedisResult, RedisError};
use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct ForexRate {
    symbol: String,
    name: String,
    ratio: f64,
    inversion: f64,
}

fn fetch_rate(rate_symbol: String) -> RedisResult<()> {
    let client = Client::open("redis://127.0.0.1/")?;
    let mut conn = client.get_connection()?;

    // let _ : RedisResult<RV> = conn.hget(String::from("forex_rate:"), rate_symbol);

    Ok(())
}
