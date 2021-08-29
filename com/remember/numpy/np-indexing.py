# @see https://mofanpy.com/tutorials/data-manipulation/np-pd/np-indexing/
import numpy as np




A = np.arange(3,15).reshape((3,4))
print(A)

# [[ 3  4  5  6]
#  [ 7  8  9 10]
#  [11 12 13 14]]

# flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。而flat是一个迭代器，本身是一个object属性。
print(A.flatten())
# [ 3  4  5  6  7  8  9 10 11 12 13 14]


print("================================================")



A = np.arange(3,15)
print(A)
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

print(A[3])  # 6
print("================================================")
A = np.arange(3, 15).reshape((3, 4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""

print(A[2])
# [11 12 13 14]
print(A[1][1])      # 8
print("================================================")

# 二维索引

print(A[1][1])
print(A[1,1])
print(A[1,1:3])

for row in A:
    print(row)
# [3 4 5 6]
# [ 7  8  9 10]
# [11 12 13 14]

for column in A.T:
    print(column)
# [ 3  7 11]
# [ 4  8 12]
# [ 5  9 13]
# [ 6 10 14]






