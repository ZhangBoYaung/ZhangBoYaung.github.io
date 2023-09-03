"""
一个用来练习整数加减法口算的简单APP（闲的）
"""
import random
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

fuhao = ('+', '-')
make = 0
savefile = 0
score = 0
weight = 1
imp = 0
num = 0
t = 0
right = 0
ing = False
button2 = None
zheng = True
many = 0
many_right = 0

class exercise1(toga.App):

    def startup(self):

        def on_fu(widget):
            input1.value = -1

        def weifu(widget):
            global zheng
            zheng = False
            bt2.style.background_color = 'orange'
            del bt1.style.background_color

        def weizheng(widget):
            global zheng
            zheng = True
            bt1.style.background_color = 'orange'
            del bt2.style.background_color

        def start():
            global make

            if savefile == 0 :
                pass
            elif savefile == 1 :
                weight = imp
                if weight == 1:
                    make = 11
                elif weight == 2:
                    make = 21
                elif weight == 3:
                    make = 101
                elif weight == 4:
                    make = 501
                elif weight == 5:
                    make = 1001
                else:
                    pass
                out_label.text = '你想算几道题？'

        def next1():
            global t, right , ing

            if t!=num :
                input1.value = None
                a = random.randrange(make)
                b = random.randrange(make)
                xx = random.choice(fuhao)

                if zheng and a<b and xx=='-':
                    a,b = b,a

                if a==b and xx=='-':
                    xx = '+'
                out_label.text = f'第{t + 1}题\n{a}{xx}{b}=？'
                right = eval(f'{a}{xx}{b}')
                t += 1

            else:
                out_label.text = f'你一共算了{num}道题\n算对{score}道题\n分数：{int(score / num *100)}'
                ing = True

        def guiwei():
            global button2, make, savefile, score, weight, imp, num, t, right, ing
            make = 0
            savefile = 0
            score = 0
            weight = 1
            imp = 0
            num = 0
            t = 0
            right = 0
            ing = False
            input1.value = None
            big_label.text='口算练习'

        def anxia2(widget):
            guiwei()
            out_label.text = '''
请选择你的难度（输入序号）
1  简单
2  中等
3  较难
4  很难
5  非常难
        '''

        def button(widget):
            global many,many_right
            if input1.value != 0:
                global imp, savefile, num, score, make, weight, ing, t, right
                n = input1.value
                imp = int(n)

                if savefile == 0 and imp in [1, 2, 3, 4, 5]:
                    savefile += 1
                    start()
                elif savefile == 1 and float(n) == imp:
                    savefile += 1
                    num = imp
                    next1()

                if t > 0 and  savefile>2 :

                    if right == imp:
                        many_right += 1
                        many += 1
                        big_label.text = '√ 正确！'
                        score += 1
                    else:
                        many += 1
                        big_label.text = f'× 错误！\n{right}'

                    try:
                        tl.text = '你这次一共算了{}道题\n算对了{}题，正确率{:.2%}'.format(many, many_right,many_right / many)
                    except:
                        tl.text = '你这次一共算了0道题\n算对了0题，正确率0'
                    next1()
                elif t > 0 and savefile==2:
                    savefile += 1

            if ing:
                guiwei()

            input1.value = 0

        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box()
        box1 = toga.Box()
        box_shuru = toga.Box()
        box2 = toga.Box()
        box3 = toga.Box()
        main_box.add(box1,box_shuru,box2,box3)

        big_label = toga.Label('口算练习')

        big_label.style.color = 'red'
        big_label.style.background_color = 'lightblue'
        big_label.style.text_align = 'center'
        big_label.style.font_size='50'
        box1.add(big_label)
        main_box.style.direction='column'

        input1 = toga.NumberInput()
        input1.style.width = 250
        input1.style.font_size = 30
        box_shuru.add(input1)

        button_fu = toga.Button('输入负号 -',on_press=on_fu)
        button_fu.style.font_size = 15

        button1 = toga.Button('确定！',on_press=button)
        button1.style.font_size = 15

        box2.add(button_fu,button1)

        out_label = toga.Label('请选择难度（输入序号）！')
        out_label.style.font_size = 20

        box3.add(out_label)

        out_label.text='''
请选择你的难度（输入序号）
1  简单
2  中等
3  较难
4  很难
5  非常难
'''
        box4 = toga.Box()
        main_box.add(box4)
        button2 = toga.Button('重新开始', on_press=anxia2)
        button2.style.font_size = 25
        box4.add(button2)

        textbox = toga.Box()
        main_box.add(textbox)
        tl = toga.Label(' ')
        textbox.add(tl)

        try:
            tl.text = '你这次一共算了{}道题\n算对了{}题，正确率{:.2%}'.format(many, many_right, many_right / many)
        except:
            tl.text = '你这次一共算了0道题\n算对了0题，正确率0'

        box5 = toga.Box()
        main_box.add(box5)
        bt1 = toga.Button('结果始终为正数',on_press=weizheng)
        bt2 = toga.Button('结果可能为负数',on_press=weifu)
        bt1.style.font_size = 15
        bt2.style.font_size = 15
        box5.add(bt1,bt2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return exercise1()