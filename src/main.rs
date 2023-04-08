mod args;
mod conv;
mod rate;

use args::CalcArgs;
use clap::{builder::Str, Parser};
use rate::{get_forex_symbols, redis_client};
use redis::{Commands, FromRedisValue};

fn main() {
    // let _args = CalcArgs::parse();

    let mut conn = redis_client().get_connection().unwrap();
    // let _: () = redis::cmd("SET")
    //     .arg("foo")
    //     .arg("bar")
    //     .query(&mut conn)
    //     .expect("failed to execute SET for 'foo'");

    let bar: Vec<String> = redis::cmd("HGETALL")
        .arg("forex_rates")
        .query(&mut conn)
        .expect("failed to execute HGETALL for 'forex_rates'");

    dbg!(&bar);
}
