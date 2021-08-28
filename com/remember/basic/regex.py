import re

# @see https://mofanpy.com/tutorials/python-basic/interactive-python/regex/

# 特定标识	含义	范围
# \d	任何数字	[0-9]
# \D	不是数字的
# \s	任何空白字符	[ \t\n\r\f\v]
# \S	空白字符以外的
# \w	任何大小写字母,数字和 _	[a-zA-Z0-9_]
# \W	\w 以外的
# \b	匹配一个单词边界	比如 er\b 可以匹配 never 中的 er，但不能匹配 verb 中的 er
# \B	匹配非单词边界	比如 er\B 能匹配 verb 中的 er，但不能匹配 never 中的 er
# \\	强制匹配 \
# .	匹配任何字符 (除了 \n)
# ?	前面的模式可有可无
# *	重复零次或多次
# +	重复一次或多次
# {n,m}	重复 n 至 m 次
# {n}	重复 n 次
# +?	非贪婪，最小方式匹配 +
# *?	非贪婪，最小方式匹配 *
# ??	非贪婪，最小方式匹配 ?
# ^	匹配一行开头，在 re.M 下，每行开头都匹配
# $	匹配一行结尾，在 re.M 下，每行结尾都匹配
# \A	匹配最开始，在 re.M 下，也从文本最开始
# \B	匹配最结尾，在 re.M 下，也从文本最结尾

# 有时候我们 group 的信息太多了，括号写得太多，让人眼花缭乱怎么办？我们还能用一个名字来索引匹配好的字段，
# 然后用 group("索引") 的方式获取到对应的片段。注意，上面方案中的 findall 不提供名字索引的方法，
# 我们可以用 search 或者 finditer 来调用 group 方法。为了索引，我们需要在括号中写上 ?P<索引名> 这种模式。
string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
match = re.finditer(r"(?P<y>\d+?)-(?P<m>\d+?)-(?P<d>\d+?)\.jpg", string)
for file in match:
    print("matched string:", file.group(0),
          ", year:", file.group("y"),
          ", month:", file.group("m"),
          ", day:", file.group("d"))
# matched string: 2021-02-01.jpg , year: 2021 , month: 02 , day: 01
# matched string: 2021-02-02.jpg , year: 2021 , month: 02 , day: 02
# matched string: 2021-02-03.jpg , year: 2021 , month: 02 , day: 03


