from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Learn to code')
root.iconbitmap('C:\gui\win.ico')
root.geometry("400x400")
def show():
    my_label=Label(root,text=var.get()).pack()
var=StringVar()
c =Checkbutton(root, text="Would you like to SuperSize your order? Check Here!", variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()
btn=Button(root,text='Click Me',command=show).pack()
root.mainloop()