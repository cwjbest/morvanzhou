class Calculator:
    # name = 'Good calculator'
    # price = '18'

# 类似构造器的一个东西，初始化参数,不同的是，不需要提前定义变量
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        result = x * y
        print(result)

    def divide(self, x, y):
        result = x / y
        print(result)

calculator = Calculator('cwj', 100)
print(calculator.name)
calculator.add(3, 4)
calculator.minus(4, 2)
calculator.times(3, 5)
calculator.divide(6, 3)


