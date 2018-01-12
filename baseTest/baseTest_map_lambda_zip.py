# zip 合并操作
a = [1, 2, 3]
b = [4, 5, 6]
list1 = list(zip(a, b))
print(list1)

for i, j in zip(a, b):
    print(i/2, j*2)

# 多个也是可以的
list2 = list(zip(a, a, b))
print(list2)

# lambda 和def函数类似,简单一点的方程可以用lambda
def fun1(x, y):
    return x+y

print(fun1(2, 3))

fun2 = lambda x, y: x+y
print(fun2(2, 3))

# map 将函数和对应的输入绑定
list3 = list(map(fun1, [1], [2]))
print(list3)
# 多个参数也是可以的，分开计算
list4 = list(map(lambda x, y: x+y, [1, 3], [2, 5]))
print(list4)


