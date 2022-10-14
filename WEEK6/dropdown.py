from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Learn to code')
root.iconbitmap('C:\gui\win.ico')
root.geometry("400x400")
def show():
    my_label=Label(root,text=clicked.get()).pack()
options=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
clicked=StringVar()
clicked.set(options[0])
drop=OptionMenu(root,clicked,*options)
drop.pack()
btn=Button(root,text='Show selection',command=show).pack()
root.mainloop()