from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title('Digital Clock')
def get_time():
    timeVar = time.strftime('%H:%M:%S, %d.%m.%y')
    clock.config(text=timeVar)
    clock.after(200, get_time)

clock = Label(master, font = (calibri, 100), bg = 'black', fg = 'blue')
clock.pack()

get_time()

master.mainloop()
