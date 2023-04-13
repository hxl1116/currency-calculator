use clap::Parser;

#[derive(Debug, Parser)]
#[command(author, version, about)]
pub struct ConversionArgs {
    /// Currency amount
    #[arg(short, long, default_value_t = 1.00)]
    pub amount: f64,

    /// Currency to convert from (three letter code)
    #[arg(short, long, default_value_t = String::from("usd"))]
    pub from: String,

    /// Currency to convert to (three letter code)
    #[arg(short, long)]
    pub to: String,
}
