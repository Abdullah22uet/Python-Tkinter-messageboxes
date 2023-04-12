import tkinter
from tkinter import *
from tkinter import messagebox
def btn1_is_click():
    messagebox.showinfo("Instructions","By using this button you can login to facebook")
def btn2_is_click():
    messagebox.showerror("Error","Error is occured.First reslolve this issue to move forward")
def btn3_is_click():
    messagebox.showwarning("Warning","Don't click this button")
root = tkinter.Tk( )
root.title("Practice of Tkinter")
root.configure(background="#74a7f7")
root.geometry("800x500")
btn1 = Button(root,
       text="Login to facebook",
       width=15,
       height=3,
       bg="#000000",
       fg="#ffffff",
       command = btn1_is_click,).grid(row=0,column=0)
btn2 = Button(root,text="Click me",bg="#5239e3",fg="#ddebe0",width=15,height=3,command=btn2_is_click)
btn2.grid(row=1,column=0)
btn3 = Button(root,text="Click me",bg="#32a852",fg="#ddebe0",width=15,height=3,command=btn3_is_click)
btn3.grid(row=2,column=0)
root.mainloop()


