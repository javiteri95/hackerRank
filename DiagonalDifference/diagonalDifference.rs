extern crate ndarray;
use ndarray::arr2;


fn diagonal_difference(matrix: &arr2) -> i32 {
    let mut principal_diag = 0;
    let mut second_diag = 0;
    for i in 0..matrix.len() {
        for j in 0..matrix.len() {
            if i == j {
                principal_diag += matrix[i][j];
            } else if (matrix.len() -1) - i == j {
                second_diag += matrix[i][j];
            }
        }
    }
    let returning: i32 = principal_diag - second_diag;
    returning.abs()
}

fn main() {
    let array = arr2(&[[1,2,3],[4,5,6], [7,8,9]]);
    let value = diagonal_difference(&array);
    println!("{}",value);
}
