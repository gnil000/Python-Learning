from curses import window
from itertools import count
import tkinter


def click_Convert():
    label2.config(text=((float(entry1.get())-32)/1.8))


def click_Quit():
    window.quit()


window = tkinter.Tk()
# count = tkinter.StringVar()

window.geometry('300x200')
frame1 = tkinter.Frame(window)
frame1.pack()
label1 = tkinter.Label(frame1, text='Temperature in Fahrenheit')
label1.pack()
entry1 = tkinter.Entry(frame1)
entry1.pack()
label2 = tkinter.Label(frame1)
label2.pack()

frame2 = tkinter.Frame(window)
frame2.pack()
button1 = tkinter.Button(frame2, text='Convert', command=click_Convert)
button1.pack()
button1 = tkinter.Button(frame2, text='Quit', command=click_Quit)
button1.pack()


window.mainloop()
