# @see https://mofanpy.com/tutorials/python-basic/interactive-python/lazy-usage/

# 最后一种是要 copy 出一个浅拷贝副本的反转

l = [1,2,3]
_l = l[::-1]
print(_l)
# [3, 2, 1]


l = [1,2,3]
for i in reversed(l):
    print(i)


l = [1, 2, 3]
l.reverse()
print(l)
# [3, 2, 1]


l = [1, 2, 3]
_l = [l[-i - 1] for i in range(len(l))]
print(_l)
# [3, 2, 1]

l = [1, 2, 3]
_l = []
for i in range(len(l)):
    _l.append(l[-i - 1])
print(_l)
# [3, 2, 1]

print("================================================")

name = ["a", "b", "c"]
score = [1, 2, 3]
bonus = [1, 0, 1]
d = {}
for n, s, b in zip(name, score, bonus):
    d[n] = s + b
print(d)
# {'a': 2, 'b': 2, 'c': 4}


name = ["a", "b", "c"]
score = [1, 2, 3]
d = {}

for n, s in zip(name, score):
    d[n] = s
print(d)
# {'a': 1, 'b': 2, 'c': 3}


name = ["a", "b", "c"]
score = [1, 2, 3]
d = {}

for i in range(3):
    d[name[i]] = score[i]
print(d)
# {'a': 1, 'b': 2, 'c': 3}

print("================================================")

# enumerate
l = [11, 22, 33, 44]
d = {}
for count, data in enumerate(l, start=5):
    d[count] = data
print(d)
# {5: 11, 6: 22, 7: 33, 8: 44}


l = [11, 22, 33, 44]
for count, data in enumerate(l):
    if count == 2:
        data += 11
    l[count] = data
print(l)
# [11, 22, 44, 44]

count = 0
l = [11, 22, 33, 44]
for data in l:
    if count == 2:
        data += 11
    l[count] = data
    count += 1
print(l)
# [11, 22, 44, 44]


print("================================================")

d = {"index" + str(i): i * 2 for i in range(10) if i % 2 == 0}
print(d)
# {'index0': 0, 'index2': 4, 'index4': 8, 'index6': 12, 'index8': 16}


print("================================================")

l = [i * 2 for i in range(10) if i % 2 == 0]
print(l)
# [0, 4, 8, 12, 16]


l = []
for i in range(10):
    if i % 2 == 0:
        l.append(i * 2)

print(l)
# [0, 4, 8, 12, 16]


print("================================================")

done = False
a = 1 if done else 2
print(a)
# 2


done = False
if done:
    a = 1
else:
    a = 2
print(a)

# 2

print("================================================")

d = {"index" + str(i): i ** 2 for i in range(1, 10)}
print(d)

# {'index1': 1, 'index2': 4, 'index3': 9, 'index4': 16, 'index5': 25, 'index6': 36, 'index7': 49, 'index8': 64, 'index9': 81}


print("================================================")

l = []
for i in range(10):
    l.append(i * 2)
print(l)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print("================================================")

add = lambda a, b: a + b
print(add(1, 2))
# 3

print("================================================")


def add(a, b):
    return a + b


print(add(1, 2))
# 3

print("================================================")
