from tkinter import * #import tkinter for GUI
from tkinter import filedialog #import filedialog to browse files on local system
import pyttsx3 #text to speech engine

root = Tk()
root.title("Text-to-speech")
root.geometry("500x500")

fToRead = ""
def browseFiles(): 
   
    global fToRead
    f = filedialog.askopenfilename(initialdir = "/", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    labelFile.configure(text="File Opened: "+f)
    fToRead = f

def talk():
    engine = pyttsx3.init()
    s = "Enter the sentence or browse files."
    if(fToRead != ""):
        f = open(fToRead, "r")
        s = f.read()
    elif(entry.get() != ""):
        s = entry.get()
          
    engine.say(s)
    engine.runAndWait()
    entry.delete(0, END)
    
 

entry = Entry(root, font=("Helvetica", 28)) #take input from the user
entry.pack(pady = 20) 

button = Button(root, text="Speak", command=talk) #button to speak
button.pack(pady = 20)

buttonExplore = Button(root, text = "Browse Files", command = browseFiles) #button to browse file
buttonExplore.pack(pady = 20)

labelFile = Label(root, text = "File", width = 100, height = 4, fg = "blue") #display chosen file
labelFile.pack(pady = 20)

 


root.mainloop()
