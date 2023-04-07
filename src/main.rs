mod args;
mod rate;

use args::CalcArgs;
use clap::Parser;

fn main() {
    let _args = CalcArgs::parse();

    // TODO: Handle args and calculate conversion
}
