#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    swaps = 0
    reverse_swaps = 0
    sorted_up_array = arr[:]
    sorted_down_array = arr[:]
    i = 0

    # sorted_up_arr : [1,2,3,4,5]
    # sorted_down_arr : [5,4,3,2,1]
    while sorted(sorted_up_array) != sorted_up_array or sorted(sorted_down_array, reverse=True) != sorted_down_array:
        
        temp_arr_up = sorted_up_array[i:]
        temp_arr_down = sorted_down_array[i:]

        min_element = min(temp_arr_up)
        index_min_element = temp_arr_up.index(min_element)

        max_element = max(temp_arr_down)
        index_max_element = temp_arr_down.index(max_element)

        if index_min_element != 0:
            temp_arr_up[index_min_element] = temp_arr_up[0]
            temp_arr_up[0] = min_element
            swaps += 1
        
        if index_max_element != 0:
            temp_arr_down[index_max_element] = temp_arr_down[0]
            temp_arr_down[0] = max_element
            reverse_swaps += 1

        sorted_up_array[i:] = temp_arr_up
        
        sorted_down_array[i:] = temp_arr_down

        i += 1
    
    return min([swaps, reverse_swaps])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()