print("================================================")

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
match = re.findall(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
for file in match:
    print("year:", file[0], ", month:", file[1], ", day:", file[2])
# year: 2021 , month: 02 , day: 01
# year: 2021 , month: 02 , day: 02
# year: 2021 , month: 02 , day: 03

print("================================================")

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
match = re.finditer(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
for file in match:
    print("matched string:", file.group(0), ",year:", file.group(1), ", month:", file.group(2), ", day:", file.group(3))
# matched string: 2021-02-01.jpg ,year: 2021 , month: 02 , day: 01
# matched string: 2021-02-02.jpg ,year: 2021 , month: 02 , day: 02
# matched string: 2021-02-03.jpg ,year: 2021 , month: 02 , day: 03

print("================================================")

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
print("without ():", re.findall(r"[\w-]+?\.jpg", string))
print("with ():", re.findall(r"([\w-]+?)\.jpg", string))
# without (): ['2021-02-01.jpg', '2021-02-02.jpg', '2021-02-03.jpg']
# with (): ['2021-02-01', '2021-02-02', '2021-02-03']

print("================================================")

found = []
for i in re.finditer(r"[\w-]+?\.jpg", "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"):
    found.append(re.sub(r".jpg", "", i.group()))
print(found)

# ['2021-02-01', '2021-02-02', '2021-02-03']

print("================================================")

print("search:", re.search(r"run", "I run to you"))
print("match:", re.match(r"run", "I run to you"))
print("findall:", re.findall(r"r[ua]n", "I run to you. you ran to him"))

for i in re.finditer(r"r[ua]n", "I run to you. you ran to him"):
    print("finditer:", i)

print("split:", re.split(r"r[ua]n", "I run to you. you ran to him"))
print("sub:", re.sub(r"r[ua]n", "jump", "I run to you. you ran to him"))
print("subn:", re.subn(r"r[ua]n", "jump", "I run to you. you ran to him"))

print("================================================")

# 功能	说明	举例
# re.search()	扫描查找整个字符串，找到第一个模式匹配的	re.search(rrun, I run to you) > 'run'
# re.match()	从字符的最开头匹配，找到第一个模式匹配的即使用 re.M 多行匹配，也是从最最开头开始匹配	re.match(rrun, I run to you) > None
# re.findall()	返回一个不重复的 pattern 的匹配列表	re.findall(rr[ua]n, I run to you. you ran to him) > ['run', 'ran']
# re.finditer()	和 findall 一样，只是用迭代器的方式使用	for item in re.finditer(rr[ua]n, I run to you. you ran to him):
# re.split()	用正则分开字符串	re.split(rr[ua]n, I run to you. you ran to him) > ['I ', ' to you. you ', ' to him']
# re.sub()	用正则替换字符	re.sub(rr[ua]n, jump, I run to you. you ran to him) > 'I jump to you. you jump to him'
# re.subn()	和 sub 一样，额外返回一个替代次数	re.subn(rr[ua]n, jump, I run to you. you ran to him) > ('I jump to you. you jump to him', 2)


print("================================================")
print(re.search(r"[\u4e00-\u9fa5！？。，￥【】「」]+", "我爱莫烦。莫烦棒！"))
# <re.Match object; span=(0, 9), match='我爱莫烦。莫烦棒！'>


print("================================================")

print(re.search(r"[\u4e00-\u9fa5]+", "我爱莫烦python"))
# <re.Match object; span=(0, 4), match='我爱莫烦'>

print("================================================")

print("中".encode("unicode-escape"))
# b'\\u4e2d'


print("================================================")

# 中文情况下
print(re.search(r"不?爱", "我爱你"))
print(re.search(r"不?爱", "我不爱你"))
print(re.search(r"不.*?爱", "我不是很爱你"))

# <re.Match object; span=(1, 2), match='爱'>
# <re.Match object; span=(1, 3), match='不爱'>
# <re.Match object; span=(1, 5), match='不是很爱'>
print("================================================")

#  \d{8} 就是用来表示任意的数字，重复 8 遍。
print(re.search(r"138\d{8}", "13812345678"))
print(re.search(r"138\d{8}", "138123456780000"))
# <re.Match object; span=(0, 11), match='13812345678'>
# <re.Match object; span=(0, 11), match='13812345678'>

print("================================================")

# 满足多个字符的不同匹配，比如我想同时找到 find 和 found。我该怎么办呢？

print(re.search(r"f(ou|i)nd", "I find you"))
print(re.search(r"f(ou|i)nd", "I found you"))

# <re.Match object; span=(2, 6), match='find'>
# <re.Match object; span=(2, 7), match='found'>

print("================================================")

# 在 run 与 ran 之间，其实它们的差别就只是中间这个字母，我们还能使用 [au] 来简化一下。
# 让它同时接受中间字母是 a 或者 u 的情况
print(re.search(r"r[au]n", "I run to you"))
# <re.Match object; span=(2, 5), match='run'>


print("================================================")

print(re.search(r"ran|run", "I run to you"))
# <re.Match object; span=(2, 5), match='run'>
# 这个 | 就代表或者的意思。

print("================================================")

print(re.search(r"ran", "I run to you"))
print(re.search(r"run", "I run to you"))

# None
# <re.Match object; span=(2, 5), match='run'>

print("================================================")

match = re.search(r"run", "I run to you")
print(match)
print(match.group())

# <re.Match object; span=(2, 5), match='run'>
# run
# ？因为正则表达式很多时候都要包含\，r 代表原生字符串， 使用 r 开头的字符串是为了不让你混淆 pattern 字符串中到底要写几个 \，
# 你只要当成一个规则来记住在写 pattern 的时候，都写上一个 r 在前面就好了。
#  .group() 能取出来里面找到的字符

print("================================================")

matched = re.search(r"\w+?@\w+?\.com", "1332661444@qq.com")
print("1332661444@qq.com:", matched)
matched = re.search(r"\w+?@\w+?\.com", "the email is wangjiahao@qq.com")
print("the email is wangjiahao@qq.com:", matched)

# 1332661444@qq.com: <re.Match object; span=(0, 17), match='1332661444@qq.com'>
# the email is wangjiahao@qq.com: <re.Match object; span=(13, 30), match='wangjiahao@qq.com'>
# span=(13,30) 代表匹配到的位置

print("================================================")

ptn = re.compile(r"\w+?@\w+?\.com")
matched = ptn.search("1332661444@qq.com")
print("1332661444@qq.com is a valid email:", matched)
matched = ptn.search("wangjiahao@qq+com")
print("wangjiahao@qq+com is a valid email:", matched)

# 1332661444@qq.com is a valid email: <re.Match object; span=(0, 17), match='1332661444@qq.com'>
# wangjiahao@qq+com is a valid email: None


print("================================================")

pattern1 = "file"
pattern2 = "files"
string = "the file is in the folder"
print("file in string", pattern1 in string)
print("files in string", pattern2 in string)
# file in string True
# files in string False

print("================================================")
