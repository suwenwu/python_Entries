# coding=utf-8
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random
import threading
import itertools
import time

root = Tk()
root.title("抽奖小程序")
root.geometry('700x545+400+200')
root.resizable(False, False)


listold = Listbox(root, width=30, height=15, font="微软雅黑 15")
listold.grid(row=1, column=0, rowspan=7, columnspan=2, padx=30, sticky='ns')


def closewindow():
    root.flag = False
    time.sleep(0.1)
    root.destroy()
    print("退出")


root.protocol('WM_DELETE_WINDOW', closewindow)


def onclick():
    global list_var
    global listnew
    file_name = filedialog.askopenfilename(
        title="打开我的文件", initialdir="/Users/skyelam/Desktop/学习/python code",
        filetypes=[("文本文档", ".txt"), ('All Files', '*')])
    print(f"打开文件为{file_name}")
    import sys
    list_var = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            list_var.append(list(line.strip('\n').split(',')))
    num = len(list_var)
    print(list_var)
    listnew = Listbox(root, listvariable=list_var, font="微软雅黑 15", width=30, height=15, selectmode=EXTENDED)
    for i in range(len(list_var)):
        listnew.insert("end", list_var[i])
    listnew.grid(row=1, column=0, rowspan=7, columnspan=2, padx=30, sticky='e')
    showname['text'] = f"本次参加抽奖{len(list_var)}人 "
    print(showname['text'])
    f.close()


def deletename():
    sel = listnew.curselection()
    for index in sel[::-1]:
        listnew.delete(index)
        del list_var[index]
    listnew.grid(row=1, column=0, rowspan=7, columnspan=2, padx=30, sticky='e')
    showname['text'] = f"本次参加抽奖{len(list_var)}人 "
    print(showname['text'])
    print(list_var)


root.flag = False


def switch():
    root.flag = True
    # 随机打乱学生名单
    t = list_var[:]
    random.shuffle(t)
    t = itertools.cycle(t)
    while root.flag:
        # 滚动显示
        lb6['text'] = lb4['text']
        lb4['text'] = lb2['text']
        lb2['text'] = lb1['text']
        lb1['text'] = lb3['text']
        lb3['text'] = lb5['text']
        lb5['text'] = lb7['text']
        lb7['text'] = next(t)
        # 数字可以修改，控制滚动速度
        time.sleep(0.03)

def btnstartclick():
    global luckyguy
    award = val.get()
    luckyguy = var_range.get()
    print(f"{award}抽奖人数为：{luckyguy}人")
    luckyguy = int(luckyguy)
    if luckyguy == 1:
        lb1['fg'] = 'red'
        lb2['fg'] = 'black'
        lb3['fg'] = 'black'
        lb4['fg'] = 'black'
        lb5['fg'] = 'black'
    if luckyguy == 2:
        lb1['fg'] = 'red'
        lb2['fg'] = 'red'
        lb3['fg'] = 'black'
        lb4['fg'] = 'black'
        lb5['fg'] = 'black'
    if luckyguy == 3:
        lb1['fg'] = 'red'
        lb2['fg'] = 'red'
        lb3['fg'] = 'red'
        lb4['fg'] = 'black'
        lb5['fg'] = 'black'
    if luckyguy == 4:
        lb1['fg'] = 'red'
        lb2['fg'] = 'red'
        lb3['fg'] = 'red'
        lb4['fg'] = 'red'
        lb5['fg'] = 'black'
    if luckyguy == 5:
        lb1['fg'] = 'red'
        lb2['fg'] = 'red'
        lb3['fg'] = 'red'
        lb4['fg'] = 'red'
        lb5['fg'] = 'red'
    # 每次单击“开始”按钮启动新线程
    t = threading.Thread(target=switch)
    t.start()
    btnstart['state'] = 'disabled'
    btnstop['state'] = 'normal'


