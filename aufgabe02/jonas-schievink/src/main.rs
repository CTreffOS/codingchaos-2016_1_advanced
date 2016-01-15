extern crate serde_json;
extern crate hyper;

use std::*;
use std::io::prelude::*;
use hyper::client::*;
use hyper::header::UserAgent;

fn main() {
    let mut args = env::args();
    args.next().unwrap();
    let user = args.next().unwrap();
    let repo = args.next().unwrap();
    println!("Fetching {}/{}", user, repo);

    let client = Client::new();

    let mut res = client.get(&format!(
        "https://api.github.com/repos/{}/{}/pulls?access_token=c7af25b8fa0c8ceee6381d4db69094446f059e6a", user, repo)).header(UserAgent("Blerg".to_string())).send().unwrap();
    let mut data = Vec::new();
    res.read_to_end(&mut data).unwrap();
    let s = String::from_utf8(data).unwrap();
    //println!("{}", s);
    assert_eq!(res.status, hyper::Ok);

    let data: serde_json::Value = serde_json::from_str(&s).unwrap();
    for pr in data.as_array().unwrap().iter() {
        let obj = pr.as_object().unwrap();
        if obj["state"].as_string().unwrap() == "open" {
            let num = obj["number"].as_u64().unwrap();
            let author = obj["user"].as_object().unwrap()["login"].as_string().unwrap();
            let title = obj["title"].as_string().unwrap();

            println!("{}\t{}\t{}", num, author, title);
        }
    }
}
