# coding=UTF-8
from Tkinter import *
from random import *


class Letter:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
        self.latin = 0
        self.sanscrit = 0
        self.text = 0
        self.square = 0
        self.square2 = 0



def new_game():
    return

def root_menu():
    main_menu = Menu(root)
    start_menu = Menu(main_menu)
    main_menu.add_cascade(label="開始", menu=start_menu)
    start_menu.add_command(label='新遊戲', command=new_game)
    start_menu.add_command(label='***', command=new_game)
    start_menu.add_separator()
    start_menu.add_command(label='設置', command=new_game)
    start_menu.add_separator()
    start_menu.add_command(label='退出', command=root.quit)
    help_menu = Menu(main_menu)
    main_menu.add_cascade(label="幫助", menu=help_menu)
    help_menu.add_command(label='操作指南', command=new_game)
    help_menu.add_command(label='作弊', command=new_game)
    root.config(menu=main_menu)


def handler_adaptor(fun, *kwds):
     return lambda event, f=fun, k=kwds: f(event, *k)


def griding():
    global alphabet, sanskrit
    for i in range(len(alphabet)):
        m = 50 + alphabet[i].x * 50
        n = 360 + alphabet[i].y * 50

        alphabet[i].text = sanskrit[i][0]
        alphabet[i].square = canvas.create_rectangle(m, n, m + 50, n + 50, fill='grey', width=3, outline='white')
        #alphabet[i].latin = canvas.create_text(m + 25, n + 25, text=sanskrit[i][1], font=('Times New Roman', 20), anchor='center')
        alphabet[i].sanscrit = canvas.create_text(m + 25, n + 25, text=sanskrit[i][0], font=('Kokila', 30), anchor='center')
        alphabet[i].square2 = canvas.create_rectangle(m, n, m + 50, n + 50, fill='', outline='')

        canvas.tag_bind(alphabet[i].square2, '<Enter>', func=handler_adaptor(choose, alphabet[i].square))
        canvas.tag_bind(alphabet[i].square2, '<Leave>', func=handler_adaptor(cancel, alphabet[i].square))
        canvas.tag_bind(alphabet[i].square2, '<Button-1>', func=handler_adaptor(check, alphabet[i]))

        if sanskrit[i][0] == 'ऋ' or sanskrit[i][0] == 'ॠ':
            canvas.move(alphabet[i].sanscrit, 0, -5)
            canvas.itemconfig(alphabet[i].sanscrit, font=('Mangal', 20))


def gotonext(event):
    canvas.itemconfig(nextone, fill='white')


def notgotonext(event):
    canvas.itemconfig(nextone, fill='black')


def change(event):
    global p, sanskrit, state, r, total

    state = 1
    canvas.itemconfig(youranswer.square, fill='grey')
    canvas.itemconfig(answer.square, fill='grey')

    if sanskrit[p][0] == 'ऋ'or sanskrit[p][0] == 'ॠ':
        canvas.move(x, 0, 50)
        canvas.itemconfig(x, font=('Kokila', 200))

    total = total + 1
    canvas.itemconfig(totaltag, text='FINISH: %d' % total)
    canvas.itemconfig(correcttag, text='CORRECT: %.2f%%' % (correct / total * 100))

    p = p + 1
    if p == len(sanskrit):
        p = 0
        r = r + 1
        canvas.itemconfig(roundtag, text='ROUND: %d' % r)
        shuffle(sanskrit)

    if sanskrit[p][0] == 'ऋ'or sanskrit[p][0] == 'ॠ':
        canvas.move(x, 0, -50)
        canvas.itemconfig(x, font=('Mangal', 140))

    canvas.itemconfig(c, state='hidden')
    canvas.itemconfig(x, text=sanskrit[p][0])
    canvas.itemconfig(latin, text=sanskrit[p][1])
    canvas.itemconfig(c, state='normal')


def choose(event, tag):
    global state
    if state == 1:
        canvas.itemconfig(tag, fill='white')


def cancel(event, tag):
    global state
    if state == 1:
        canvas.itemconfig(tag, fill='grey')


def check(event, i):
    global state, p, sanskrit, canvas, youranswer, answer, alphabet, correct

    if state == 1:
        state = 0
        youranswer = i
        for j in alphabet:
            if j.text == sanskrit[p][0]:
                answer = j
                break

        if answer.text == youranswer.text:
            canvas.itemconfig(youranswer.square, fill='green')
            correct = correct + 1
        else:
            canvas.itemconfig(youranswer.square, fill='red')
            canvas.itemconfig(answer.square, fill='green')

