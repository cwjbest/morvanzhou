a_tuple = (12, 2, 4, 65, 32)
another_tuple = 32, 4, 5, 7, 3
# 元组，加不加括号无所谓

# list和tuple其实差不多，tuple不能修改元素内容，list可以，一般用list就行了
a_list = [1, 2, 3, 4, 5]

for content in a_list:
    print(content)

# range(len(list))指明这个list的下标范围
for index in range(len(a_list)):
    print("index=", index, ", number in list =", a_list[index])

a_list.append(0)
print(a_list)

# insert 在某个位置插入，默认情况和append一样都在末尾
a_list.insert(1, 0)
print(a_list)

# remove就不同了，不是remove索引，而是第一个value
a_list.remove(0)
print(a_list)

# 最后一个值，可以用-1来索引
print(a_list[-1])

# 范围，0,1,2，并没有3哦
print(a_list[0:3])
print(a_list[3:])
print(a_list[:3])

# 4这个value的index是3
print(a_list.index(4))

# 3出现的次数
print(a_list.count(3))

# 默认从小到大排序，并且会覆盖原有list，反序的话reverse = True

a_list.sort()
print(a_list)

a_list.sort(reverse=True)
print(a_list)

# 多维list
multi_dim_a = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
print(multi_dim_a[0])