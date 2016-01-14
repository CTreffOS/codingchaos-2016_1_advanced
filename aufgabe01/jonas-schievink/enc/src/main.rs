//! `cargo run <plaintext>`

use std::*;

const KEY: &'static str = "chaostreffosnabrueck";
const ALPHABET: &'static str = "abcdefghijklmnopqrstuvwxyz";

fn encrypt(text: &str, key: &str) -> String {
    let mut keyloop = key.chars().cycle();
    let mut s = String::new();

    for ch in text.chars() {
        let row = keyloop.next().unwrap();
        let caesar = ALPHABET.chars().cycle().skip(row as usize - 'a' as usize);
        let col = ch as usize - 'a' as usize;
        s.push(caesar.skip(col).next().unwrap() as char);
    }

    s
}

fn main() {
    let mut args = env::args();
    args.next().unwrap();
    let text = args.next().unwrap();
    println!("{}", encrypt(&text, KEY));
}
