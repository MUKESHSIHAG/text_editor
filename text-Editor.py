#import modulefrom 
from tkinter import * 
import tkFileDialog

from tkinter import *
import tkinter.tkFileDialog

root = Tk('Text Editor')
text = Text(root)
text.grid()

#saving the text
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkFiledialog.asksavefilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close

button= Button(root, text="Save", command=saveas)
button.grid()
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
command=FontHelvetica) 

root.mainloop()