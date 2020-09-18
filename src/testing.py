import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6]) 

arr2 = np.array(['apple', 'banana', 'cherry'])

newarr = arr.reshape(2, 3)

print(arr)

print(arr[0])

print(arr[1:2])

print(arr.dtype)

print(arr2.dtype)

print(arr.shape)

print(newarr)