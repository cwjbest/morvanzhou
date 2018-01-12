# import time
# from time import time, localtime
from time import *

from baseTest import my_module

# 自己的模块,同目录下就可以

# 这种比较方便，可以直接使用模块
# print(time.localtime())
print(time())
print(localtime())

my_module.fun('Hello')