from tkinter import *
root=Tk()
def myClick():
    mylabel=Label(root,text="I click the button!")
    mylabel.pack()
mybutton=Button(root,text='Click Me',command=myClick,fg="green")
mybutton.pack()
root.mainloop()