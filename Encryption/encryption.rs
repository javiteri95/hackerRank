

fn encryption(s: &str) -> String {
    let string_not_spaces: String = s.split_whitespace().collect();
    let string_size = string_not_spaces.len() as usize;
    let ceil = (string_size as f64).sqrt() as usize + 1;
    let floor = ceil -1 ;
    let mut matrix : Vec<Vec<char>> = vec![vec![Default::default(); floor]; ceil];
    let mut row: Vec<char> = vec![Default::default(); floor];
    for i in 0..string_size {
        row.push(string_not_spaces[i]);
        if ((i+1) % ceil == 0) || i == string_not_spaces.len() -1 {
            matrix.push(row);
            row = vec![Default::default(); floor];
        }
    }
    let mut transposed_matrix : Vec<Vec<char>> = vec![vec![Default::default(); ceil]; floor];
    for i in 0..transposed_matrix.len() {
        for j in 0..transposed_matrix[i].len() {
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
    let s = "if man was meant to stay on the ground god would have given us roots";
    let encrypted = encryption(s);
}