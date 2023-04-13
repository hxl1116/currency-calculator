use crate::rate::{get_conversion_info, ConversionInfo};

pub fn convert_currency(amt: f64, from: String, to: String) -> f64 {
    let from_rate: ConversionInfo = get_conversion_info(from).unwrap();
    let to_rate: ConversionInfo = get_conversion_info(to).unwrap();
    
    amt * from_rate.inverse * to_rate.rate
}
