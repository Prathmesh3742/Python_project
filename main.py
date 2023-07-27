import pyshorteners as py
from tkinter import *
import webbrowser as wb

win = Tk()
win.title("URL shortener")
win.geometry("400x380")
win.config(bg = "black")
def nav():
    url = e2.get()
    if len(url) == 0 or url == "This url cannot be shortened further" or url == "You did not entered a link" or url == "Invalid url":
        l2.pack(fill="x",padx=20,pady=(20,0))
    else:
        wb.open(url= url)
        
def shortener():
    url = e1.get()
    l2.pack_forget()
    b2.pack_forget()
    if len(url) == 0:
        short = "You did not entered a link"
        e2.config(bg="yellow")
        e2.delete(0,END)
        e2.insert(END,short)
    else:
        try:
            short = py.Shortener().tinyurl.short(url)
        except py.exceptions.ShorteningErrorException:
            short = "This url cannot be shortened further"
        except py.exceptions.BadURLException :
            short = "Invalid url"
        e2.config(bg="yellow")
        e2.delete(0,END)
        e2.insert(END,short)
        b2.pack()

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

b2 = Button(win,text="Open Link",font="impack 12 bold",bg="yellow",fg ="purple",width=12,command=nav,bd=0)

l2 = Label(win,text="Link cannot be opened",font="impack 15",bg="red",fg="white")
mainloop()
