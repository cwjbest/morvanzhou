# -*- coding:utf-8 -*-
import threading
import time


def thread_job():
    print("This is added Thread, number is %s" % threading.current_thread())


def t1_job():
    print("T1 start\n")
    time.sleep(3)
    print("T1 finish\n")


def t2_job():
    print("T2 start\n")
    print("T2 finish\n")


def main():
    # # 当前线程数
    # print(threading.active_count())
    # # 线程信息
    # print(threading.enumerate())
    # # 程序运行时的线程
    # print(threading.current_thread())
    # # 添加thread,指明要做什么任务，target
    # added_thread = threading.Thread(target=thread_job())
    # added_thread.start()

    t1_thread = threading.Thread(target=t1_job, name="T1")
    t2_thread = threading.Thread(target=t2_job, name="T2")
    t1_thread.start()
    t2_thread.start()
    # t1_thread.join()
    print("all done")


if __name__ == '__main__':
    main()
