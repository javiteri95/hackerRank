#!/bin/python3

import math

# Complete the encryption function below.
def encryption(s):
    matrix = []
    string_not_spaces = s.replace(" ", "")
    total_len = len(string_not_spaces)
    sqrt_total_len = total_len ** 0.5
    ceil = math.ceil(sqrt_total_len)
    row = []
    matrix = []
    for i in range(0, len(string_not_spaces)):
        row.append(string_not_spaces[i])
        if (((i+1) % ceil == 0) or i == len(string_not_spaces) -1):
            matrix.append(row)
            row = []
    transpose_matrix = transpose(matrix)
    response_str = ""
    for i in range(0, len(transpose_matrix)):
        response_str+=" "
        for j in range(0,len(transpose_matrix[i])):
            response_str+=transpose_matrix[i][j]

    return response_str.strip()

def transpose(matrix):
    transpose_matrix = [[] for j in range(0,len(matrix[0]))]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            transpose_matrix[j].append(matrix[i][j])
    return transpose_matrix



if __name__ == "__main__":
    s = "if man was meant to stay on the ground god would have given us roots"
    s = "haveaniceday"
    s = "feedthedog"
    s = "chillout"
    s_1 = encryption(s)
    print(s_1)