# coding=UTF-8
from Tkinter import *
from random import *


class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.latin = 0
        self.sanscrit = 0
        self.text = []
        self.undersquare = 0
        self.oversquare = 0


def version():
    t = Toplevel(root)
    t.title('Version Information')
    Label(t, justify='left', text='This is the 1.0 version of Kana Kiri. \n' +
                                  'Author: Fushiginahito \n' +
                                  'All Rights Reserved \n' +
                                  '                                   9/25/2019').pack()
    Button(t, text='确定', command=t.withdraw).pack()


def about():
    t = Toplevel(root)
    t.title('About Kana')
    Label(t, justify='left', text='To Be Announced.').pack()
    Button(t, text='确定', command=t.withdraw).pack()


def restart2():
    restart(1)


def restart(event):
    global cpy, correct, finish, r, p, sanskrit

    cpy = recover_alphabet()

    correct = 0.0
    finish = -1
    r = 0
    p = len(sanskrit) - 1

    shuffle(sanskrit)
    change(1)


def learning_mode():
    global mode

    if mode != 2:
        canvas.move(questiontag[0], 0, 30)
        canvas.move(questiontag[1], 0, -100)

        canvas.itemconfig(questiontag[0], state='normal')
        canvas.itemconfig(questiontag[1], font=('Times New Roman', 50), state='normal')
        for i in alphabet:
            canvas.itemconfig(i.text[0], state='normal')
            canvas.itemconfig(i.text[1], state='hidden')

        canvas.itemconfig(correcttag, state='hidden')
        canvas.itemconfig(typetag, state='hidden')
        canvas.itemconfig(typebutton, state='hidden')
        canvas.itemconfig(modetag,  text='LEARNING MODE')

    mode = 2
    restart(1)


def quizzing_mode():
    global mode

    if mode == 2:
        canvas.move(questiontag[0], 0, -30)
        canvas.move(questiontag[1], 0, 100)
        canvas.itemconfig(questiontag[1], font=('Times New Roman', 100))

        if questiontype == 1:
            sanskrit_only()
        elif questiontype == 2:
            latin_only()

        canvas.itemconfig(correcttag,  text='CORRECT: --%', state='normal')
        canvas.itemconfig(typetag, state='normal')
        canvas.itemconfig(typebutton, state='normal')
        canvas.itemconfig(modetag,  text='QUIZZING MODE')

    mode = 1
    restart(1)


def change_question_type(event):
    global questiontype
    
    if questiontype == 0:
        questiontype = 1
        sanskrit_only()
        canvas.itemconfig(typetag, text='HIRAGANA ONLY')
    elif questiontype == 1:
        questiontype = 2
        latin_only()
        canvas.itemconfig(typetag, text='LATIN ONLY')
    elif questiontype == 2:
        questiontype = 0
        canvas.itemconfig(typetag, text='MIXED QUESTION')

    restart(1)


def change_mode(event):
    global mode

    if mode != 2:
        learning_mode()
    elif mode == 2:
        quizzing_mode()

    restart(1)


def root_menu():
    main_menu = Menu(root)
    start_menu = Menu(main_menu)
    main_menu.add_cascade(label="Start", menu=start_menu)
    start_menu.add_command(label='Restart', command=restart2)
    start_menu.add_command(label='Learning Mode', command=learning_mode)
    start_menu.add_command(label='Quizzing Mode', command=quizzing_mode)
    start_menu.add_separator()
    start_menu.add_command(label='Quit', command=root.quit)
    help_menu = Menu(main_menu)
    main_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label='Version Info', command=version)
    help_menu.add_command(label='About Kana', command=about)
    root.config(menu=main_menu)


def handler_adaptor(fun, *kwds):
     return lambda event, f=fun, k=kwds: f(event, *k)


def griding():
    global alphabet, cpy

    if mode == 1:
        shuffle(cpy)
    for i in range(len(alphabet)):
        m = 50 + alphabet[i].x * 50
        n = 360 + alphabet[i].y * 50

        alphabet[i].sanscrit = cpy[i][0]
        alphabet[i].latin = cpy[i][1]
        alphabet[i].undersquare = canvas.create_rectangle(m, n, m + 50, n + 50, fill='grey', width=3, outline='white')
        alphabet[i].text += [canvas.create_text(m + 25, n + 25, text=cpy[i][0], font=('DFKai-SB', 25), anchor='center')]
        alphabet[i].text += [canvas.create_text(m + 25, n + 25, text=cpy[i][1], font=('Times New Roman', 20), anchor='center', state='hidden')]
        alphabet[i].oversquare = canvas.create_rectangle(m, n, m + 50, n + 50, fill='', outline='')

        canvas.tag_bind(alphabet[i].oversquare, '<Enter>', func=handler_adaptor(choose, alphabet[i]))
        canvas.tag_bind(alphabet[i].oversquare, '<Leave>', func=handler_adaptor(cancel, alphabet[i]))
        canvas.tag_bind(alphabet[i].oversquare, '<Button-1>', func=handler_adaptor(check, alphabet[i]))


