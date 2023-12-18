# @see https://mofanpy.com/tutorials/python-basic/interactive-python/copy/
from copy import deepcopy



print("================================================")

l = [[1],[2],3]
_l = deepcopy(l)
_l[0][0] = -1
print(_l)
print(l)
# [[-1], [2], 3]
# [[1], [2], 3]

print("================================================")


# 明明源列表是 mp3 的，怎么被复制后的列表改变成了 mp4 了，自动升了各级？查阅 Python 的说明书，你就会发现， 原来在 Python 中复制东西，有两种方式，一种是深拷贝，一种是浅拷贝。
class File:
    def __init__(self, name):
        self.name = name


audio = File("mp3")
file = File("txt")
l = [audio, file]
_l = l.copy()
_l[0].name = "mp4"
print(audio.name)

# mp4


print("================================================")
# 下面我们在用列表把列表里再放一个列表，copy() 源列表 l 去 _l。这次对 _l 里边的小列表修改，看看源列表是什么变化。

l = [[1], [2], [3]]
_l = l.copy()
_l[0][0] = -1
print(_l)
print(l)
# [[-1], [2], [3]]
# [[-1], [2], [3]]


print("================================================")

l = [1, 2, 3]
_l = l.copy()
_l[0] = -1
print(_l)
print(l)
# [-1, 2, 3]
# [1, 2, 3]


print("================================================")
