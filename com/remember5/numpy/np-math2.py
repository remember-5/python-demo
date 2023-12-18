# @see https://mofanpy.com/tutorials/data-manipulation/np-pd/np-math1/
import numpy as np

print("================================================")
a = np.random.random((2, 4))
print(a)

print(np.sum(a))
print(np.min(a))
print(np.max(a))

# axis 0列 1行
print("a = ", a)
print("sum = ", np.sum(a, axis=1))
print("min = ", np.min(a, axis=0))
print("max = ", np.max(a, axis=1))

print("================================================")

a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape(2, 2)
print(a)
# [[1 1]
#  [0 1]]
print("-----------------------------------------------")
print(b)
# [[0 1]
#  [2 3]]
print("-----------------------------------------------")
c_dot = np.dot(a, b)
print(c_dot)

print("-----------------------------------------------")
c_dot_2 = a.dot(b)
print(c_dot_2)

print("================================================")

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a)
print(b)

print("================================================")

# numpy 的几种基本运算

c = a - b
print(c)
# [10 19 28 37]

c = a + b
print(c)
# [10 21 32 43]

c = a * b
print(c)
# [  0  20  60 120]


c = b ** 2
print(c)
# [0 1 4 9]


c = 10 * np.sin(a)
print(c)
# [-5.44021111  9.12945251 -9.88031624  7.4511316 ]

print(b < 3)
# [ True  True  True False]