def btnstopclick():
    # 单击“停”按钮结束滚动显示
    root.flag = False
    time.sleep(0.3)
    award = val.get()
    if luckyguy == 1:
        messagebox.showinfo("中奖名单", award + '中奖名单：' + '\n' + lb1['text'])
        print(f"{award}中奖名单:{lb1['text']}")
    if luckyguy == 2:
        messagebox.showinfo("中奖名单", award + '中奖名单：' + '\n'
                            + lb1['text']
                            + ',' + lb2['text'])
        print(f"{award}中奖名单:{lb1['text']},{lb2['text']}")
    if luckyguy == 3:
        messagebox.showinfo("中奖名单", award + '中奖名单：' + '\n'
                            + lb1['text']
                            + ',' + lb2['text']
                            + ',' + lb3['text'])
        print(f"{award}中奖名单:{lb1['text']},{lb2['text']},{lb3['text']}")
    if luckyguy == 4:
        messagebox.showinfo("中奖名单", award + '中奖名单：' + '\n'
                            + lb1['text']
                            + ',' + lb2['text']
                            + ',' + lb3['text']
                            + ',' + lb4['text'])
        print(f"{award}中奖名单:{lb1['text']},{lb2['text']},{lb3['text']},{lb4['text']}")
    if luckyguy == 5:
        messagebox.showinfo("中奖名单", award + '中奖名单：' + '\n'
                            + lb1['text']
                            + ',' + lb2['text']
                            + ',' + lb3['text']
                            + ',' + lb4['text']
                            + ',' + lb5['text'])
        print(f"{award}中奖名单:{lb1['text']},{lb2['text']},{lb3['text']},{lb4['text']},{lb5['text']}")
    btnstart['state'] = 'normal'
    btnstop['state'] = 'disabled'


Label(root, text='选择抽奖名单(txt)', font="微软雅黑 13").grid(row=0, column=0, sticky='e')
Button(root, text="浏览", command=onclick, font="微软雅黑 13").grid(row=0, column=1, sticky='ns')
showname = Label(root, text='', font="微软雅黑 13", fg='blue')
showname.grid(row=8, column=0, columnspan=2, padx=30, sticky='ns')
op_list = ["特等奖", "一等奖", "二等奖", "三等奖"]
val = StringVar()
val.set(op_list[0])
# 注意，传入的列表前需要加一个*号，这是表示不定参的传递，
# 两个*则是表示字典类型的不定参传递
OptionMenu(root, val, *op_list).grid(row=9, column=0, sticky='w', padx=35)
Label(root, text="中奖人数：").grid(row=9, column=0, sticky='e')
var_range = StringVar()
var_range.set(0)
Spinbox(root, textvariable=var_range, font="微软雅黑 10", width=6, from_=1, to=5).grid(row=9, column=1, sticky='w')
lb6 = Label(root, text='', font="微软雅黑 15")
lb6.grid(row=1, column=6, columnspan=3, sticky='ns')
lb4 = Label(root, text='', font="微软雅黑 15")
lb4.grid(row=2, column=6, columnspan=3, sticky='ns')
lb2 = Label(root, text='', font="微软雅黑 15")
lb2.grid(row=3, column=6, columnspan=3, sticky='ns')
lb1 = Label(root, text='', font="微软雅黑 15", fg='red')
lb1.grid(row=4, column=6, columnspan=3, sticky='ns')
lb3 = Label(root, text='', font="微软雅黑 15")
lb3.grid(row=5, column=6, columnspan=3, sticky='ns')
lb5 = Label(root, text='', font="微软雅黑 15")
lb5.grid(row=6, column=6, columnspan=3, sticky='ns')
lb7 = Label(root, text='', font="微软雅黑 15")
lb7.grid(row=7, column=6, columnspan=3, sticky='ns')
btnstart = Button(root, text='开始', command=btnstartclick)
btndelete = Button(root, text="删除", command=deletename)
btndelete.grid(row=7, column=2, sticky='s')
btnstart.grid(row=9, column=2)
Label(root, text="Lucky guy？", font=('Bradley Hand', '20')).grid(row=0, column=6, columnspan=3, sticky='ns')
btnstop = Button(root, text='停', command=btnstopclick)
btnstop['state'] = 'disabled'
btnstop.grid(row=9, column=7, sticky='e')
Button(root, text="退出", command=closewindow).grid(row=9, column=9, sticky='e')
root.mainloop()