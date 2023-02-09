import tkinter as tk
from tkinter import messagebox

# 生成tk窗口，设置居中显示，并且设置无法拉伸
root = tk.Tk()
root.title("学生管理系统登录页面")
width = 300
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int(screen_width / 2 - width / 2)
y = int(screen_height / 2 - height / 2)
size = '{}x{}+{}+{}'.format(width, height, x, y)
root.geometry(size)
root.resizable(False, False)

# 进行登录页面编辑
tk.Label(root, text="用户名:", font=('微软雅黑', 20, 'bold'),
         anchor='w', pady=15, padx=10).grid(row=0, sticky='w')
tk.Label(root, text="密  码:", font=('微软雅黑', 20, 'bold'),
         anchor='w', pady=15, padx=10).grid(row=1, sticky='w')
# 设置账号输入框
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1)
# 设置密码输入框
psw_entry = tk.Entry(root, show='*')
psw_entry.grid(row=1, column=1)


def login():
    messagebox.showinfo(title='登录成功', message="successful")
    print("欢迎登录学生管理系统" + user_entry.get())


def logout():
    result = messagebox.askyesno("提示", message="你确定要关闭窗口吗")
    if result:
        root.quit()


tk.Button(root, text='登录', width=10, command=login
          ).grid(row=3, column=0, columnspan=2, sticky='w', padx=10, pady=5)
tk.Button(root, text='退出', width=10, command=logout
          ).grid(row=3, column=1, columnspan=2, sticky='e', padx=10, pady=5)
root.mainloop()
