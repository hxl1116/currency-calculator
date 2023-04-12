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
        value: amt * from_rate.inverse
    }
}

pub fn get_conv_from_usd(amt: f64, to: String) -> Conversion {
    let to_rate: ForexRate = get_forex_rate(to).unwrap();

    Conversion {
        symbol: to_rate.symbol,
        value: amt * to_rate.rate
    }
}

pub fn get_conv(amt: f64, from: String, to: String) -> Conversion {
    let from_rate: ForexRate = get_forex_rate(from).unwrap();
    let to_rate: ForexRate = get_forex_rate(to).unwrap();

    Conversion {
        symbol: to_rate.symbol,
        value: amt * from_rate.inverse * to_rate.rate
    }
}
