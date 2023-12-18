# @see https://mofanpy.com/tutorials/data-manipulation/np-pd/np-array/

import numpy as np

# array：创建数组
# dtype：指定数据类型
# zeros：创建数据全为0
# ones：创建数据全为1
# empty：创建数据接近0
# arrange：按指定范围创建数据
# linspace：创建线段


a = np.linspace(1, 10, 20).reshape(4, 5)
print(a)

print("================================================")

# 用linspace创建险段型数据
a = np.linspace(1, 10, 20)  # 开端1 结束端10 切分割成20个数据，生成线段
print(a)

print("================================================")

# 使用reshape改变数据类型
a = np.arange(12).reshape((3, 4))  # 3行4列，0到11
print(a)

print("================================================")

# 用 arange 创建连续数组
a = np.arange(10, 20, 2)  # 10-19的数据，2步长
print(a)
# [10 12 14 16 18]

print("================================================")

# 创建全空数组，其实每个值都是接近于0的数
a = np.empty((3, 4))
print(a)

print("================================================")

# 创建全一数组, 同时也能指定这些特定数据的 dtype:
a = np.ones((3, 4), dtype=np.int_)
print(a)

print("================================================")

# 创建全零数组
a = np.zeros((3, 4))
print(a)
print("================================================")

# 创建特定数据
a = np.array([[2, 23, 4], [2, 32, 4]])
print(a)
print("================================================")

# 指定类型 dtype

# a = np.array([2, 55, 4], dtype=np.int)
# print(a.dtype)

# a = np.array([2, 25, 4], dtype=np.int32)
# print(a.dtype)

# a = np.array([2, 33, 4], dtype=np.float)
# print(a.dtype)

# a = np.array([2, 33, 4], dtype=np.float32)
# print(a.dtype)


print("================================================")

# 创建数组array

# a = np.array([2, 23, 4])  # list id
# print(a)

print("================================================")
