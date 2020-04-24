pub mod tools;

use std::env;
use tools::mod_status;

// run CLI version of app
fn cli() {
    println!("Running CLI...");
    // Literally just using this to test things right now.
    mod_status::compare_hashes(String::from("test.txt"));
}

// run GUI version of app
fn gui() {
    println!("Eventually GUI functionality will go here.");
}

// warn invalid usage of app
macro_rules! help_message {
    () => {
        println!("Invalid usage.");
    };
}

fn main() {
    /* execute based on arguments, if supplied
     * defaults to CLI, for now
     * will eventually default to GUI once more work has been put there
     */
    let args: Vec<String> = env::args().collect();
    match args.len() {
        1 => cli(),
        2 => {
            match args[1].as_str() {
                "-cli" => cli(),
                "-gui" => gui(),
                _ => help_message!(),
            }
        }
        _ => help_message!(),
    }

    println!("Done.");
}
