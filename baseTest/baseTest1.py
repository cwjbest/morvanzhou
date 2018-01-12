print('hello')
print('I\' m a teacher ')
print('apple' + str(4))
print(1 + 2)
print(int('1') + 2)
print(float('1.2') + 2)
print(2**2)
print(9/4)
print(9//4)
# 这个才是取整

apple = 1
print(apple)

a, b, c = 1, 2, 3
print(a, b, c)

condition = 1
while condition < 10:
    print(condition)
    condition += 1

# while True:
#    print("hello")
# python减少了（）的使用，但是对结构要求更加严谨，比如空格

example_list = [1, 2, 3, 4, 5, 6]
for i in example_list:
    print(i)
print('end')

# range函数，从start到stop-1，步长可以省略默认1
for i in range(1, 10, 2):
    print(i)
print('end')

x = 2
y = 3
z = 0
# python可以识别连续比较，不用再&& ||了
if x < y < z:
    print('x is less than y')
else:
    print('x is not less than y')

# 注意elif
if x > 2:
    print('x > 2')
elif x < 2:
    print('x < 2')
else:
    print('x = 2')