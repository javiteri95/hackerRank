

fn encryption(s: &str) -> String {
    let string_not_spaces: String = s.split_whitespace().collect();
    let string_size = string_not_spaces.len() as usize;
    let ceil = (string_size as f64).sqrt() as usize + 1;
    let floor = ceil -1 ;
    let mut matrix : Vec<Vec<char>> = Vec::with_capacity(ceil);
    let mut row: Vec<char> = Vec::with_capacity(floor);
    for i in 0..string_size {
        row.push(string_not_spaces.chars().nth(i).unwrap());
        if ((i+1) % ceil == 0) || i == string_not_spaces.len() -1 {
            matrix.push(row);
            row = Vec::with_capacity(floor);
        }
    }
    let mut transposed_matrix : Vec<Vec<char>> = Vec::with_capacity(floor);

    for _i in 0..ceil {
        let row = Vec::with_capacity(ceil);
        transposed_matrix.push(row);
    }
    for i in 0..matrix.len() {
        for j in 0..matrix[i].len() {
            transposed_matrix[j].push(matrix[i][j]);
        }
    }

    let mut string_response = "".to_owned();
    for i in 0..transposed_matrix.len() {
        string_response.push_str(" ");
        for j in 0..transposed_matrix[i].len() {
            string_response.push(transposed_matrix[i][j]);
        }
    }
    string_response

}

fn main() {
    //let s = "if man was meant to stay on the ground god would have given us roots";
    let s = "chillout";
    let encrypted = encryption(s);
    println!("{}",encrypted);
}