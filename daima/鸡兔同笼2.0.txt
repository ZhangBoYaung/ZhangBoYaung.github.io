"""
张博洋的项目：鸡兔同笼;
"""

import tkinter as tk
main = tk.Tk()
main.state('zoomed')
def qingkong(*x):
    for xx in x:
        xx.kuang.delete(0,tk.END)
def cuozi(*x):
    for xx in x:
        xx.kuang.insert(0,shuoming[1])
class Suanji(object):
    def __init__(self,wenben='鸡有多少只',ji=True,tou=True):
        self.tou=tou
        self.ji=ji
        self.wenben=wenben
        tk.Label(main, text=self.wenben, font=('宋体', 20), bg='lightblue').pack()
        self.kuang = tk.Entry(main, font=('黑体', 15))
        self.kuang.pack()
    def du(self):
        shumu = int(self.kuang.get())
        return shumu
    def xiugai(self):
        self.kuang.delete(0,tk.END)
        list1 = ji_tu()
        if self.ji:
            self.kuang.insert(0,list1['ji'])
        else:
            self.kuang.insert(0,list1['tu'])
    def touhetui(self):
        list1 = tou_tui()
        self.kuang.delete(0,tk.END)
        if self.tou:
            self.kuang.insert(0,list1['tou'])
        else:
            self.kuang.insert(0,list1['tui'])

def baocuo():
    qingkong(JI,TU,Tou,Tui)
    cuozi(JI,TU,Tou,Tui)
def tou_tui():
    x = JI.du()
    y = TU.du()
    if 0 <= x == int(x) and 0 <= y == int(y):
        x=int(x)
        y=int(y)
    else:
        baocuo()
    list1 = {'tou':x+y,'tui':x*2+y*4}
    return list1
def ji_tu():
    x = Tou.du()
    y = Tui.du()
    tu = (y-2*x)/2
    ji = x -tu
    if int(tu)== tu >=0  and int(ji)==ji >= 0 :
        tu=int(tu)
        ji=int(ji)
    else:
        baocuo()
    list1 = {'ji':ji,'tu':tu}
    return list1
def jisuan():
    try:
        JI.xiugai()
        TU.xiugai()
    except:
        baocuo()

def suanji():
    try:
        Tou.touhetui()
        Tui.touhetui()
    except:
        baocuo()
main['background']='lightblue'
main.geometry('1600x800')
main.title('鸡兔同笼2.0')
main.iconbitmap('img/000.ico')
PI = tk.PhotoImage(file='img/000.png')
tupian = tk.Label(main,image=PI,bg='lightblue')
tupian.pack()
biaoti = tk.Label(main,text='鸡兔同笼',font=('楷体',40),bg='lightblue')
biaoti.pack()
wenzi1 = open('txt/text1.txt','r',encoding='utf-8')
shuoming = eval(wenzi1.read())
JI = Suanji()
TU = Suanji(wenben='兔有多少只',ji=False)
anniu = tk.Button(main,text='计算头和腿',command=suanji)
anniu.pack()
Tou = Suanji(wenben='头有多少颗')
Tui = Suanji(wenben='腿有多少条',tou=False)
anniu2 = tk.Button(main,text='计算鸡和兔',command=jisuan)
anniu2.pack()
xiaozi = tk.Label(main,text=shuoming[0],font=('宋体',15),bg='lightblue')
xiaozi.pack()
main.mainloop()