# coding:UTF-8
import multiprocessing as mp
import time


def job(v, num, l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num # 获得共享变量值
        print(v.value, end=" ")
    l.release()


def multi_process():
    l = mp.Lock() # 定义进程锁
    v = mp.Value('i', 0) # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1, l)) # 作为参数将锁传入
    p2 = mp.Process(target=job, args=(v, 3, l)) # 累加不同的值，看是否会抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multi_process()