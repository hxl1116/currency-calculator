use crate::rate::{get_forex_rate, ForexRate};

#[derive(Debug, Default)]
pub struct Conversion {
    pub symbol: String,
    pub value: f64,
}

pub fn convert_currency(amt: f64, from: String, to: String) -> Conversion {
    let from_rate: ForexRate = get_forex_rate(from).unwrap();
    let to_rate: ForexRate = get_forex_rate(to).unwrap();

    Conversion {
        symbol: to_rate.symbol,
        value: amt * from_rate.inverse * to_rate.rate,
    }
}
