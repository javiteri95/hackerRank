

fn a_very_big_sum(ar: &[i32]) -> i32{
    let mut sum = 0;
    for element in ar.iter() {
        sum += element;
    }
    sum
}

fn main() {
    let array = [1,2,34];
    let sum = a_very_big_sum(&array);
    println!("The value of sum is: {}", sum);
}