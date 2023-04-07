use clap::Parser;

#[derive(Debug, Parser)]
#[command(author, version, about)]
pub struct CalcArgs {
    /// Currency amount
    #[arg(short, long, default_value_t = 1.00)]
    pub amount: f64,

    /// From currency
    #[arg(short, long, default_value_t = String::from("usd"))]
    pub from: String,

    /// To currency
    #[arg(short, long)]
    pub to: String,
}
