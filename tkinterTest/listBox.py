# coding:UTF-8
import tkinter as tk

window = tk.Tk()
window.title('list box')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)# 获取当前选中的文本
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))# 为变量设置值

lb = tk.Listbox(window, listvariable=var2)# 将var2的值赋给Listbox

# 创建一个list并将值循环添加到Listbox控件中
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)

lb.pack()

window.mainloop()