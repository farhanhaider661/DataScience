from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
root.iconbitmap('C:\gui\win.ico')


def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap('C:\gui\win.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close window', command=top.destroy).pack()


btn = Button(root, text='open second window', command=open).pack()
root.mainloop()