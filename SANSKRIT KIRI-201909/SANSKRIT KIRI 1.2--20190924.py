# coding=UTF-8
from Tkinter import *
from random import randint


class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.latin = 0
        self.sanscrit = 0
        self.text = []
        self.undersquare = 0
        self.oversquare = 0


def restart():
    global cpy, youranswer, answer, correct, total, r, p, sanskrit

    canvas.itemconfig(youranswer.undersquare, fill='grey')
    canvas.itemconfig(answer.undersquare, fill='grey')

    if question[0] == 'ऋ'or question[0] == 'ॠ':
        canvas.move(questiontag[0], 0, 50)
        canvas.itemconfig(questiontag[0], font=('Kokila', 200))

    canvas.move(alphabet[special[0]].text[0], 0, 5)
    canvas.itemconfig(alphabet[special[0]].text[0], font=('Kokila', 30))
    canvas.move(alphabet[special[1]].text[0], 0, 5)
    canvas.itemconfig(alphabet[special[1]].text[0], font=('Kokila', 30))

    cpy = [('अ', 'a'), ('आ', 'ā'), ('इ', 'i'), ('ई', 'ī'),
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
    youranswer = alphabet[0]
    answer = alphabet[0]
    correct = 0.0
    total = 0
    r = 1
    p = 0

    shuffle(sanskrit)
    question[0] = sanskrit[p][0]
    question[1] = sanskrit[p][1]
    canvas.itemconfig(questiontag[0], text=sanskrit[p][0])
    canvas.itemconfig(questiontag[1], text=sanskrit[p][1])
    if question[0] == 'ऋ' or question[0] == 'ॠ':
        canvas.move(questiontag[0], 0, -50)
        canvas.itemconfig(questiontag[0], font=('Mangal', 140))

    if state == 1:
        shuffle(cpy)
    canvas.itemconfig(roundtag, text='ROUND: %d' % r)
    canvas.itemconfig(totaltag, text='FINISH: %d' % total)
    for i in range(len(alphabet)):
        alphabet[i].sanscrit = cpy[i][0]
        alphabet[i].latin = cpy[i][1]
        canvas.itemconfig(alphabet[i].text[0], text=cpy[i][0])
        canvas.itemconfig(alphabet[i].text[1], text=cpy[i][1])
        if cpy[i][0] == 'ऋ' or cpy[i][0] == 'ॠ':
            if cpy[i][0] == 'ऋ':
                special[0] = i
            else:
                special[1] = i
            canvas.move(alphabet[i].text[0], 0, -5)
            canvas.itemconfig(alphabet[i].text[0], font=('Mangal', 20))


def learning_mode():
    global state

    if state != 2:
        canvas.move(questiontag[0], 0, 50)
        canvas.move(questiontag[1], 0, -100)

        canvas.itemconfig(questiontag[0], state='normal')
        canvas.itemconfig(questiontag[1], font=('Times New Roman', 50), state='normal')
        canvas.itemconfig(correcttag, state='hidden')

    state = 2
    restart()


def quizzing_mode():
    global state

    if state == 2:
        canvas.move(questiontag[0], 0, -50)
        canvas.move(questiontag[1], 0, 100)

        if type == 0:
            canvas.itemconfig(questiontag[0], state='hidden')
            canvas.itemconfig(questiontag[1], font=('Times New Roman', 100), state='normal')
        elif type == 1:
            canvas.itemconfig(questiontag[0], state='normal')
            canvas.itemconfig(questiontag[1], font=('Times New Roman', 100), state='hidden')
        elif type == 2:
            canvas.itemconfig(questiontag[0], state='hidden')
            canvas.itemconfig(questiontag[1], font=('Times New Roman', 100), state='normal')

        canvas.itemconfig(correcttag,  text='CORRECT: --%', state='normal')

    state = 1
    restart()


def root_menu():
    main_menu = Menu(root)
    start_menu = Menu(main_menu)
    main_menu.add_cascade(label="Start", menu=start_menu)
    start_menu.add_command(label='Restart', command=restart)
    start_menu.add_command(label='Learning Mode', command=learning_mode)
    start_menu.add_command(label='Quizzing Mode', command=quizzing_mode)
    start_menu.add_separator()
    start_menu.add_command(label='Settings/Question Type', command=restart)
    start_menu.add_separator()
    start_menu.add_command(label='Quit', command=root.quit)
    help_menu = Menu(main_menu)
    main_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label='Version Info', command=restart)
    help_menu.add_command(label='About SANSKRIT', command=restart)
    root.config(menu=main_menu)


def handler_adaptor(fun, *kwds):
     return lambda event, f=fun, k=kwds: f(event, *k)


