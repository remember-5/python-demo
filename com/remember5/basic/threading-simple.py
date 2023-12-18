# @see https://mofanpy.com/tutorials/python-basic/threading/thread/
import threading

print(threading.active_count())
print(threading.enumerate())
# 2

def thread_job():
    print('This is a thread of %s' % threading.current_thread())


def main():
    thread = threading.Thread(target=thread_job, )  # 定义线程
    thread.start()  # 让线程开始工作


if __name__ == '__main__':
    main()