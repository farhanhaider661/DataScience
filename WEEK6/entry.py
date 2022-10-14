from tkinter import *
root=Tk()
e=Entry(root,width=50,font=('Helvatica',24))
e.pack()
e.insert(0,"Enter your Name: ")
def myClick():
    hello="Hello "+ e.get()
    mylabel=Label(root,text=hello)
    e.delete(0,'end')
    mylabel.pack()
mybutton=Button(root,text="Enter your quote",command=myClick)
mybutton.pack()
root.mainloop()