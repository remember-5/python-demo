from concurrent.futures.thread import ThreadPoolExecutor

pool = ThreadPoolExecutor(10)


def foo(name):
    print("hello {}".format(name))


if __name__ == '__main__':
    pool.submit(foo,"wangjiahao1")
    pool.submit(foo,"wangjiahao2")
    pool.submit(foo,"wangjiahao3")
    pool.submit(foo,"wangjiahao4")
    pool.submit(foo,"wangjiahao5")
    pool.submit(foo,"wangjiahao6")
