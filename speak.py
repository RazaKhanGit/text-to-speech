from tkinter import *
import pyttsx3

root = Tk()
root.title("Raza")
root.geometry("800x500")
def talk():
    engine = pyttsx3.init()
    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0, END)

entry = Entry(root, font=("Helvetica", 28))
entry.pack(pady = 20)
button = Button(root, text="Speak", command=talk)
button.pack(pady = 20)
root.mainloop()