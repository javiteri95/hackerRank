
fn staircase(n: i32) -> () {
    for i in 1..n+1 {
        for _j in 0..n-i {
            print!(" ");
        }
        for _k in 0..i {
            print!("#");
        }
        println!();
    }
}

fn main() {
    let n = 4;
    staircase(n)
}