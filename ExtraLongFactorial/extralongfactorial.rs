
fn extraLongFactorials(n: i32) -> i32 {
    if n == 0 {
        return 1;
    }
    n * extraLongFactorials(n -1)
}

fn main() {
    let number = 6;
    let factorial = extraLongFactorials(number);
    println!("factorial is: {}", factorial);
}