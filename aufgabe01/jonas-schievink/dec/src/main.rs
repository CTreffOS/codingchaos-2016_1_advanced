//! `cargo run <ciphertext>`

use std::*;

const KEY: &'static str = "chaostreffosnabrueck";
const ALPHABET: &'static str = "abcdefghijklmnopqrstuvwxyz";

fn decrypt(text: &str, key: &str) -> String {
    let mut keyloop = key.chars().cycle();
    let mut s = String::new();

    for ch in text.chars() {
        let row = keyloop.next().unwrap();
        let mut caesar = ALPHABET.chars().cycle().skip(row as usize - 'a' as usize);
        let col = caesar.position(|x| x == ch).unwrap();
        let ch = col + 'a' as usize;
        s.push(ch as u8 as char);
    }

    s
}

fn main() {
    let mut args = env::args();
    args.next().unwrap();
    let text = args.next().unwrap();
    println!("{}", decrypt(&text, KEY));
}
