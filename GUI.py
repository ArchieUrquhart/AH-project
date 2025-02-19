import re
from tkinter import *


#function to validate username
def valid_name(username):
    #check the length of username and regex to check if there any special characters
    if len(username) > 20 or len(username) < 4 or re.search("\W",username):
        return False
    else:
        return True

def Take_input(root, inputtxt, label):
    input = inputtxt.get("1.0", "end-1c")
    if valid_name(input):
        root.destroy()
        username = input
    else:
        label.configure(text="Please re-enter your username")


def get_username():
    username = ""

    root = Tk()
    root.title("Worm")

    label = Label(text="Please enter your username")
    inputtxt = Text(root, height=1,width=20,padx=20,pady=10)
    button = Button(root, height=2,width=8,text="Play",command=lambda: Take_input(root,inputtxt,label))

    label.grid(row=0,column=0)
    inputtxt.grid(row=1, column=0)
    button.grid(row=1, column=1)



    mainloop()

    return username
