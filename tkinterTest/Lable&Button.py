import tkinter as tk


window = tk.Tk()
window.title('my window')
# MD为什么是x而不是*
window.geometry('500x300')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=30, height=8)
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("想吃麻辣烫！")
    else:
        on_hit = False
        var.set('')
b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()

window.mainloop()