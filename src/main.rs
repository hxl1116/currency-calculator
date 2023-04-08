mod args;
mod conv;
mod rate;

use args::CalcArgs;
use clap::Parser;
use rate::get_forex_symbols;

fn main() {
    // let _args = CalcArgs::parse();

    // let mut conn = redis_client().get_connection().unwrap();
    // let result: () = redis::cmd("PING").query(&mut conn).unwrap();

    // dbg!(&result);

    // get_forex_symbols().unwrap();
}
