import tkinter as tt
from tkinter import *
from  tkinter import Tk, Label, Button,Entry, StringVar

win = tt.Tk()# 创建窗体对象
# win.title('来自我的表白')#标题
# win.geometry('350x200+430+350')
# label = tt.Label(win,text='能做我女朋友吗？',font="微软雅黑",fg='#666',bg='red')
# label.pack()
# def mClick():
#     label = tt.Label(win,text='爱你哦！',font="宋体",fg='#888888')
#     label.place(x=70,y=100)
# def mClick1():
#     label = tt.Label(win, text='再考虑一下不！我是认真的呢', font="宋体", fg='#888888')
#     label.place(x=70,y=100)
# btn = Button(win,text='可以',command=mClick)
# btn1 = Button(win,text='不可以',command=mClick1)
# btn.place(x=70,y=50)
# btn1.place(x=230,y=50)

win.title('程序验证')#标题
win.geometry('350x200+430+350')
txt1=StringVar()  # 声明为StringVar对象
txt2=StringVar()
label = Label(win, text="请输入密码!",  font=('宋体','16'))
label.pack()
def mClick():
    # L1 = Label(win, textvariable=txt2,font=('宋体', '16'))
    # L1.pack()
    str = txt1.get()
    # txt2.set(str)
    if  str == '123':
        L2 = Label(win, text='恭喜你输入正确',  font=('宋体','16'))
        L2.pack()
    else:
        L3 = Label(win, text='输入错误', font=('宋体', '16'))
        L3.pack()


txt1=Entry(win, textvariable=txt1, width=16, font=('宋体','16'))
txt1.pack()
btn=Button(win, text='确认', command=mClick)
btn.pack()
#成功了！
win.mainloop()# 循环事件

