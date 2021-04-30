# 简单对话框，包括字符、整数和浮点数
import tkinter as tk
from tkinter import simpledialog


def input_str():
    r = simpledialog.askstring('字符录入', '请输入字符', initialvalue='hello world!')
    if r:
        print(r)
        label['text'] = '输入的是：' + r


def input_int():
    r = simpledialog.askinteger('整数录入', '请输入整数', initialvalue=100)
    if r:
        print(r)
        label['text'] = '输入的是：' + str(r)


def input_float():
    r = simpledialog.askfloat('浮点数录入', '请输入浮点数', initialvalue=1.01)
    if r:
        print(r)
        label['text'] = '输入的是：' + str(r)


root = tk.Tk()
root.title('对话框')
root.geometry('300x100+300+300')

label = tk.Label(root, text='输入对话框，包括字符、整数和浮点数', font='宋体 -14', pady=8)
label.pack()

frm = tk.Frame(root)
btn_str = tk.Button(frm, text='字符', width=6, command=input_str)
btn_str.pack(side=tk.LEFT)
btn_int = tk.Button(frm, text='整数', width=6, command=input_int)
btn_int.pack(side=tk.LEFT)
btn_int = tk.Button(frm, text='浮点数', width=6, command=input_float)
btn_int.pack(side=tk.LEFT)
frm.pack()

root.mainloop()