def enter_button(event, tag):
    canvas.itemconfig(tag, fill='white')


def leave_button(event, tag):
    canvas.itemconfig(tag, fill='black')


def mixed():
    global randnum, mode, questiontype

    randnum = randint(0, 1)
    if randnum == 1:
        sanskrit_only()
    else:
        latin_only()


def sanskrit_only():
    canvas.itemconfig(questiontag[0], state='normal')
    canvas.itemconfig(questiontag[1], state='hidden')
    for i in alphabet:
        canvas.itemconfig(i.text[0], state='hidden')
        canvas.itemconfig(i.text[1], state='normal')


def latin_only():
    canvas.itemconfig(questiontag[0], state='hidden')
    canvas.itemconfig(questiontag[1], state='normal')
    for i in alphabet:
        canvas.itemconfig(i.text[0], state='normal')
        canvas.itemconfig(i.text[1], state='hidden')


def change(event):
    global p, sanskrit, mode, r, finish, alphabet, question

    canvas.itemconfig(youranswer.undersquare, fill='grey')
    canvas.itemconfig(answer.undersquare, fill='grey')

    if mode != 2:
        mode = 1
        shuffle(cpy)
        if questiontype == 0:
            mixed()
        elif questiontype == 1:
            sanskrit_only()
        elif questiontype == 2:
            latin_only()

    for i in range(len(alphabet)):
        alphabet[i].sanscrit = cpy[i][0]
        alphabet[i].latin = cpy[i][1]
        canvas.itemconfig(alphabet[i].text[0], text=cpy[i][0])
        canvas.itemconfig(alphabet[i].text[1], text=cpy[i][1])

    finish = finish + 1
    canvas.itemconfig(totaltag, text='FINISH: %d' % finish)
    if finish == 0:
        canvas.itemconfig(correcttag, text='CORRECT: --%')
    else:
        canvas.itemconfig(correcttag, text='CORRECT: %.2f%%' % (correct / finish * 100))

    p = p + 1
    if p == len(sanskrit):
        p = 0
        r = r + 1
        canvas.itemconfig(roundtag, text='ROUND: %d' % r)
        shuffle(sanskrit)

    canvas.itemconfig(c, state='hidden')
    canvas.itemconfig(questiontag[0], text=sanskrit[p][0])
    canvas.itemconfig(questiontag[1], text=sanskrit[p][1])
    question[0] = sanskrit[p][0]
    question[1] = sanskrit[p][1]
    canvas.itemconfig(c, state='normal')


mutex = 0


def choose(event, i):
    global mode, mutex
    if mode == 1:
        canvas.itemconfig(i.undersquare, fill='white')
    if mode == 2 and mutex == 0:
        mutex = 1
        canvas.itemconfig(i.undersquare, fill='white')
        canvas.itemconfig(i.text[0], state='hidden')
        canvas.itemconfig(i.text[1], state='normal')

        canvas.itemconfig(c, state='hidden')
        canvas.itemconfig(questiontag[0], text=i.sanscrit)
        canvas.itemconfig(questiontag[1], text=i.latin)
        canvas.itemconfig(c, state='normal')


def cancel(event, i):
    global mode, mutex
    if mode == 1:
        canvas.itemconfig(i.undersquare, fill='grey')
    if mode == 2 and mutex == 1:
        mutex = 0
        canvas.itemconfig(i.undersquare, fill='grey')
        canvas.itemconfig(i.text[0], state='normal')
        canvas.itemconfig(i.text[1], state='hidden')

        canvas.itemconfig(c, state='hidden')
        canvas.itemconfig(questiontag[0], text=question[0])
        canvas.itemconfig(questiontag[1], text=question[1])
        canvas.itemconfig(c, state='normal')


def check(event, i):
    global mode, p, sanskrit, canvas, youranswer, answer, alphabet, correct
    if mode == 1:
        mode = 0
        youranswer = i
        for j in alphabet:
            if j.sanscrit == sanskrit[p][0]:
                answer = j
                break

        if answer.sanscrit == youranswer.sanscrit:
            canvas.itemconfig(youranswer.undersquare, fill='green')
            correct = correct + 1
        else:
            canvas.itemconfig(youranswer.undersquare, fill='red')
            canvas.itemconfig(answer.undersquare, fill='green')


def recover_alphabet():
    return [('あ', 'a'), ('い', 'i'), ('う', 'u'), ('え', 'e'), ('お', 'o'),
           ('か', 'ka'), ('き', 'ki'), ('く', 'ku'), ('け', 'ke'), ('こ', 'ko'),
           ('さ', 'sa'), ('し', 'shi'), ('す', 'su'), ('せ', 'se'), ('そ', 'so'),
           ('た', 'ta'), ('ち', 'chi'), ('つ', 'tsu'), ('て', 'te'), ('と', 'to'),
           ('な', 'na'), ('に', 'ni'), ('ぬ', 'nu'), ('ね', 'ne'), ('の', 'no'),
           ('は', 'ha'), ('ひ', 'hi'), ('ふ', 'fu'), ('へ', 'he'), ('ほ', 'ho'),
           ('ま', 'ma'), ('み', 'mi'), ('む', 'mu'), ('め', 'me'), ('も', 'mo'),
           ('や', 'ya'), ('ゆ', 'yu'), ('よ', 'yo'),
           ('ら', 'ra'), ('り', 'ri'), ('る', 'ru'), ('れ', 're'), ('ろ', 'ro'),
           ('わ', 'wa'), ('を', 'wo'), ('ん', 'n')]
