import queue
import threading

import time


# 生产者
class Producter(threading.Thread):
    def __init__(self, name):
        super(Producter, self).__init__()
        self.name = "producter %s" % str(name)

    def run(self):
        things = ['A', 'B', 'C', 'D', 'E', 'F']
        while True:
            print(self.name)


# 消费者
class Consumer(threading.Thread):
    def __init__(self, name):
        super(Consumer, self).__init__()
        self.name = "Consumer:" + str(name)

    def run(self):
        while True:
            print(self.name)


if __name__ == '__main__':
    all_productions = queue.Queue(-1)

    producter_num = 0
    consumer_num = 0
    while True:
        producter_num += 1
        Producter(producter_num)
        time.sleep(1)
        if producter_num > 50:
            break

    while True:
        consumer_num += 1
        Consumer(consumer_num)
        time.sleep(1)
        if consumer_num > 50:
            break

    # 阻塞，直到生产者生产的数据被消耗完
    all_productions.join()