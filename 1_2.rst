use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input1")?;
    let reader = BufReader::new(file);
    let mut array: [i32; 2000] = [0; 2000];
    let mut previous = 99999;
    let mut c = 0;
    let mut i = 0;
    
    for line in reader.lines() {
	let x = line?.parse().unwrap();
	array[i] = x;
	i += 1;
    }

    for n in 0..1998 {
        let current = array[n] + array[n + 1] + array[n + 2];

	if current > previous {
	    c += 1;
	}

	previous = current;
    }

    println!("{}", c);

    Ok(())
}