def griding():
    global alphabet, cpy, special

    if state == 1:
        shuffle(cpy)
    for i in range(len(alphabet)):
        m = 50 + alphabet[i].x * 50
        n = 360 + alphabet[i].y * 50

        alphabet[i].sanscrit = cpy[i][0]
        alphabet[i].latin = cpy[i][1]
        alphabet[i].undersquare = canvas.create_rectangle(m, n, m + 50, n + 50, fill='grey', width=3, outline='white')
        alphabet[i].text += [canvas.create_text(m + 25, n + 25, text=cpy[i][0], font=('Kokila', 30), anchor='center')]
        alphabet[i].text += [canvas.create_text(m + 25, n + 25, text=cpy[i][1], font=('Times New Roman', 20), anchor='center', state='hidden')]
        alphabet[i].oversquare = canvas.create_rectangle(m, n, m + 50, n + 50, fill='', outline='')

        canvas.tag_bind(alphabet[i].oversquare, '<Enter>', func=handler_adaptor(choose, alphabet[i]))
        canvas.tag_bind(alphabet[i].oversquare, '<Leave>', func=handler_adaptor(cancel, alphabet[i]))
        canvas.tag_bind(alphabet[i].oversquare, '<Button-1>', func=handler_adaptor(check, alphabet[i]))

        if cpy[i][0] == 'ऋ' or cpy[i][0] == 'ॠ':
            if cpy[i][0] == 'ऋ':
                special[0] = i
            else:
                special[1] = i
            canvas.move(alphabet[i].text[0], 0, -5)
            canvas.itemconfig(alphabet[i].text[0], font=('Mangal', 20))


def enter_button(event, tag):
    canvas.itemconfig(tag, fill='white')


def leave_button(event, tag):
    canvas.itemconfig(tag, fill='black')


def change(event):
    global p, sanskrit, state, r, total, alphabet, special, question

    canvas.itemconfig(youranswer.undersquare, fill='grey')
    canvas.itemconfig(answer.undersquare, fill='grey')

    if sanskrit[p][0] == 'ऋ'or sanskrit[p][0] == 'ॠ':
        canvas.move(questiontag[0], 0, 50)
        canvas.itemconfig(questiontag[0], font=('Kokila', 200))

    if state == 0 or state == 1:
        state = 1
        shuffle(cpy)
        canvas.move(alphabet[special[0]].text[0], 0, 5)
        canvas.itemconfig(alphabet[special[0]].text[0], font=('Kokila', 30))
        canvas.move(alphabet[special[1]].text[0], 0, 5)
        canvas.itemconfig(alphabet[special[1]].text[0], font=('Kokila', 30))
        for i in range(len(alphabet)):
            alphabet[i].sanscrit = cpy[i][0]
            alphabet[i].latin = cpy[i][1]
            canvas.itemconfig(alphabet[i].text[0], text=cpy[i][0])
            canvas.itemconfig(alphabet[i].text[1], text=cpy[i][1])
            if cpy[i][0] == 'ऋ' or cpy[i][0] == 'ॠ':
                if cpy[i][0] == 'ऋ':
                    special[0] = i
                else:
                    special[1] = i
                canvas.move(alphabet[i].text[0], 0, -5)
                canvas.itemconfig(alphabet[i].text[0], font=('Mangal', 20))

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
        canvas.move(questiontag[0], 0, -50)
        canvas.itemconfig(questiontag[0], font=('Mangal', 140))

    canvas.itemconfig(c, state='hidden')
    canvas.itemconfig(questiontag[0], text=sanskrit[p][0])
    canvas.itemconfig(questiontag[1], text=sanskrit[p][1])
    question[0] = sanskrit[p][0]
    question[1] = sanskrit[p][1]
    canvas.itemconfig(c, state='normal')


mutex = 0


def choose(event, i):
    global state, mutex
    if state == 1:
        canvas.itemconfig(i.undersquare, fill='white')
    if state == 2 and mutex == 0:
        mutex = 1
        canvas.itemconfig(i.undersquare, fill='white')
        canvas.itemconfig(i.text[0], state='hidden')
        canvas.itemconfig(i.text[1], state='normal')

        canvas.itemconfig(c, state='hidden')
        if (question[0] == 'ऋ' or question[0] == 'ॠ') and not (i.sanscrit == 'ऋ'or i.sanscrit == 'ॠ'):
            canvas.move(questiontag[0], 0, 50)
            canvas.itemconfig(questiontag[0], font=('Kokila', 200))
        elif (i.sanscrit == 'ऋ'or i.sanscrit == 'ॠ') and not (question[0] == 'ऋ' or question[0] == 'ॠ'):
            canvas.move(questiontag[0], 0, -50)
            canvas.itemconfig(questiontag[0], font=('Mangal', 140))
        canvas.itemconfig(questiontag[0], text=i.sanscrit)
        canvas.itemconfig(questiontag[1], text=i.latin)
        canvas.itemconfig(c, state='normal')


