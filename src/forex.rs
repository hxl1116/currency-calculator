use redis::{Commands, RedisResult};
use serde::Deserialize;

#[derive(Debug, Default, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct ConversionInfo {
    pub code: String,
    pub name: String,
    pub rate: f64,
    pub inverse: f64,
}

pub fn redis_client() -> redis::Client {
    redis::Client::open("redis://127.0.0.1:6379").unwrap()
}

pub fn get_forex_codes() -> RedisResult<Vec<String>> {
    let mut conn = redis_client().get_connection().unwrap();
    let result: Vec<String> = conn.hgetall("forex_rates").unwrap();
    
    Ok(result)
}

pub fn get_conversion_info(forex_symbol: String) -> RedisResult<ConversionInfo> {
    let mut conn = redis_client().get_connection().unwrap();
    let result: Vec<String> = conn.hvals(format!("forex_rate:{}", forex_symbol)).unwrap();

    let rate = ConversionInfo {
        code: result[0].clone(),
        name: result[1].clone(),
        rate: result[2].parse().unwrap(),
        inverse: result[3].parse().unwrap(),
    };

    Ok(rate)
}
