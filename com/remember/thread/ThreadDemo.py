import random
import time
from concurrent.futures.thread import ThreadPoolExecutor

# 创建线程池
pool = ThreadPoolExecutor(10)


def foo(name):
    time.sleep(random.randint(1, 10))
    print("hello {}".format(name))



if __name__ == '__main__':
    # 执行方法
    for i in range(1, 11):
        pool.submit(foo, "wangjiahao" + str(i))
