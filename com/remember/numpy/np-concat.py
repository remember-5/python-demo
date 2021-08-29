# @See https://mofanpy.com/tutorials/data-manipulation/np-pd/np-concat/

import numpy as np




print("================================================")

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.concatenate((A,B,B,A),axis=0)
print(C)
print(C.shape)

# [[1]
#  [1]
#  [1]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [1]
#  [1]
#  [1]]
# (12, 1)


D = np.concatenate((A,B,B,A),axis=1)
print(D)
print(D.shape)
# [[1 2 2 1]
#  [1 2 2 1]
#  [1 2 2 1]]
# (3, 4)


print("================================================")

print(A)
# [[1]
#  [1]
#  [1]]
print(B)
# [[2]
#  [2]
#  [2]]
C = np.vstack((A, B))
# [[1]
#  [1]
#  [1]
#  [2]
#  [2]
#  [2]]
D = np.hstack((A, B))
# [[1 2]
#  [1 2]
#  [1 2]]

print(C.shape)
# (6, 1)
print(D.shape)
# (3, 2)


print(C)
print(D)

print("================================================")

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print(np.vstack((A, B)))

# 合并为阵列

C = np.vstack((A, B))
print(A.shape, C.shape)

print("================================================")

print(A[np.newaxis, :])
# [[1 1 1]]
print(A[np.newaxis, :].shape)
# (1, 3)

print(A[:, np.newaxis])
# [[1]
#  [1]
#  [1]]
print(A[:, np.newaxis].shape)
# (3, 1)


print("================================================")

# np.hstack() 合并为数列
D = np.hstack((A, B))  # horizontal stack

print(D)
# [1,1,1,2,2,2]

print(A.shape, D.shape)
# (3,) (6,)

print("================================================")
