use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input1")?;
    let reader = BufReader::new(file);
    let mut previous = 9999;
    let mut c = 0;
    for line in reader.lines() {
	let current = line?.parse().unwrap();
	if current > previous {
	    c += 1;
	}

	previous = current;
    }

    println!("{}", c);

    Ok(())
}
