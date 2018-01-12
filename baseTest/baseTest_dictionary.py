d1 = {'apple': 1, 'pear': 2, 'orange': 3}
d2 = {1: 'a', 2: 'b', 'c': 'd'}

print(d1['apple'])

# 删除，感觉python各种简写
del d2[1]
print(d2)

d2[1] = 'apple'
print(d2)

# 字典可以嵌套，可以是函数，可以是各种东西
