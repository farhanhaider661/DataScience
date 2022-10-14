from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Learn To Code')
root.iconbitmap('C:\gui\win.ico')
myImg=ImageTk.PhotoImage(Image.open("images/aspen.png"))
myLabel=Label(image=myImg)
myLabel.pack()
btn_quit=Button(root,text='Exit',command=root.quit)
btn_quit.pack()
root.mainloop()