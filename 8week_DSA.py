def biggest(arr):
    biggest_num = arr[0]
    for index in range (1, len(arr)):
        if arr[index] > biggest_num:
            biggest_num = arr[index]
    return biggest_num

print(biggest([10, 23, 3, 4,92, 52]))

import array 

arr = array.array('i', [1, 2, 3, 4, 5])

print( arr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)