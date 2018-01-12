def function(a, b):
    c = a + b
    print(c)

function(1, 2)
function(a=2, b=5)
# 可以指明变量值

def sale_car(price, color='red', brand='BMW'):
    print('price:', price,
          'color:', color,
          'brand:', brand)
sale_car(100)
# 默认的参数值，很方便，但是必须顺序写在一起，想改变，调用时直接赋新值即可

# global全局变量
APPLE = 100
a = None
def fun1():
    global a
    a = 20
    return a + APPLE

print('a pass =', a)
print(fun1())
print('a now =', a)

# 安装模块可以用pip



