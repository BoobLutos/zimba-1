#import tkinter
from tkinter import *
import re
#import time
#from datetime import datetime

top = Tk()

def helloCallBack():
    messagebox.showinfo("Muriyo","gyetuli")
    
def ins7():
    #Display.delete(0, END)
    Display.insert("end", 7)
    
def ins8():
    #Display.delete(0, END)
    Display.insert("end", 8)
    
def ins9():
    #Display.delete(0, END)
    Display.insert("end", 9)

def ins4():
    #Display.delete(0, END)
    Display.insert("end", 4)
    
def ins5():
    #Display.delete(0, END)
    Display.insert("end", 5)
    
def ins6():
    #Display.delete(0, END)
    Display.insert("end", 6)

def ins1():
    #Display.delete(0, END)
    Display.insert("end", 1)
    
def ins2():
    #Display.delete(0, END)
    Display.insert("end", 2)
    
def ins3():
    #Display.delete(0, END)
    Display.insert("end", 3)

def ins0():
    #Display.delete(0, END)
    Display.insert("end", 0)

def insplus():
    #Display.delete(0, END)
    Display.insert("end", '+')


def insminus():
    #Display.delete(0, END)
    Display.insert("end", '-')
    
def insdiv():
    #Display.delete(0, END)
    Display.insert("end", '/')


def insmult():
    #Display.delete(0, END)
    Display.insert("end", 'x')


def insequals():
    #Display.delete(0, END)
    Display.insert("end", '=')
    
def inspoint():
    #Display.delete(0, END)
    Display.insert("end", '.')
    
def inspos_neg():
    #Display.delete(0, END)
    Display.insert("end", '=')

def insclear():
    Display.delete(0, END)
    

def fetch_result():
    #print (Display.get())[0:2]
    result=Display.get()
    ressanitize =re.sub('x','*', result)
    res =re.search(r"^\d+(?:[-+*/]\d+)+", ressanitize) # we use regex to enforce some input validation
    #numpos = result.rsplit('+') 
    #print(result)
    #add = int(numpos[0]) + int(numpos[1])
    #add = numpos[0] + numpos[1]
    duh = eval(res.group())
    print(duh)
    #print (result)[0:2]

Display = Entry(top, width=52, justify=RIGHT)
#Display = Entry(top, width=57, justify=RIGHT)   
#Display = Text(top, width=39, height=2)
Display.grid(row=0, columnspan=5)    
    
    
B7 = Button(top, text = "7", width=10, height=2, command = ins7); B7.grid(row=1,column=0)
B8 = Button(top, text = "8", width=10, height=2, command = ins8); B8.grid(row=1,column=1)
B9 = Button(top, text = "9", width=10, height=2, command = ins9); B9.grid(row=1,column=2)

B4 = Button(top, text = "4", width=10, height=2, command = ins4); B4.grid(row=2,column=0)
B5 = Button(top, text = "5", width=10, height=2, command = ins5); B5.grid(row=2,column=1)
B6 = Button(top, text = "6", width=10, height=2, command = ins6); B6.grid(row=2,column=2)


B1 = Button(top, text = "1", width=10, height=2, command = ins1); B1.grid(row=3,column=0)
B2 = Button(top, text = "2", width=10, height=2, command = ins2); B2.grid(row=3,column=1)
B3 = Button(top, text = "3", width=10, height=2, command = ins3); B3.grid(row=3,column=2)

B0 = Button(top, text = "0", width=10, height=2, command = ins0); B0.grid(row=4,column=1)
Ba = Button(top, text = "+/-", width=10, height=2, command = inspos_neg); Ba.grid(row=4,column=0)
Bb = Button(top, text = ".", width=10, height=2, command = inspoint); Bb.grid(row=4,column=2)
Bc = Button(top, text = "x", width=10, height=2, command = insmult); Bc.grid(row=1,column=3)
Bd = Button(top, text = "-", width=10, height=2, command = insminus); Bd.grid(row=2,column=3)
Be = Button(top, text = "+", width=10, height=2, command = insplus); Be.grid(row=3,column=3)
Bf = Button(top, text = "=", width=10, height=2, command = fetch_result); Bf.grid(row=4,column=3)


Bg = Button(top, text = "%", width=10, height=2, command = inspos_neg); Bg.grid(row=5,column=0)
Bh = Button(top, text = "1/x", width=10, height=2, command = inspoint); Bh.grid(row=6,column=0)
Bi = Button(top, text = "x2", width=10, height=2, command = insmult); Bi.grid(row=6,column=1)
Bj = Button(top, text = "sqrt", width=10, height=2, command = insminus); Bj.grid(row=6,column=2)
Bk = Button(top, text = "/", width=10, height=2, command = insdiv); Bk.grid(row=6,column=3)
Bl = Button(top, text = "<<-", width=10, height=2, command = insequals); Bl.grid(row=5,column=3)
Bm = Button(top, text = "CE", width=10, height=2, command = insplus); Bm.grid(row=5,column=1)
Bn = Button(top, text = "C", width=10, height=2, command = insclear); Bn.grid(row=5,column=2)


#C = Canvas(top, bg = "white", height = 700, width = 900)
#C.pack(fill=BOTH, expand=1)

#C.create_text(100,100, text="trying text")
#C.create_text(400,400, text=current_time)
coord = 400, 500, 410, 510
#circle = C.create_oval(coord, fill="black")
#arc = C.create_arc(coord, start=0, extent=150, fill="red")



top.mainloop()