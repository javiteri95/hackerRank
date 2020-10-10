def diagonalDifference(arr):
    firstDiag = 0
    secondDiag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                firstDiag+= arr[i][j]
            if (len(arr) - i) == j + 1:
                secondDiag += arr[i][j]
    
    return abs(firstDiag - secondDiag)
    # Write your code here

'''
[
    1,2,3
    4,5,6
    7,8,9
]


'''

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    difference = diagonalDifference(arr)
    print(difference)