##################################################变量常量声
sanskrit = recover_alphabet()
cpy = recover_alphabet()

alphabet = [Cube(0, 0), Cube(0, 1), Cube(0, 2), Cube(0, 3), Cube(0, 4),
            Cube(1, 0), Cube(1, 1), Cube(1, 2), Cube(1, 3), Cube(1, 4),
            Cube(2, 0), Cube(2, 1), Cube(2, 2), Cube(2, 3), Cube(2, 4),
            Cube(3, 0), Cube(3, 1), Cube(3, 2), Cube(3, 3), Cube(3, 4),
            Cube(4, 0), Cube(4, 1), Cube(4, 2), Cube(4, 3), Cube(4, 4),
            Cube(5, 0), Cube(5, 1), Cube(5, 2), Cube(5, 3), Cube(5, 4),
            Cube(6, 0), Cube(6, 1), Cube(6, 2), Cube(6, 3), Cube(6, 4),
            Cube(7, 0), Cube(7, 2), Cube(7, 4),
            Cube(8, 0), Cube(8, 1), Cube(8, 2), Cube(8, 3), Cube(8, 4),
            Cube(9, 0), Cube(9, 2), Cube(9, 4)]
youranswer = alphabet[0]
answer = alphabet[0]
correct = 0.0
finish = 0
r = 1
p = 0
randnum = randint(0, 1)

# 1=quizzing, 0=checking, 2=learning
mode = 1
# 0=mixed, 1=sanskrit only, 2=latin only
questiontype = 0
#################################################界面生成
root = Tk()
root.title('KANA KIRI 1.0')
root.geometry('600x650')
root_menu()

canvas = Canvas(root, height=700, width=600, bg='grey')
canvas.place(x=-1, y=-4)
c = canvas.create_rectangle(0, 0, 600, 700, fill='grey', outline='')
questiontag = [canvas.create_text(300, 210, text='', font=('DFKai-SB', 130), anchor='center')]
questiontag += [canvas.create_text(300, 200, text='', font=('Times New Roman', 100))]
question = [0, 0]

griding()

nexttag = canvas.create_text(530, 320, text='NEXT', font=('Andalus', 25, 'bold'), anchor='center')
nextbutton = canvas.create_rectangle(480, 295, 580, 340, fill='', outline='')
canvas.tag_bind(nextbutton, '<Enter>', func=handler_adaptor(enter_button, nexttag))
canvas.tag_bind(nextbutton, '<Leave>', func=handler_adaptor(leave_button, nexttag))
canvas.tag_bind(nextbutton, '<Button-1>', change)

restarttag = canvas.create_text(590, 8, text='RESTART', font=('Andalus', 15, 'bold'), anchor='ne')
restartbutton = canvas.create_rectangle(510, 10, 595, 30, fill='', outline='')
canvas.tag_bind(restartbutton, '<Enter>', func=handler_adaptor(enter_button, restarttag))
canvas.tag_bind(restartbutton, '<Leave>', func=handler_adaptor(leave_button, restarttag))
canvas.tag_bind(restartbutton, '<Button-1>', restart)

modetag = canvas.create_text(590, 32, text='QUIZZING MODE', font=('Andalus', 15, 'bold'), anchor='ne')
modebutton = canvas.create_rectangle(410, 37, 595, 59, fill='', outline='')
canvas.tag_bind(modebutton, '<Enter>', func=handler_adaptor(enter_button, modetag))
canvas.tag_bind(modebutton, '<Leave>', func=handler_adaptor(leave_button, modetag))
canvas.tag_bind(modebutton, '<Button-1>', change_mode)

typetag = canvas.create_text(590, 56, text='MIXED QUESTION', font=('Andalus', 15, 'bold'), anchor='ne')
typebutton = canvas.create_rectangle(410, 63, 595, 83, fill='', outline='')
canvas.tag_bind(typebutton, '<Enter>', func=handler_adaptor(enter_button, typetag))
canvas.tag_bind(typebutton, '<Leave>', func=handler_adaptor(leave_button, typetag))
canvas.tag_bind(typebutton, '<Button-1>', change_question_type)

roundtag = canvas.create_text(10, 8, text='ROUND: %d' % r, font=('Andalus', 15, 'bold'), anchor='nw')
totaltag = canvas.create_text(10, 32, text='FINISH: %d' % finish, font=('Andalus', 15, 'bold'), anchor='nw')
correcttag = canvas.create_text(10, 56, text='CORRECT: --%', font=('Andalus', 15, 'bold'), anchor='nw')

restart(1)

root.mainloop()
