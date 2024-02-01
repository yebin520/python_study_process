from tkinter import *
def information_print():
    class_number = entry_class.get()
    student_name = entry_name.get()
    started_leavel = entry_level.get()
    text.insert(END, '{0}:{1}-{2},正在下载...'.format("第一名",entry_class.get(), entry_name.get()))
    print(class_number,started_leavel,student_name)

root = Tk()
# 标题
root.title('守护最好的坤坤')
# 界面的大小
root.geometry('560x550+400+200')
# 标签组件
# 输入班级，姓名
label1 = Label(root,text="请输入你的班级:",font=('楷体',20))
label2 = Label(root,text="请输入你的姓名:",font=('楷体',20))
label3 = Label(root,text="请输入起始关卡:",font=('楷体',20))
label4 = Label(root,text="TOP 10",bg = 'red',font=('楷体',25))
# 定位与布局
label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=3,column=0)
# 输入框组件
entry_class = Entry(root,font=('宋体',20))
entry_class.grid(row=0,column=1)

entry_name = Entry(root,font=('宋体',20))
entry_name.grid(row=1,column=1)

entry_level = Entry(root,font=('宋体',20))
entry_level.grid(row=2,column=1)
# 下载按钮
button1 = Button(root,text='开始游戏',font=('楷体',15),command=information_print)
button1.grid(row=5,column=0)
button2 = Button(root,text='结束游戏',font=('楷体',15))
button2.grid(row=5,column=1)
#排名框架
text = Listbox(root,font=('楷体',16),width=50,height=15)
text.grid(row=4,columnspan=2)

root.mainloop()

