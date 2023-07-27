import pyshorteners as py
from tkinter import *

win = Tk()
win.title("URL shortener")
win.geometry("400x270")
win.config(bg = "black")

def shortener():
    url = e1.get()
    if len(url) == 0:
        short = "You did not entered a link"
        e2.config(bg="yellow")
        e2.delete(0,END)
        e2.insert(END,short)
    else:
        try:
            short = py.Shortener().tinyurl.short(url)
        except py.exceptions.ShorteningErrorException as p:
            short = "This url cannot be shortened further"
        e2.config(bg="yellow")
        e2.delete(0,END)
        e2.insert(END,short)

l1 = Label(win,text="Enter Your URL link",font="impack 15 bold",bg="light blue",fg="purple",highlightthickness=3)
l1.config(highlightbackground="blue",highlightcolor="blue")
l1.pack(fill="x",padx=20,pady=(20,0))

e1 =Entry(win,font="10",width=40,highlightthickness=3,bg="light blue")
e1.config(highlightbackground="blue",highlightcolor="blue")
e1.pack(pady=30,padx=20)

b1 = Button(win,text="Submit",font="impack 12 bold",bg="yellow",fg ="purple",width=12,command=shortener)
b1.pack()

e2 = Entry(win,font="impack 12",bg= "black",width=24,bd=0,fg="green",justify=CENTER)
e2.pack(pady=27)
mainloop()
