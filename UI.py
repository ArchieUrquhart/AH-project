import re
from tkinter import *


#function to validate username - FR 2.2
def valid_name(username):
    #check the length of username and regex to check if there any special characters
    if len(username) > 15 or len(username) < 4 or re.search("\W",username):
        return False
    else:
        return True

#return username when button pressed
def get_input(root, inputtxt, label):
    global username
    input = inputtxt.get("1.0", "end-1c")
    if valid_name(input):
        root.destroy()
        username = input
    else:
        label.configure(text="Please re-enter your username")

# FR 2.1
def get_username():
    global username
    username = ""

    root = Tk()
    root.title("Worm")

    prompt = Label(text="Please enter your username")
    inputtxt = Text(root, height=1,width=20,padx=20,pady=10)
    button = Button(root, height=2,width=8,text="Play",command=lambda: get_input(root,inputtxt,prompt))

    prompt.grid(row=0,column=0)
    inputtxt.grid(row=1, column=0)
    button.grid(row=1, column=1)


    mainloop()

    return username

    return username

