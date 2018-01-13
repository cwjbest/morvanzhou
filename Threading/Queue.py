# -*- coding:UTF-8 -*-
import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    # 将l放入Queue中以便将来取出，不能return
    q.put(l)


def multi_threading():
    # 线程不能用return返回结果，所以要用Queue来存储线程的计算结果
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 3, 3]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        # 将每个线程加入到线程组中
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__ == '__main__':
    multi_threading()