# coding:UTF-8

# 虽然可以用global来定义全局变量，但是进程之间共享数据，用global不能保证及时性，所以要用到共享内存

import multiprocessing as mp

# 定义共享变量,预先定义形式
value = mp.Value('i', 1)

# 数组的话只能是一维
array = mp.Array('i', [1, 2, 3])

