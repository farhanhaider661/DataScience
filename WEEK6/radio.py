from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code')
root.iconbitmap('C:\gui\win.ico')
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]
pizza = StringVar()
pizza.set("Pepperoni")
for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


btn = Button(root, text='choose pizza ', command=lambda: clicked(pizza.get()))
btn.pack()
r = IntVar()
r.set("2")
Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
btn2 = Button(root, text='choose option', command=lambda: clicked(r.get()))
btn2.pack()
root.mainloop()