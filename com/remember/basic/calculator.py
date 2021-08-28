# @see https://mofanpy.com/tutorials/python-basic/interactive-python/useless-calculator/
# 嗯，计算器，那就该有计算器该有的样子。我先定位一下这个产品出来以后能怎么用？
#
# 计算两个数的加减乘除等一些常用方法
# 一次性计算一批数据的运算结果
# 好，就这么简单两项，能为我的生活创造出很多价值了，特别是第二个功能，让我能一次性处理一批数据。这个需求很常见，比如我在 excel 里面有一批数据， 都要处理，那么批处理就十分有用了。


class Calculator:
    def subtract(self, a, b):
        return a - b

    def batch_subtract(self, a_list, b_list):
        res_list = []
        for i in range(len(a_list)):
            res_list.append(self.subtract(a_list[i], b_list[i]))
        return res_list


c = Calculator()
print(c.subtract(2, 1))
print(c.batch_subtract([3, 2, 1], [2, 3, 4]))

print("================================================")


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # 处理异常
        if b == 0:
            print("b cannot be 0")
        else:
            return a / b


# 生产一个实例
c = Calculator()
print(c.add(1, 2))
print(c.divide(1, 2))
c.divide(1, 0)
