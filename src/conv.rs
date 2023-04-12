use serde::Deserialize;

use crate::rate::{get_forex_rate, ForexRate};

#[derive(Debug, Default)]
pub struct Conversion {
    pub symbol: String,
    pub value: f64,
}

pub fn get_conv_to_usd(amt: f64, from: String) -> Conversion {
    let from_rate: ForexRate = get_forex_rate(from).unwrap();

    Conversion {
        symbol: from_rate.symbol,
        value: amt * from_rate.inverse,
    }
}

// TODO: Implement conversion func from USD to target currency
pub fn get_conv_from_usd() -> () {}

// TODO: Implement conversion func for currency parameters
pub fn get_conv(amt: f64, from: String, to: String) -> () {}
