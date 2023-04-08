use redis::{Commands, RedisResult};
use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct ForexRate {
    symbol: String,
    name: String,
    rate: f64,
    inverse: f64,
}

pub fn redis_client() -> redis::Client {
    redis::Client::open("redis://127.0.0.1:6379").unwrap()
}

pub fn get_forex_symbols() -> RedisResult<()> {
    let mut conn = redis_client().get_connection().unwrap();
    let result: () = conn.hgetall("forex_rates").unwrap();

    dbg!(&result);
    Ok(result)
}

pub fn get_forex_rate(forex_symbol: String) -> RedisResult<()> {
    let mut conn = redis_client().get_connection().unwrap();
    let forex_key = format!("forex_rate:{}", forex_symbol);
    let res: () = conn.hgetall(forex_key).unwrap();

    dbg!(&res);

    Ok(res)
}
