use sha1::{Sha1, Digest};
use std::fs;
use std::io::{Read};

const BUFFER_SIZE: u32 = 65536;

fn print_result(sum: &[u8], name: &str) {
    for byte in sum {
        print!("{:02x}", byte);
    }
    println!("\t{}", name);
}

fn process<D: Digest + Default, R: Read>(reader: &mut R, name: &str) {
    let mut sh = D::default();
    let mut buffer = [0u8; BUFFER_SIZE];
    loop {
        let n = match reader.read(&mut buffer) {
            Ok(n) => n,
            Err(_) => return,
        };
        sh.input(&buffer[..n]);
        if n == 0 || n < BUFFER_SIZE {
            break;
        }
    }
    print_result(&sh.result(), name);
}


pub fn compare_hashes(path:String) {
    
    println!("file_path: {}", path);
    

    let file = fs::File::open(&path);
    process::<Sha1, _>(&mut file, &path);



}
