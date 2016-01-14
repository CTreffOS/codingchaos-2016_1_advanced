use std::*;
use std::io::prelude::*;
use std::fs::*;

fn main() {
    let mut args = env::args();
    args.next().unwrap();
    let input = args.next().unwrap();
    let out = args.next().unwrap();

    let mut input = File::open(input).unwrap();
    let mut output = File::create(out).unwrap();

    let mut data = Vec::new();
    input.read_to_end(&mut data).unwrap();
    let mut samples = Vec::<i16>::new();

    for s in data.chunks(2) {
        let (lo, hi) = (s[0] as u16, s[1] as u16);
        samples.push((hi << 8 | lo) as i16);
    }

    println!("{} samples", samples.len());
    let mut hsamp = Vec::new();
    let offset = samples.len() / 1000;
    for (i, s) in samples.iter().enumerate() {
        if i % offset == 0 { hsamp.push(*s); }
        if hsamp.len() == 1000 { break }    // Den Rest verwerfen
    }

    println!("{} samples", hsamp.len());
    for i in &mut hsamp {
        *i >>= 8;
    }

    write!(output, "P1\n1000\n255\n").unwrap();
    for y in (0..128).rev().chain(0..128) {
        for &s in &hsamp {
            write!(output, "{} ", if s >= y { "1" } else { "0" }).unwrap();
        }
    }
}
