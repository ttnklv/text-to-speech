from Tkinter import Tk, Label, Button, Text, Checkbutton
from pydub import AudioSegment
import subprocess
import os


class MySecondGUI:
    def __init__(self, master):
        self.master = master
        master.title("reading window")

        self.label = Label(master, text="This is our second GUI!")
        self.label.pack()

        self.text = Text(width=25, height=5, bg="darkgreen", fg='white')
        self.text.pack()

        self.read_button = Button(master, width=9, text="Read text", command=self.read)
        self.read_button.pack()
        self.read_button.place(x=120, y=40)

        self.close_button = Button(master, width=9, text="Close", command=master.quit)
        self.close_button.pack()
        self.close_button.place(x=120, y=70)

        self.pin = 0



    def read(self):
        open("combined.wav", "w")
        os.remove("combined.wav")
        open("combined.wav", "w")
        text = self.text.get("1.0", 'end')
        user_text = map(lambda c: c, text)
        print user_text
        combined = AudioSegment.from_file(user_text[0] + ".wav")
        combined.export("combined.wav", format='wav')
        user_text.pop(0)
        for number in user_text:
            if number == '\n' or number == ' ':
                continue
            sound1 = AudioSegment.from_file("combined.wav")
            sound2 = AudioSegment.from_file(number + ".wav")
            combined = sound1 + sound2
            combined.export("combined.wav", format='wav')
        self.pin = subprocess.call("python voice_acting.py combined.wav", shell=True)


    # def close(self):
        # self.pin.kill()


root = Tk()
my_gui = MySecondGUI(root)
root.geometry('600x130+200+100')

root.mainloop()

