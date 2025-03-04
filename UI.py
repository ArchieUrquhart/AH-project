import re
from tkinter import *


#function to validate username
def valid_name(username):
    #check the length of username and regex to check if there any special characters
    if len(username) > 15 or len(username) < 4 or re.search("\W",username):
        return False
    else:
        return True

#retrives the username from the text box
def get_input(root, inputtxt):
    global username
    input = inputtxt.get("1.0", "end-1c")
    root.destroy()
    username = input

#gets username from user with a variable prompt
def get_username(message):
    global username
    username = ""

    #sets up window
    root = Tk()
    root.title("Worm")

    #creates all window features
    prompt = Label(text=message)
    inputtxt = Text(root, height=1,width=20,padx=20,pady=10)
    button = Button(root, height=2,width=8,text="Play",command=lambda: get_input(root,inputtxt))

    #positioning of features
    prompt.grid(row=0,column=0)
    inputtxt.grid(row=1, column=0)
    button.grid(row=1, column=1)


    mainloop()

    return username
