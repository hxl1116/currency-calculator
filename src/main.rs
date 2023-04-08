mod args;
mod conv;

use args::CalcArgs;
use clap::Parser;
use conv::get_conv;

fn main() {
    let args = CalcArgs::parse();

    let _res = get_conv(args.from, args.to, args.amount);

    // let forex_from = format!("forex_rate:{symbol}", symbol=_args.from);
    // let forex_to = format!("forex_rate:{symbol}", symbol=_args.to);
}
