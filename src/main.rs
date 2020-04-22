pub mod tools;

use std::env;
use tools::mod_status::check_if_modded;

fn help() {
    println!("I don't do anything yet!");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    
    for arg in args {
        println!("{}",arg );
    
    }
    help();
    tools::mod_status::check_if_modded("hi".to_string(), "hello".to_string());
}
