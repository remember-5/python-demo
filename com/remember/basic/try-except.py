# 还好，在 Python 中，或者任何语言中，都有一些处理错误的方式，handler 这些错误，保证你的程序可以顺利执行下去。
# @see https://mofanpy.com/tutorials/python-basic/interactive-python/try-except/


#  Python异常错误名称表


# 异常名称	描述
# BaseException	所有异常的基类
# SystemExit	解释器请求退出
# KeyboardInterrupt	用户中断执行(通常是输入^C)
# Exception	常规错误的基类
# StopIteration	迭代器没有更多的值
# GeneratorExit	生成器(generator)发生异常来通知退出
# StandardError	所有的内建标准异常的基类
# ArithmeticError	所有数值计算错误的基类
# FloatingPointError	浮点计算错误
# OverflowError	数值运算超出最大限制
# ZeroDivisionError	除(或取模)零 (所有数据类型)
# AssertionError	断言语句失败
# AttributeError	对象没有这个属性
# EOFError	没有内建输入,到达EOF 标记
# EnvironmentError	操作系统错误的基类
# IOError	输入/输出操作失败
# OSError	操作系统错误
# WindowsError	系统调用失败
# ImportError	导入模块/对象失败
# LookupError	无效数据查询的基类
# IndexError	序列中没有此索引(index)
# KeyError	映射中没有这个键
# MemoryError	内存溢出错误(对于Python 解释器不是致命的)
# NameError	未声明/初始化对象 (没有属性)
# UnboundLocalError	访问未初始化的本地变量
# ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError	一般的运行时错误
# NotImplementedError	尚未实现的方法
# SyntaxError	Python 语法错误
# IndentationError	缩进错误
# TabError	Tab 和空格混用
# SystemError	一般的解释器系统错误
# TypeError	对类型无效的操作
# ValueError	传入无效的参数
# UnicodeError	Unicode 相关的错误
# UnicodeDecodeError	Unicode 解码时的错误
# UnicodeEncodeError	Unicode 编码时错误
# UnicodeTranslateError	Unicode 转换时错误
# Warning	警告的基类
# DeprecationWarning	关于被弃用的特征的警告
# FutureWarning	关于构造将来语义会有改变的警告
# OverflowWarning	旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning	关于特性将会被废弃的警告
# RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning	可疑的语法的警告
# UserWarning	用户代码生成的警告


# 你要基础，或者使用 raise 的时候，就是你的代码写得足够好了，你为了别人使用你的代码而写代码。
# 这个时候你就会多考虑 raise 的用法了。 为什么这么说？因为 raise 是你为别人犯错留下的证据，
# 或者是告诉别人你怎么犯错的。
# def no_negative(num):
#     if num < 0:
#         raise ValueError("I said no negative")
#     return num


# print(no_negative(-1))

print("================================================")
# try:
#     dddd = dddddd
# finally:
#     print("I know there is error, so what?")

print("================================================")

l = [1, 2, 3, 4]
try:
    l[3] = 4
except IndexError as e:
    print(e)
finally:
    print("reach finally")
# reach finally

print("================================================")

# 你已经见识了大部分的异常处理方法了。如果 else 是为了执行没有异常的状况，那么 finally 就是为了执行
# 不管有没有异常 的情况。 无论有报错还是没报错，finally 下面的代码都会运行。下面第一段代码是会报错的，第二段不会报错。

l = [1, 2, 3]
try:
    l[3] = 4
except IndexError as e:
    print(e)
finally:
    print("reach finally")
# list assignment index out of range
# reach finally


print("================================================")

l = [1, 2, 3, 4]
try:
    l[3] = 4
except IndexError as e:
    print(e)
else:
    print("no error, now in else")

# no error, now in else

print("================================================")

l = [1, 2, 3]
try:
    l[3] = 4
except IndexError as e:
    print(e)
else:
    print("no error, now in else")

# list assignment index out of range


print("================================================")
# 它不会同时处理字典的 KeyError 和列表的 IndexError，因为在程序顺序执行的时候，只要是报错了，
# 那么就会终止错误之后的代码，进入错误 回收 环节。
# 这个回收环节在上面的案例中也就是 except 的错误处理环节。
# 所以你就能发现，其实在你不改动上面代码的情况下，l 列表是没有 append(4) 的。
# 只有当字典正常的时候，列表的报错才会触发。
d = {"name": "f1", "age": 2}
l = [1, 2, 3]
try:
    v = d["gender"]
    l[3] = 4
except KeyError as e:
    print("key error for:", e)
    d["gender"] = "x"
except IndexError as e:
    print("index error for:", e)
    l.append(4)
print(d)
print(l)

# key error for: 'gender'
# {'name': 'f1', 'age': 2, 'gender': 'x'}
# [1, 2, 3]

print("================================================")

d = {"name": "f1", "age": 2}
l = [1, 2, 3]
try:
    v = d["gender"]
    l[3] = 4
except (KeyError, IndexError) as e:
    print("key or index error for:", e)
# key or index error for: 'gender'

print("================================================")
try:
    with open("no_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)
    with open("no_file.txt", "w") as f:
        f.write("I'm no_file.txt")
    print("new file 'no_file.txt' has been written")

# [Errno 2] No such file or directory: 'no_file.txt'
# new file 'no_file.txt' has been written


print("================================================")

with open("no_file.txt", "r") as f:
    print(f.read())

# Traceback (most recent call last):
#   File "/Users/wangjiahao/server/github/python-demo/com/remember/basic/try-except.py", line 6, in <module>
#     with open("no_file.txt", "r") as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'no_file.txt'
