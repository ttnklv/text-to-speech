## -*- coding: utf-8 -*-
from Tkinter import Tk, Label, Button, Radiobutton, IntVar, Entry, StringVar
import voice_recording
import subprocess


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("listening window")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.label.place(x=100, y=30)

        self.label_2 = Label(master, text="Enter the name if you see fit: ")
        self.label_2.pack()
        self.label_2.place(x=100, y=5)

        self.message = StringVar()
        self.entry = Entry(textvariable=self.message)
        self.entry.place(x=320, y=15, anchor="c")

        self.label_word = Label(master, text="Vocalize: a")
        self.label_word.pack()
        self.label_word.place(x=120, y=60)

        self.var = IntVar()
        self.var.set(0)

        self.checkRU = Radiobutton(master, value=0, variable=self.var, text="Russian")
        self.checkRU.pack()
        self.checkRU.place(x=310, y=30)

        self.checkEn = Radiobutton(master, value=1, variable=self.var, text="English")
        self.checkEn.pack()
        self.checkEn.place(x=310, y=60)

        self.start_button = Button(master, text="Start recording", width=11, command=self.greet)
        self.start_button.pack()
        self.start_button.place(x=210, y=30)

        self.close_button = Button(master, text="Close", width=11, command=master.quit)
        self.close_button.pack()
        self.close_button.place(x=210, y=60)

        self.alphabet_english = [x for x in 'abcdefghijklmnopqrstuvwxyz']
        self.alphabet_russian = [x for x in unicode('абвгдежзийклмнопрстуфхцчшщыэюя', "utf-8")]
        self.x = voice_recording

        self.close_button = Button(master, text="Redirect", width=11, command=self.redirect)
        self.close_button.pack()
        self.close_button.place(x=210, y=90)

    def greet(self):
        if self.var.get() == 0:
            str_alphabet = "абвгдежзийклмнопрстуфхцчшщыэюя"
        else:
            str_alphabet = "abcdefghijklmnopqrstuvwxyz"

        if (self.var.get() == 1) and (not self.alphabet_english):
            print("List is empty")
            self.alphabet_english = [x for x in str_alphabet]
        elif (self.var.get() == 0) and (not self.alphabet_russian):
            self.alphabet_russian = [x for x in unicode(str_alphabet, "utf-8")]

        if self.var.get() == 0:
            number = self.alphabet_russian.pop(0)
        else:
            number = self.alphabet_english.pop(0)
        print (number)
        self.x.my_record(self.message.get() + "_" + number + ".wav")

        if self.alphabet_english and self.var.get() == 1:
            self.label_word['text'] = "Vocalize: " + self.alphabet_english[0]
        elif self.alphabet_english and self.var.get() == 0:
            self.label_word['text'] = "Vocalize: " + self.alphabet_russian[0]
        else:
            self.label_word['text'] = 'Vocalize: a'
            subprocess.call("python voice_acting.py combined.wav", shell=True)

    def redirect(self):
        subprocess.call("python read_GUI.py " + self.message.get())


root = Tk()
my_gui = MyFirstGUI(root)
root.geometry('500x120+200+100')
root.mainloop()
