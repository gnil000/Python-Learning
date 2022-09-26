from curses import window
from itertools import count
from operator import truediv
import tkinter
import random

prevWord = ''


def wordExists(word, valueWord):
    if words.get(word) != None and words.get(word, valueWord) == valueWord:
        return True
    else:
        return False


def click_Replace():
    global prevWord
    newWord = random.choice(list(words.values()))
    while newWord == prevWord:
        prevWord = newWord
        newWord = random.choice(list(words.values()))
    prevWord = newWord
    valueWord.set(newWord)


def click_Check():
    if wordExists(entry1.get(), valueWord.get()) == True:
        print(entry1.get())
        print(valueWord.get())
        label2.config(text='Вы супер, всё верно!')
    else:
        print(entry1.get())
        print(valueWord)
        label2.config(text='Неверно, попробуйте ещё раз')


words = {'cat': 'кот', 'dog': 'собака', 'apple': 'яблоко',
         'deterministic': 'детерминированный'}


window = tkinter.Tk()

valueWord = tkinter.StringVar()
valueWord.set('')

window.geometry('300x125')
frame1 = tkinter.Frame(window)
frame1.pack()
label1 = tkinter.Label(frame1, textvariable=valueWord)
label1.pack()
entry1 = tkinter.Entry(frame1)
entry1.pack()
button1 = tkinter.Button(frame1, text='Принять', command=click_Check)
button1.pack()
button2 = tkinter.Button(
    frame1, text='Зарандомить слово', command=click_Replace)
button2.pack()
label2 = tkinter.Label(frame1)
label2.pack()


window.mainloop()
