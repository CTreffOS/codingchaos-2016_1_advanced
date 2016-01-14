// AAAAAH NIGHTLY
#![feature(time2)]

use std::*;
use std::process::{Command, ExitStatus};

const ALPHA: &'static str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn build(pass: &str) -> Command {
    let mut cmd = Command::new("../crypto");
    cmd.arg(pass);
    cmd
}

/// Millisekunden messen
fn run_timed(pass: &str) -> u64 {
    //build(pass)
    let now = time::SystemTime::now();
    if build(pass).status().unwrap().code().unwrap() == 0 {
        println!("PASSWORT: {}", pass);
        process::exit(0);
    }
    let el = now.elapsed().unwrap();
    el.as_secs() * 1000 + el.subsec_nanos() as u64 / 1000000
}

/// Laufen lassen und return code zurückgeben
fn run_ret(pass: &str) -> ExitStatus {
    build(pass).status().unwrap()
}

fn main() {
    // Finde Länge
    let mut len = 0;
    for i in 0..100 {
        println!("{}", i);
        if run_ret(&iter::repeat('A').take(i).collect::<String>()).code().unwrap() == 2 {
            // zu lang
            len = i - 1;
            break;
        }
    }

    println!("Länge: {}", len);
    let mut pass = iter::repeat('A').take(len).collect::<String>();
    for i in 0..len {
        let mut times = Vec::new();
        for letter in ALPHA.chars() {
            pass = pass.chars().enumerate().map(|(idx, c)| if idx == i { letter } else { c }).collect();
            let ms = run_timed(&pass);
            println!("{} als zeichen {} ({}): {} ms", letter, i, pass, ms);
            times.push(ms);
        }

        let (idx, _) = times.iter().enumerate().max_by_key(|&(_, i)| *i).unwrap();
        let letter = ALPHA.chars().skip(idx).next().unwrap();
        println!("{}", letter);
        pass = pass.chars().enumerate().map(|(idx, c)| if idx == i { letter } else { c }).collect();
    }
}
