from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
root=Tk()
root.title('Learn to code')
root.iconbitmap('C:\gui\win.ico')
root.geometry("400x200")
def graph():
    house_price=np.random.normal(200000, 25000, 5000)
    plt.polar(house_price)
    plt.show()
btn=Button(root,text='Make Graph',command=graph).pack()
root.mainloop()