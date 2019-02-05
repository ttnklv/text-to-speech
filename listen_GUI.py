from Tkinter import Tk, Label, Button, Entry, Checkbutton
import subprocess


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("listening window")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.label.place(x=140, y=10)

        self.label_word = Label(master, text="A")
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

    def greet(self):
        print("Greetings!")
        self.label['text'] = '* recording'
        instruction = 'python voice_recording.py'
        #subprocess.call("python voice_recording.py a.wav", shell=True)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        #alphabet = 'a'
        for number in alphabet:
            print (number)
            subprocess.call(instruction + " " + number + ".wav", shell=True)


#read_GUI.py


root = Tk()
my_gui = MyFirstGUI(root)
root.geometry('600x100+200+100')
root.mainloop()


