# coding:utf-8

from Tkinter import *


root = Tk()
# 窗口的大小及位置
root.geometry('500x500+700+400')

# 去除边框
# root.overrideredirect(1)
# title
root.wm_title('Python在线编辑器')


# Lable
title = Label(root, text='Python编译器', foreground='blue', height=3)
title.pack()


text = Text(root, background='black', foreground='blue', relief='groove')
text.pack()


text = Entry(root, background='black')
text.pack()

b = Button(root, text='submit', foreground='blue', height=2)
b.bind('<Button-1>', 'cal')
b.pack()

root.mainloop()
