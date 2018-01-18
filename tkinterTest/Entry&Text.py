# coding:UTF-8
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

# show='*'代表输入密码全为*
e = tk.Entry(window, show=None)
e.pack()

t = tk.Text(window, height=2)


def insert_point():
    var = e.get()
    t.insert('insert', var)
    # 'insert'代表光标处插入


def insert_end():
    var = e.get()
    t.insert('end', var)
    # 'end'代表尾部插入
    # t.insert(1.1, var) 第一行第一位插入


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
b2.pack()
t.pack()

window.mainloop()