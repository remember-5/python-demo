import queue
import random
import threading
import time

# 生产者线程数
PRODUCT_WORKER_THREAD_NUM = 10
# 消费者线程书
CONSUMER_WORKER_THREAD_NUM = 5


# 生产者类
class Producter(threading.Thread):
    def __init__(self, name):
        super(Producter, self).__init__()
        self.name = "Producter:" + str(name)

    def run(self):
        things = ['A', 'B', 'C', 'D', 'E', 'F']
        for _ in range(CONSUMER_WORKER_THREAD_NUM):
            production = random.choice(things)
            print(self.name + " producted--->" + production)
            production = production + " from " + self.name
            all_productions.put(production)  # 将生产的数据放入队列
            time.sleep(1)
        time.sleep(5)


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name):
        super(Consumer, self).__init__()
        self.name = "Consumer:" + str(name)

    def run(self):
        for _ in range(PRODUCT_WORKER_THREAD_NUM):
            thing = all_productions.get()  # 拿出已经生产好的数据
            print(self.name + " is using--->" + thing)
            time.sleep(2)
            all_productions.task_done()  # 告诉队列有关这个数据的任务已经完成
        time.sleep(5)


if __name__ == "__main__":
    all_productions = queue.Queue()

    # 启动10个生产者线程生产
    product_threads = []
    for i in range(PRODUCT_WORKER_THREAD_NUM):
        p = Producter(i)
        p.start()
        product_threads.append(p)

    # 启动5个消费者线程消费
    consumer_threads = []
    for i in range(CONSUMER_WORKER_THREAD_NUM):
        c = Consumer(i)
        c.start()
        consumer_threads.append(c)

    # 阻塞，直到生产者生产的数据被消耗完
    all_productions.join()

    # 等待生产者线程结束
    for p in product_threads:
        p.join()
    # 等待消费者线程结束
    for c in consumer_threads:
        c.join()

    print('阔以了....')