def cancel(event, i):
    global state, mutex
    if state == 1:
        canvas.itemconfig(i.undersquare, fill='grey')
    if state == 2 and mutex == 1:
        mutex = 0
        canvas.itemconfig(i.undersquare, fill='grey')
        canvas.itemconfig(i.text[0], state='normal')
        canvas.itemconfig(i.text[1], state='hidden')

        canvas.itemconfig(c, state='hidden')
        if (i.sanscrit == 'ऋ'or i.sanscrit == 'ॠ') and not (question[0] == 'ऋ' or question[0] == 'ॠ'):
            canvas.move(questiontag[0], 0, 50)
            canvas.itemconfig(questiontag[0], font=('Kokila', 200))
        elif (question[0] == 'ऋ' or question[0] == 'ॠ') and not (i.sanscrit == 'ऋ'or i.sanscrit == 'ॠ'):
            canvas.move(questiontag[0], 0, -50)
            canvas.itemconfig(questiontag[0], font=('Mangal', 140))
        canvas.itemconfig(questiontag[0], text=question[0])
        canvas.itemconfig(questiontag[1], text=question[1])
        canvas.itemconfig(c, state='normal')


def check(event, i):
    global state, p, sanskrit, canvas, youranswer, answer, alphabet, correct
    if state == 1:
        state = 0
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


##################################################变量常量声明
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
cpy = [('अ', 'a'), ('आ', 'ā'), ('इ', 'i'), ('ई', 'ī'),
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
alphabet = [Cube(0, 0), Cube(1, 0), Cube(0, 1), Cube(1, 1),
            Cube(0, 2), Cube(1, 2), Cube(0, 3), Cube(1, 3), Cube(0, 4),
            Cube(2, 0), Cube(2, 1), Cube(2, 2), Cube(2, 3),
            Cube(3, 0), Cube(3, 1), Cube(3, 2), Cube(3, 3), Cube(3, 4),
            Cube(4, 0), Cube(4, 1), Cube(4, 2), Cube(4, 3), Cube(4, 4),
            Cube(5, 0), Cube(5, 1), Cube(5, 2), Cube(5, 3), Cube(5, 4),
            Cube(6, 0), Cube(6, 1), Cube(6, 2), Cube(6, 3), Cube(6, 4),
            Cube(7, 0), Cube(7, 1), Cube(7, 2), Cube(7, 3), Cube(7, 4),
            Cube(8, 0), Cube(8, 1), Cube(8, 2), Cube(8, 3),
            Cube(9, 0), Cube(9, 1), Cube(9, 2),
            Cube(9, 4)]
special = [0, 0]
youranswer = alphabet[0]
answer = alphabet[0]
correct = 0.0
total = 0
r = 1
p = 0
randnum = randint(0, 1)

# 1=quizzing, 0=checking, 2=learning
state = 1
# 0=mixed, 1=sanskrit only, 2=latin only
type = 0
#################################################界面生成
root = Tk()
root.title('SANSKRIT KIRI 1.2')
root.geometry('600x650')
root_menu()

canvas = Canvas(root, height=700, width=600, bg='grey')
canvas.place(x=-1, y=-4)
c = canvas.create_rectangle(0, 0, 600, 700, fill='grey', outline='')
questiontag = [canvas.create_text(300, 210, text='', font=('Kokila', 200), anchor='center')]
questiontag += [canvas.create_text(300, 180, text='', font=('Times New Roman', 100))]
question = [0, 0]

griding()

nexttag = canvas.create_text(530, 320, text='NEXT', font=('Andalus', 25, 'bold'), anchor='center')
nextbutton = canvas.create_rectangle(480, 295, 580, 340, fill='', outline='')
canvas.tag_bind(nextbutton, '<Enter>', func=handler_adaptor(enter_button, nexttag))
canvas.tag_bind(nextbutton, '<Leave>', func=handler_adaptor(leave_button, nexttag))
canvas.tag_bind(nextbutton, '<Button-1>', change)

roundtag = canvas.create_text(10, 8, text='ROUND: %d' % r, font=('Andalus', 15, 'bold'), anchor='nw')
totaltag = canvas.create_text(10, 28, text='FINISH: %d' % total, font=('Andalus', 15, 'bold'), anchor='nw')
correcttag = canvas.create_text(10, 48, text='CORRECT: --%', font=('Andalus', 15, 'bold'), anchor='nw')
modetag = canvas.create_text(590, 8, text='QUIZZING MODE', font=('Andalus', 15, 'bold'), anchor='ne')
typetag = canvas.create_text(590, 28, text='LATIN ONLY', font=('Andalus', 15, 'bold'), anchor='ne')

restart()

root.mainloop()
