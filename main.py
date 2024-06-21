import tkinter
import time
tk = tkinter.Tk()
def cl():
    tk.destroy()
mainlist = list(range(0,6))
for i in mainlist:
    mainlist[i] = tkinter.Toplevel()
    mainlist[i].title('你好同学')
    mainlist[i].config(bg='blue')
    mainlist[i].geometry('800x600-'+str(50*int(i))+"-"+str(50*int(i)))
    text = tkinter.Label(mainlist[i],
        text='你好同学\n我是你们亲爱的张博洋学长\n技术交流可以找我：\nyouhulu2021@outlook.com', font=('黑体', 40), padx=50, pady=450, bg='blue', fg='red')
    text.pack()
for i in range(0,6):
    mainlist[i].after(5000,cl)
    mainlist[i].mainloop()
tk.mainloop()


