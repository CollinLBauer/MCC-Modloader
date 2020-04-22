pub mod tools;

use std::env;
use tools::mod_status::check_if_modded;

fn cli() {
    println!("Eventually CLI functionality will go here.");
    println!("CLI is mostly for testing and early implementation.");
}

fn gui() {
    println!("Eventually GUI functionality will go here.");
}

fn help_message() {
    println!("Invalid usage.");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    
    match args.len() {
        1 => {
            gui();
        }
        2 => {
            match args[1].as_str() {
                "-cli" => {
                    cli();
                }
                "-gui" => {
                    gui();
                }
                _ => {
                    help_message();
                }
            }
        }
        _ => {
            help_message();
        }
    }

    println!("Done.");
}
