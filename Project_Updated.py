# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:08:35 2019

@author: CHARAN

"""

from tkinter import *
import random as r
from tkinter import messagebox as message
def change():
    c.delete("all")
    h=list()
    global result
    for i in range(0,5):
        h.append(chr(r.randint(33,126)))

    colr=["black","purple","red","blue","green","gray","violet","pink","orange"]
    fonts=["Verdana","Arial","Papyrus","Calibri","Georgia"]

    t1=c.create_text(40+r.randint(0,10),40+r.randint(0,10),text=h[0],font=fonts[r.randint(0,4)]+" 28 bold",fill=colr[r.randint(0,8)])
    t2=c.create_text(80+r.randint(0,10),40+r.randint(0,10),text=h[1],font=fonts[r.randint(0,4)]+" 28 bold",fill=colr[r.randint(0,8)])
    t3=c.create_text(120+r.randint(0,10),40+r.randint(0,10),text=h[2],font=fonts[r.randint(0,4)]+" 28 bold",fill=colr[r.randint(0,8)])
    t4=c.create_text(160+r.randint(0,10),40+r.randint(0,10),text=h[3],font=fonts[r.randint(0,4)]+" 28 bold",fill=colr[r.randint(0,8)])
    t5=c.create_text(200+r.randint(0,10),40+r.randint(0,10),text=h[4],font=fonts[r.randint(0,4)]+" 28 bold",fill=colr[r.randint(0,8)])
    
    for i in range(0,10):
        l=c.create_line(r.randint(5,295),r.randint(5,195),r.randint(5,295),r.randint(5,195),fill=colr[r.randint(0,8)],width=[r.randint(1,3)])
    result=''.join(h)
    
def results():
    a=entry1.get()
    if(a==result):
        message.showinfo('SUCCESS!','YOUR CAPTHCA HAS BEEN VALIDATD SUCCESSFULLY')
    else:
        message.showerror("ERROR!"," INVALID CAPTCHA OR PLEASE ENTER THE CAPTCHA PROVIDED")
    b=entry2.get()
    if (b):
        pass
    else:
        message.showerror("Error","Registration Number Required")
    if ((b) and (a==result)):
        screen=Toplevel(root)
        screen.geometry("300x450+550+100")
        screen.title("Login Page")
        
        label0= Label(screen, text="LOGIN SYSTEM", bg="white",fg="black")
        label1= Label(screen, text="Username  :",bg="yellow")
        label2= Label(screen, text="Password  :",bg="yellow")
        label3= Label(screen, text="Re-enter Password  :",bg="yellow")
        
        en1= Entry(screen)
        en2= Entry(screen)
        en3= Entry(screen)
        
        label0.grid(row=0,pady=20)
        label1.grid(row=1,pady=20)
        label2.grid(row=2,pady=20)
        label3.grid(row=3,pady=20)        
        en1.grid(row=1,  column=1)
        en2.grid(row=2,  column=1)
        en3.grid(row=3,  column=1)
        
        B = Button(screen, text="Submit" ,bg="red")
        B.grid(columnspan=4,pady=20)

        d= Button(screen, text="Main Page")
        d.grid(columnspan=5,pady=20)

def exits():
    root.destroy()
root=Tk()
root.geometry("500x390")
root.title("Password Reminder")
c=Canvas(width=250,height=100,bg="white")
c.place(x=120,y=70)
input_text=StringVar()
l1=Label(root,text = "Reg No.",bg="yellow",fg="black")
l1.place(x=70,y=20)

entry2=Entry(root,width=15,bd=1.5,font=("Georgia",15))
entry2.place(x=168,y=20)
l2=Label(root,text="Enter the CAPTCHA from above:")
l2.place(x=150,y=190)
entry1=Entry(root,textvariable=input_text,width=10,font=("Georgia",20))
entry1.place(x=150,y=220)
change=Button(root,text="GENERATE CAPTCHA",bd=3,padx=5,pady=5,font=("Verdana 1 bold",10),command=change,bg="yellow")
change.place(x=100,y=280)
sub=Button(root,text="SUBMIT",bg="lightgreen",bd=3,padx=15,pady=4,font=("Verdana 1 bold",10),command=results)
sub.place(x=290,y=280)
ex=Button(root,text="EXIT",bd=3,padx=5,pady=5,font=("Verdana 1 bold",10),command=exits,bg="Orange")
ex.place(x=220,y=335)
root.mainloop()
