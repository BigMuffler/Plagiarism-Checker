from tkinter import *
from tkinter import filedialog
import nltk

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
    filename = filedialog.askopenfilename(initialdir = "/C",title = "Browse Files" , filetypes = (("pdf files", "*.pdf"),("all files","*.*")))
    my_label = Label(root, text=filename)
    my_label.pack()
    
          
btn = Button(root, text = "Browse Files", command = Browse)
btn.pack()


root.mainloop()


