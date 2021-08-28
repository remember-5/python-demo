# @see https://mofanpy.com/tutorials/python-basic/interactive-python/string/


# 方式	意思
# strip	去除两端的空白符
# replace	替换字符
# lower	全部做小写处理
# upper	全部做大写处理
# title	仅开头的字母大写
# split	按要求分割
# join	按要求合并
# startswith	判断是否为某字段开头
# endswith	判断是否为某字段结尾

# 剔除前后空白
print("  我不想要前后的空白，但是  中间\n的可以有\n  ".strip())
# 我不想要前后的空白，但是  中间
# 的可以有


# 替换文字
print("帮我替换掉莫烦".replace("莫烦", "沫凡"))
# 帮我替换掉沫凡

# 文字的大小写处理
print("How ABOUT lower CaSe?".lower())
print("And upper CaSe?".upper())
print("do tiTle For me".title())

# how about lower case?
# AND UPPER CASE?
# Do Title For Me

# 拆散你，重组你
print("你|帮|我|拆分|一下|这句话".split("|"))
print("|".join(["你","帮", "我", "重组", "一下", "这句话"]))

# ['你', '帮', '我', '拆分', '一下', '这句话']
# 你|帮|我|重组|一下|这句话

print("我在街头看到你".startswith("我在"))
print("我在街头看到你".startswith("街头"))
print("我在巷尾看到你".endswith("看到你"))
print("我在巷尾看到你".endswith("巷尾"))
# True
# False
# True
# False

print("================================================")

score = 2.1234
print(f"You scored {score:.2%}")
print(f"You scored {score:.3f}")
print(f"You scored {12:5d}")

# You scored 212.34%
# You scored 2.123
# You scored    12

print("================================================")
name = "学习python"
age = 18
height = 1.8
print(f"我的名字是 {name} !我 {age} 岁了，我 {height} 米高~")
# 我的名字是 学习python !我 18 岁了，我 1.8 米高~


print(f"我 {age} 岁了，明年我就{age + 1}岁了~")
# 我 18 岁了，明年我就19岁了~

print("================================================")
# :,	每 3 个 0 就用逗号隔开，比如 1,000
# :b	该数字的二进制
# :d	整数型
# :f	小数模式
# :%	百分比模式


txt = "You scored {:%}"
print(txt.format(2.1234))

txt = "You scored {:.2%}"
print(txt.format(2.1234))

# You scored 212.340000%
# You scored 212.34%

print("================================================")

print("我 {:.3f} 米高".format(1.12345))
print("我 {ht:.1f} 米高".format(ht=1.12345))
print("我 {:3d} 米高".format(1))
print("我 {:3d} 米高".format(21))
# 我 1.123 米高
# 我 1.1 米高
# 我   1 米高
# 我  21 米高
print("================================================")

name = "学习python"
age = 18
height = 1.8
print("我的名字是 {nm} !我 {age} 岁了，我 {ht} 米高~我是{nm}".format(nm=name, age=age, ht=height))
# 我的名字是 学习python !我 18 岁了，我 1.8 米高~我是莫烦Python
print("================================================")

name = "学习python"
age = 18
height = 1.8
print("我的名字是 {0} !我 {1} 岁了，我 {2} 米高~我是{0}".format(name, age, height))
# 我的名字是 学习python !我 18 岁了，我 1.8 米高~我是学习python
print("================================================")

name = "学习python"
age = 18
height = 1.8
print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name, age, height))
print("我的名字是 {} !我 {} 岁了，我 {} 米高~".format(name, age, height))

# 我的名字是 学习python !我 18 岁了，我 1.800000 米高~
# 我的名字是 学习python !我 18 岁了，我 1.8 米高~

print("================================================")

print("%f" % (1 / 3))  # 后面不限制
print("%.2f" % (1 / 3))  # 后面限制 2 个位置
print("%4d" % (1 / 3))  # 前面补全最大 4 个位置
print("%5d" % 12)  # 前面补全最大 5 个位置

# 0.333333
# 0.33
#    0
#    12

print("================================================")

print("%f" % (1 / 3))
print("%.2f" % (1 / 3))

# 0.333333
# 0.33

print("================================================")

name = "学习python"
age = 18
height = 1.8
print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name, age, height))

# 我的名字是 学习python !我 18 岁了，我 1.800000 米高~
print("================================================")

name = "学习python"
age = 18
gender = "男"
print("我的名字是 %(nm)s !我 %(age)d 岁了，我是 %(gd)s 的~" % {"nm": name, "age": age, "gd": gender})

# 我的名字是 学习python !我 18 岁了，我是 男 的~
print("================================================")

name = "学习python"
age = 18
gender = "男"
print("我的名字是" + name + "！我" + str(age) + "岁了，我是" + gender + "的~")
print("我的名字是 %s !我 %d 岁了，我是 %s 的~" % (name, age, gender))

# 我的名字是学习python！我18岁了，我是男的~
# 我的名字是 学习python !我 18 岁了，我是 男 的~
print("================================================")

name = "学习python"
print("我的名字是" + name + "！")
print("我的名字是%s!" % name)

# 我的名字是学习python！
# 我的名字是学习python!
print("================================================")
