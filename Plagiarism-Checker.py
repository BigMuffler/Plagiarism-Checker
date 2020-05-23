from tkinter import *
from tkinter import filedialog
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
from googlesearch import search

#Will work only for text files, so files uploaded must be .txt exstension
#Specify to check Essay or Code 
#EorC = input("Would you like to check a code snippet or essay for plagiarism?")
#Create GUI for Interface
root = Tk()
root.title('Plagiarsm Checker')

frame = Frame(root)
frame.pack()
label1 = Label(master=frame,text="Plagiarism Checker")
label1.pack()

def Browse():
    filename = filedialog.askopenfilename(initialdir = "/C",title = "Browse Files" , filetypes = (("txt files", "*.txt"),("all files","*.*")))
    #my_label = Label(root, text=filename)
    #my_label.pack()
    Check(filename)

def Check(path): #function for checking functionality 
    print (path)
    #tokenize and parsing a file
    file_content = open(path,encoding = "utf8").read()
    tokens = nltk.word_tokenize(file_content)
    #print (tokens)

    Selected = 10
    print (tokens[0:Selected])

    query = TreebankWordDetokenizer().detokenize(tokens[0:Selected])

    my_results_list = []
    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 10,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 10,    # Number of links to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                    ):
        my_results_list.append(i)
        print(i)


btn = Button(root, text = "Browse Files", command = Browse)
btn.pack()

root.mainloop()

