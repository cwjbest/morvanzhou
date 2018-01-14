import multiprocessing as mp


def job(x):
    return x*x


def multi_process():
    # 默认是cpu的核数，可以自己控制
    pool = mp.Pool(processes=2)
    # map是用来取回函数的返回值,可以放入很多个参数，自动分配个多个核
    res = pool.map(job, range(10))
    print(res)

    # 单个核计算，用apply_async,用get取回
    res = pool.apply_async(job, (2, ))
    print(res.get())

    # 要计算多个的话可以迭代达到map的效果
    multi_res = [pool.apply_async(job, (i, )) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multi_process()