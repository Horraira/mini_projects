from numpy import array
import numpy as np
from array import *

arr1 = array('i', [1, 2, 3, 5])
print(arr1)
# insertion operation
arr1.insert(1, 5)
print(arr1)


# searching for element in array
# B(O) = O(n)
def searchInArray(arr,
                  value):
    for i in arr:
        if i == value:
            return arr.index(value)
    return "Element is not in array"


print(searchInArray(arr1, 5))

# array remove
arr1.remove(5)
print(arr1)

# extend array
arr2 = array('i', [10, 11, 12])
arr1.extend(arr2)
print(arr1)

# reverse
arr1.reverse()
print(arr1)

# 2d array
twoDArray = np.array([[11, 12, 13],
                      [14, 15, 16],
                      [18, 21, 22]])
print(twoDArray)
newArray = np.insert(twoDArray, 1, [[1, 2, 3]], axis=1)
print(newArray)
new2DArray = np.append(twoDArray, [[2, 12, 20]], axis=0)
print(new2DArray)
