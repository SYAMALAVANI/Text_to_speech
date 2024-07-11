from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

def speak_text():
  text = entry.get()
  speech = gTTS(text=text, lang='en', slow=False)
  speech.save("speech.mp3")
  os.system("start speech.mp3")

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button  = Button(text="start", command=speak_text )
canvas.create_window(200, 250, window=button)

root.mainloop()