## -*- coding: utf-8 -*-
from Tkinter import Tk, Label, Button, Entry, Checkbutton
import voice_recording


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("listening window")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.label.place(x=140, y=10)

        self.label_word = Label(master, text="Озвучить: a")
        self.label_word.pack()
        self.label_word.place(x=190, y=40)

        self.checkRU = Checkbutton(master, text="Russian")
        self.checkRU.pack()
        self.checkRU.place(x=350, y=10)

        self.checkEn = Checkbutton(master, text="English")
        self.checkEn.pack()
        self.checkEn.place(x=350, y=40)

        self.start_button = Button(master, text="Start recording", width=11, command=self.greet)
        self.start_button.pack()
        self.start_button.place(x=250, y=10)

        self.close_button = Button(master, text="Close", width=11, command=master.quit)
        self.close_button.pack()
        self.close_button.place(x=250, y=40)

        self.alphabet_english = [x for x in 'abc']
        self.alphabet_russian = [x for x in 'абв']
        self.x = voice_recording

    def greet(self):
        print("Greetings!")
        if not self.alphabet_english:
            print("List is empty")
            self.alphabet_english = [x for x in 'abcdefghijklmnopqrstuvwxyz']
        print (self.alphabet_english)
        number = self.alphabet_english.pop(0)
        print (number)
        self.x.my_record(number + ".wav")
        if self.alphabet_english:
            self.label_word['text'] = "Озвучить: " + self.alphabet_english[0]
        else:
            self.label_word['text'] = 'Озвучить: a'


root = Tk()
my_gui = MyFirstGUI(root)
root.geometry('600x100+200+100')
root.mainloop()
