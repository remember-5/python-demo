import json
import os
import pickle

# 文件系统，机器学习，大数据等，都少不了数据文件。
# Python 也提供了一些比较方便序列化的存储的组件。
# 什么是序列化（Serialization）呢，说简单也简单，就是把像字典，列表这类的数据，
# 打包保存在电脑硬盘中。 如果粗略的理解对比，就有点像 zip 和 unzip 的过程。

# 但是 json 相比 pickle 还是有它不及的点。我们上面已经看到，pickle 可以很轻松的打包 Python 的 class。
# 但是 json 不能序列化保存 class。你只能挑出来重要的信息，放到字典或列表里，然后再用 json 打包字典。
# 下面就是一段 json 打包 class 会报错的代码。





print("================================================")

# 对比	Pickle	Json
# 存储格式	Python 特定的 Bytes 格式	通用 JSON text 格式，可用于常用的网络通讯中
# 数据种类	类，功能，字典，列表，元组等	基本和 Pickle 一样，但不能存类，功能
# 保存后可读性	不能直接阅读	能直接阅读
# 跨语言性	只能用在 Python	可以跨多语言读写
# 处理时间	长（需编码数据）	短（不需编码）
# 安全性	不安全（除非你信任数据源）	相对安全

class File:
    def __int__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def change_name(self, new_name):
        self.name = new_name


data = File("f4.txt", "now", 222)
# 存 会报错
# with open("data.json", "w") as f:
#     json.dump(data, f)

# Traceback (most recent call last):
#   File "/Users/wangjiahao/server/github/python-demo/com/remember5/basic/pickle-json.py", line 23, in <module>
#     data = File("f4.txt", "now", 222)
# TypeError: File() takes no arguments


print("================================================")

data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.json", "w") as f:
    json.dump(data, f)

print("直接当纯文本读：")
with open("data.json", "r") as f:
    print(f.read())

print("用 json 加载了读：")
with open("data.json", 'r') as f:
    new_data = json.load(f)
print("字典读取：", new_data["filename"])

# 直接当纯文本读：
# {"filename": "f1.txt", "create_time": "today", "size": 111}
# 用 json 加载了读：
# 字典读取： f1.txt


print("================================================")

data = {"filename": "f1.txt", "create_time": "today", "size": 111}
j = json.dumps(data)
print(j)
print(type(j))
# {"filename": "f1.txt", "create_time": "today", "size": 111}
# <class 'str'>


print("================================================")


# 如果你硬要用 pickle 保存，我们也还是有解决方案的。
# 用户自定义类可以通过提供 __getstate__() 和 __setstate__() 方法来绕过 pickle 的这些限制。
# pickle.dump() 会调用 __getstate__() 获取序列化的对象。 __setstate__() 在反序列化时被调用。
class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size
        self.file = open(name, "w")

    def __getstate__(self):
        # pickle 出去需要且能被 pickle 的信息
        pickled = {"name": self.name, "create_time": self.create_time, "size": self.size}
        return pickled

    def __setstate__(self, pickled_dict):
        # unpickle 加载回来，重组 class
        self.__init__(
            pickled_dict["name"], pickled_dict["create_time"], pickled_dict["size"])


data = File("f3.txt", "now", 222)
# 存
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
# 读
with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)
print(read_data.name)
print(read_data.size)

print("================================================")


# 有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象， 比如打开的文件，网络连接，线程，进程，栈帧等等

class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size
        self.file = open(name, "w")


data = File("f3.txt", "now", 222)
# pickle 存，会报错
# with open("data.pkl", "wb") as f:
#     pickle.dump(data, f)

# Traceback (most recent call last):
#   File "/Users/wangjiahao/server/github/python-demo/com/remember5/basic/pickle-json.py", line 24, in <module>
#     pickle.dump(data, f)
# TypeError: cannot pickle '_io.TextIOWrapper' object

print("================================================")


class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def chang_name(self, new_name):
        self.name = new_name


data = File("f2.txt", "now", 222)
# 存储
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# 读取
with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)
    print(read_data)
print(read_data.name)
print(read_data.size)

# <__main__.File object at 0x7fd26ee89f70>
# f2.txt
# 222

print("================================================")

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
    print(data)

# {'filename': 'f1.txt', 'create_time': 'today', 'size': 111}

print("================================================")

data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

os.listdir()

print("================================================")
data = {"filename": "f1.txt", "create_time": "today", "size": 111}
print(pickle.dumps(data))

# b'\x80\x04\x958\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08filename\x94\x8c\x06f1.txt\x94\x8c\x0bcreate_time\x94\x8c\x05today\x94\x8c\x04size\x94Kou.'
