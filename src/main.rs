mod args;
mod conv;
mod rate;

use args::ConversionArgs;
use clap::Parser;

fn main() {
    let _args = ConversionArgs::parse();

    // TODO: Handle arguments
}
