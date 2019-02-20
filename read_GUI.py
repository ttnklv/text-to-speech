from Tkinter import Tk, Label, Button, Text
from pydub import AudioSegment
import subprocess
import os
import sys


class MySecondGUI:
    def __init__(self, master):
        if len(sys.argv) < 2:
            self.name = "default"
        else:
            self.name = sys.argv[1]

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
        str_audio_name = self.name + "_combined.wav"
        open(str_audio_name, "w")
        os.remove(str_audio_name)
        open(str_audio_name, "w")
        text = self.text.get("1.0", 'end')
        user_text = map(lambda c: c, text)
        combined = AudioSegment.from_file(self.name + "_" + user_text[0] + ".wav")
        combined.export(str_audio_name, format='wav')
        user_text.pop(0)
        for number in user_text:
            if number == '\n' or number == ' ':
                continue
            sound1 = AudioSegment.from_file(str_audio_name)
            sound2 = AudioSegment.from_file(self.name + "_" + number + ".wav")
            combined = sound1 + sound2
            combined.export(str_audio_name, format='wav')
        self.pin = subprocess.call("python voice_acting.py " + str_audio_name, shell=True)



root = Tk()
my_gui = MySecondGUI(root)
root.geometry('600x130+200+100')

root.mainloop()