root = Tk()
root.title('SANSKRIT KIRI')
root.geometry('600x650')
root_menu()

canvas = Canvas(root, height=700, width=600, bg='grey')
canvas.place(x=-1, y=-4)
c = canvas.create_rectangle(0, 0, 600, 700, fill='grey', outline='')
x = canvas.create_text(300, 210, text='', font=('Kokila', 200), anchor='center', state='hidden')

sanskrit = [('अ', 'a'), ('आ', 'ā'), ('इ', 'i'), ('ई', 'ī'),
            ('उ', 'u'), ('ऊ', 'ū'), ('ऋ', 'ṛ'), ('ॠ', 'ṝ'), ('ऌ', 'ḷ'),
            ('ए', 'e'), ('ऐ', 'ai'), ('ओ', 'o'), ('औ', 'au'),
            ('क', 'ka'), ('ख', 'kha'), ('ग', 'ga'), ('घ', 'gha'), ('ङ', 'ṅa'),
            ('च', 'ca'), ('छ', 'cha'), ('ज', 'ja'), ('झ', 'jha'), ('ञ', 'ña'),
            ('ट', 'ṭa'), ('ठ', 'ṭha'), ('ड', 'ḍa'), ('ढ', 'ḍha'), ('ण', 'ṇa'),
            ('त', 'ta'), ('थ', 'tha'), ('द', 'da'), ('ध', 'dha'), ('न', 'na'),
            ('प', 'pa'), ('फ', 'pha'), ('ब', 'ba'), ('भ', 'bha'), ('म', 'ma'),
            ('य', 'ya'), ('र', 'ra'), ('ल', 'la'), ('व', 'va'),
            ('श', 'śa'), ('ष', 'ṣa'), ('स', 'sa'),
            ('ह', 'ha')]
alphabet = [Letter(0, 0), Letter(1, 0), Letter(0, 1), Letter(1, 1),
            Letter(0, 2), Letter(1, 2), Letter(0, 3), Letter(1, 3), Letter(0, 4),
            Letter(2, 0), Letter(2, 1), Letter(2, 2), Letter(2, 3),
            Letter(3, 0), Letter(3, 1), Letter(3, 2), Letter(3, 3), Letter(3, 4),
            Letter(4, 0), Letter(4, 1), Letter(4, 2), Letter(4, 3), Letter(4, 4),
            Letter(5, 0), Letter(5, 1), Letter(5, 2), Letter(5, 3), Letter(5, 4),
            Letter(6, 0), Letter(6, 1), Letter(6, 2), Letter(6, 3), Letter(6, 4),
            Letter(7, 0), Letter(7, 1), Letter(7, 2), Letter(7, 3), Letter(7, 4),
            Letter(8, 0), Letter(8, 1), Letter(8, 2), Letter(8, 3),
            Letter(9, 0), Letter(9, 1), Letter(9, 2),
            Letter(9, 4)]

griding()

state = 1
youranswer = alphabet[0]
answer = alphabet[0]
correct = 0.0
total = 0
r = 1

shuffle(sanskrit)
p = 0
latin = canvas.create_text(300, 180, text=sanskrit[p][1], font=('Times New Roman', 100))
canvas.itemconfig(x, text=sanskrit[p][0])
if sanskrit[p][0] == 'ऋ' or sanskrit[p][0] == 'ॠ':
    canvas.move(x, 0, -50)
    canvas.itemconfig(x, font=('Mangal', 140))


nextone = canvas.create_text(530, 320, text='NEXT', font=('Andalus', 25, 'bold'), anchor='center')
next = canvas.create_rectangle(480, 295, 580, 340, fill='', outline='')
canvas.tag_bind(next, '<Enter>', gotonext)
canvas.tag_bind(next, '<Leave>', notgotonext)
canvas.tag_bind(next, '<Button-1>', change)

roundtag = canvas.create_text(10, 8, text='ROUND: %d' % r, font=('Andalus', 15, 'bold'), anchor='nw')
totaltag = canvas.create_text(10, 28, text='FINISH: %d' % total, font=('Andalus', 15, 'bold'), anchor='nw')
correcttag = canvas.create_text(10, 48, text='CORRECT: --%', font=('Andalus', 15, 'bold'), anchor='nw')




root.mainloop()
