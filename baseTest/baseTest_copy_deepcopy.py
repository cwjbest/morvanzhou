import copy
a = [1, 2, 3]
b = a
print(id(a) == id(b))
# 两个id一毛一样，所以是同一块内存，改变一个，另一个也会改变
a[0] = 11
print(a, b)

# copy 两个id并不一样，所以是两块内存，互相不影响
c = copy.copy(a)
print(id(a) == id(c))
c[0] = 22
print(a, c)

# 特殊情况，copy.copy()，list嵌套的话，内层list仍然是同一块内存，这种叫浅copy
d = [1, 2, [3, 4]]
e = copy.copy(d)
print(id(d[2]) == id(e[2])) # 返回True

# 完全copy，deepcopy，全部不同内存
f = copy.deepcopy(d)
print(id(f[2]) == id(d[2])) # 返回False