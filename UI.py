import re
from tkinter import *


#function to validate username
def valid_name(username):
    #check the length of username and regex to check if there any special characters
    if len(username) > 20 or len(username) < 4 or re.search("\W",username):
        return False
    else:
        return True

#function that will run wehn button is pressed
def take_input(root, inputtxt, label):
    #get username from text box
    input = inputtxt.get("1.0", "end-1c")
    #validate name
    if valid_name(input):
        #if valid name exit the GUI and set username to output
        root.destroy()
        username = input
    else:
        #if invalid change prompt to notify user that the username is invalid
        label.configure(text="Please re-enter your username")


#function to retrieve username
def get_username():
    username = ""

    #make GUI window
    root = Tk()
    root.title("Worm")

    #prompt for username
    label = Label(text="Please enter your username")
    #textbox for username input
    inputtxt = Text(root, height=1,width=20,padx=20,pady=10)
    #button to validate name and change username
    button = Button(root, height=2,width=8,text="Play",command=lambda: Take_input(root,inputtxt,label))

    #draw elements in the correct positions
    label.grid(row=0,column=0)
    inputtxt.grid(row=1, column=0)
    button.grid(row=1, column=1)


    mainloop()

    return username
