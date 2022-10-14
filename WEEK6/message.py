from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title('Learn to code')
root.iconbitmap('C:\gui\win.ico')
def popup():
    response=messagebox.showinfo("This is my popup!","Hello world")
#     Label(root,text=response).pack()
    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!!").pack()
Button(root,text='POPUP',command=popup).pack()
root.mainloop()