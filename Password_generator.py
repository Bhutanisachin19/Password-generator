
import random
import string

#for gui
from tkinter import *


def generate_passwrd():
    #empty list
    password=[]
    for i in range(0,5):
        #5 times ie 15 characters

        #randomly selecting a letter using string predefined package
        alphabet = random.choice(string.ascii_letters)

        #print(type(alphabet))
        
        #for symbols
        symbol = random.choice(string.punctuation)
        #print(type(symbol))
        
        #for numbers
        numbers = random.choice(string.digits)
        #print(type(numbers))
        
        #add all together or append
        password.append(alphabet)
        password.append(symbol)
        password.append(numbers)
    
    #create string of above created password
    y="".join(str(x)for x in password)
    #storing password on label
    lbl.config(text=y)




#gui
root = Tk()

root.title("Password Generator")
#height and width
root.geometry("350x300")

#button
btn = Button(root,text="Generate Password", command=generate_passwrd)
btn.grid(row=2,column=2)

#where password will be displayed
lbl=Label(root,font=("times",15,"bold"))
lbl.grid(row=4,column=2)

#close main loop
root.mainloop()

