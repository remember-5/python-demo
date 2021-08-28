# @see https://mofanpy.com/tutorials/python-basic/interactive-python/generator/


class NeedReturn:
    def __init__(self,init_value=0):
        self.tmp = init_value
        self.item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.item == self.tmp:
                self.tmp *= 2
                return self.item
            self.item += 1
            if self.item == 300:
                raise StopIteration


for i in NeedReturn(10):
    print(i)







print("================================================")

def need_return(init_value):
    tmp = init_value
    for item in range(300):
        if item == tmp:
            tmp *= 2
            yield item


for i in need_return(10):
    print(i)

# 10
# 20
# 40
# 80
# 160

print("================================================")


def need_return():
    tmp = 2
    for item in range(300):
        if item == tmp:
            tmp *= item
            yield item


for i in need_return():
    print(i)
# 4
# 16
# 256
# 2
print("================================================")


def need_return():
    for item in range(5):
        if item % 2 == 0:
            print("我要扔出去一个 item=%d 了" % item)
            yield item  # 这里就会返回给下面的 for 循环
            print("我又回到里面了")


for i in need_return():
    print("我在外面接到了一个 item=%d\n" % i)

print("================================================")

items = []  # 假设这里在记录一个很大的列表
for item in range(5):
    if item % 2 == 0:
        items.append(item)

for i in items:
    print(i)

print("================================================")
