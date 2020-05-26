from tkinter import *
from tkinter import filedialog
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
from googlesearch import search
import webbrowser

#Will work only for text files, so files uploaded must be .txt exstension
#Create GUI for Interface
root = Tk()
root.title('Plagiarsm Checker')

frame = Frame(root)
frame.pack()
label1 = Label(master=frame,text="Plagiarism Checker")
l = Label(root, bg='white', width = 100, height = 5, text='Plagiarism Checker : Returns links to online documents that are the best match')
l.pack(anchor = W)

mylist = []

def Browse():
    filename = filedialog.askopenfilename(initialdir = "/C",title = "Browse Files" , filetypes = (("txt files", "*.txt"),("all files","*.*")))
    Tokenize(filename)

#Tokenize File for Search
def Tokenize(path): 
    #tokenize and parsing a file
    global tokens
    file_content = open(path,encoding = "utf8").read()
    tokens = nltk.word_tokenize(file_content)
    
def ShowChoice():
    print(v.get())

def GetResults():
    Number_of_Characters = v.get()
    Selected = Number_of_Characters
    print (tokens[0:Selected])
    query = TreebankWordDetokenizer().detokenize(tokens[0:Selected])
    global mylist
    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 10,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 10,    # Number of links to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                    ):
        mylist.append(i)
        label1 = Label(root,text=i,justify = LEFT,padx = 10 , fg = "blue", cursor="hand2")
        label1.pack()
        label1.bind("<Button-1>", callback)    

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

#Button to browse files
Label(root, 
         text="Browse for .txt file:",
         justify = LEFT,
         ).pack(anchor = W)

btn = Button(root, text = "Browse Files",  command = Browse)
btn.pack(anchor = W) 

#Buttons to select length of document to search
global v
v = IntVar()
v.set(1) 
Select_Number_of_Characters = [
    ("10", 10),
    ("50" , 50),
    ("100", 100),
    ("500", 500),
    ("Whole Document", 1000)
]
Label(root, 
         text="Choose the number of words you want to search:",
         justify = LEFT,
         pady = 10).pack(anchor = W)
for val, mode in Select_Number_of_Characters:
        Radiobutton(root, 
                  text=val,
                  padx = 10, 
                  variable=v, 
                  command=ShowChoice,
                  value=mode).pack(anchor = W)

#Button once clicked returns the search results
btn1 = Button(root, text = "GO", command = GetResults) 
btn1.pack( anchor = S, pady = 20)

root.mainloop()

