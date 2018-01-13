import threading
from queue import Queue
import copy
import time


def job(l, q):
    res = sum(l)
    q.put(res)


def multi_threading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]

    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal time:', time.time() - s_t)
    s_t = time.time()
    multi_threading(l)
    print('multi_threading time:', time.time() - s_t)
