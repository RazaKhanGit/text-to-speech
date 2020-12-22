from tkinter import * #import tkinter for GUI
from tkinter import filedialog #import filedialog to browse files on local system
import pyttsx3 #text to speech engine
import requests #to connect with the website
from bs4 import BeautifulSoup #scraping the html
import time #to keep time of functions

root = Tk()
root.title("Text-to-speech")
root.geometry("500x500")

fToRead = "" #creating a global variable
def browseFiles(): 
   
    global fToRead #using the global variable
    f = filedialog.askopenfilename(initialdir = "/", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    labelFile.configure(text="File Opened: "+f)
    fToRead = f

def talk():
    engine = pyttsx3.init()

    s = "Enter the sentence or browse files."
    if(fToRead != ""): #when no file is chosen don't run
        f = open(fToRead, "r")
        s = f.read()
    elif(entry.get() != ""): #when noting is typed don't run
        s = entry.get()
          
    engine.say(s) #speak
    engine.runAndWait()
    entry.delete(0, END) #remove the typed sentence

def readNews():      
    url='http://lite.cnn.com/en' #the news site to read from
     
    resp=requests.get(url) #open with GET method 

    if resp.status_code==200: #if connected
        engine = pyttsx3.init()
        engine.say("Successfully connected to CNN lite") 
        engine.say("The news are as follow") 
        soup=BeautifulSoup(resp.text,'html.parser') #the html-parser 

        l=soup.find("ul") #ul is the list which contains all the news headlines   
        start = time.time()
        for i in l.findAll("a"): #print only the text part of the <a> tag
            engine.say(i.text)
            engine.runAndWait()
            end = time.time()
            if end - start >= 30: #when 30sec passes break the loop
                engine.say("That's all for today, hasta la vista")
                engine.runAndWait()
                break

            

    else: 
        engine.say("Error")
        engine.runAndWait()  
 

entry = Entry(root, font=("Helvetica", 28)) #take input from the user
entry.pack(pady = 20) 

button = Button(root, text="Speak", command=talk) #button to speak
button.pack(pady = 20)

buttonExplore = Button(root, text = "Browse Files", command = browseFiles) #button to browse file
buttonExplore.pack(pady = 20)

buttonExplore = Button(root, text = "Get latest News", command = readNews) #button to read news headlines
buttonExplore.pack(pady = 20)

labelFile = Label(root, text = "File", width = 100, height = 4, fg = "blue") #display chosen file
labelFile.pack(pady = 20)



root.mainloop()