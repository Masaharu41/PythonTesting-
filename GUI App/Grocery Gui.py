# Import Tkinter Gui modules and make proper reference
#
import tkinter
from tkinter import *
# root is the primary window variable which is spawned by Tkinter
root = Tk()
# spawns a title for the window and sets dimensions 
root.title("Welcome Owen")
# Set Geometry(width x height)
root.geometry('500x400')
#label for the root window
lbl = Label(root, text = "have fun friends")
lbl.grid()
# Define behaviour when the button is clicked
def clicked():
    lbl.configure(text="Why Hello There!")
#
#defines the button, text, and the color of the text
btn = Button(root, text="click here",
            fg = "red", command=clicked)
#Configures how many buttons will be spawned
btn.grid(column=1, row=0)
#
#
root.mainloop()