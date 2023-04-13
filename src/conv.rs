use crate::rate::{get_forex_rate, ForexRate};

pub fn convert_currency(amt: f64, from: String, to: String) -> f64 {
    let from_rate: ForexRate = get_forex_rate(from).unwrap();
    let to_rate: ForexRate = get_forex_rate(to).unwrap();
    
    amt * from_rate.inverse * to_rate.rate
}
