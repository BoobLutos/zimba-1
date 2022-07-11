#import tkinter
from tkinter import *
import math
import re
#import time
#from datetime import datetime

top = Tk()

def helloCallBack():
    messagebox.showinfo("BASIC","CALCULATOR")
    
    
def insertnumber(z):
    
    regexp='{}'.format((Display2.get()))
    print([regexp]) # use square brackets to print hidden characters too
    substr="\r"
    
    
    if (Display2.get()=='0'):
        Display2.delete(0, END)
        Display2.insert("end", z)
        
    
    
    elif ((Display.get()).endswith('+ ') or (Display.get()).endswith('- ') or (Display.get()).endswith('/ ') or (Display.get()).endswith('x ')):
        
        if (substr in regexp): # if an operator has been appended, then clear the entry. Otherwise, just append digits
        
            Display2.delete(0, END)
            Display2.insert("end", z)
            
        else:
            Display2.insert("end", z)
    
            
    elif (substr in regexp):
    #elif re.search(substr, regexp): alternatively use the search function
        Display2.delete(0, END)
        Display.delete(0, END)
        Display2.insert("end", z) 
        print("found")
        
    else:
        Display2.insert("end", z)
        
        
def insoperator(y):
    #Display.delete(0, END)
    Display2value=Display2.get()
    Display.insert("end", Display2value)
    Display.insert("end", " ")
    Display.insert("end", y)
    Display.insert("end", " ")
    Display2.insert(END,'\r')

 

def insequals():
    Display2value=Display2.get()
    Display.insert("end", Display2value)
    #Display.delete(0, END)
    Display.insert("end", '=')
    
def inspoint():
    #Display.delete(0, END)
    Display2.insert("end", '.')
    
def inspos_neg():
    Display2value=Display2.get() # get value in display 2 and multiply it by -1
    Flipvalue=int(Display2value)*(-1)
    Display2.delete(0, END) # clear display 2 and replace it with flipped number
    Display2.insert('end',Flipvalue)
    Display2.insert('end'," ")
    
    
def square():
    m=int(Display2.get())
    mvalue="sqr("+str(m)+")"
    print(mvalue)
    n=m*m
    print(n)
    Display.delete(0, END)
    Display2.delete(0, END) 
    Display.insert('end', mvalue)
    Display2.insert('end', n)
    Display2.insert(END,'\r')
    
def sqrt():
    m=int(Display2.get())
    msqrt=math.sqrt(m)
    mvalue="\u221a("+str(m)+")"
      
    print(mvalue)
       
    Display.delete(0, END)
    Display2.delete(0, END) 
    Display.insert('end', mvalue)
    Display2.insert('end', msqrt)
    Display2.insert(END,'\r')
    
def invrt():
    m=int(Display2.get())
    mvalue="1/("+str(m)+")"
    print(mvalue)
    n=1/m
    print(n)
    Display.delete(0, END)
    Display2.delete(0, END) 
    Display.insert('end', mvalue)
    Display2.insert('end', n)
    Display2.insert(END,'\r')
 
def percnt():
    Display2value=float(Display2.get().replace("\r",""))
    Display2.delete(0, END)
    Display2.insert('end',Display2value/100); 
    Display2.insert(END,'\r') 

def insclear():
    Display.delete(0, END)
    Display2.delete(0, END)
    Display2.insert(END, 0)
    #Display2.insert('end'," ")
    
def insclear2():
    Display2.delete(0, END)
    Display2.insert(END, 0)
    
def insclearlast():
    Display2.delete(len(Display2.get())-1,END) # delete everything after the length of the string minus 1
  
def answer(k):
    Display2.delete(0,END)
    Display2.insert(0, k)   

def fetch_result():
    Display2value=Display2.get()
    Display.insert("end", Display2value) # copy value from display 2 into display1 and thereafter clear display2
    #Display.insert("end", " ")
    Display2.delete(0, END)
    
    
    result=Display.get() # get the string from display 1 and prepare it for computation
    ressanitize =re.sub('x','*', result)
    #res =re.search(r"^\d+(?:[-+*/]\d+)+", ressanitize) # we use regex to enforce some input validation
    res =re.search(r"^[+-]?([0-9]*[.])?[0-9]+\s(?:[-+*/]?\s[-]?([0-9]*[.])?[0-9]+)+", ressanitize)# we use regex to enforce some input validation
    print(res)
    
    duh = eval(res.group())
    #print(duh)
    #answer=Display2.insert(0,duh)
    Display2.insert(0,duh)
    Display2.insert(END,'\r')
    
    
   

Display = Entry(top, width=52, highlightthickness=0,borderwidth=0, justify=RIGHT)#also hide borders
Display2 = Entry(top, width=52, highlightthickness=0,borderwidth=0, justify=RIGHT)#also hide borders
Display2.insert(END, 0)
#Display2.insert(END, " ")

#place elements on the grid
Display.grid(row=0, columnspan=5)
Display2.grid(row=1, columnspan=5)   
    
    
B7 = Button(top, text = "7", width=10, height=2, command = lambda: insertnumber(7)); B7.grid(row=4,column=0) # use lambda to prevent the command from being executed before the button is clicked
B8 = Button(top, text = "8", width=10, height=2, command = lambda: insertnumber(8)); B8.grid(row=4,column=1)
B9 = Button(top, text = "9", width=10, height=2, command = lambda: insertnumber(9)); B9.grid(row=4,column=2)

B4 = Button(top, text = "4", width=10, height=2, command = lambda: insertnumber(4)); B4.grid(row=5,column=0)
B5 = Button(top, text = "5", width=10, height=2, command = lambda: insertnumber(5)); B5.grid(row=5,column=1)
B6 = Button(top, text = "6", width=10, height=2, command = lambda: insertnumber(6)); B6.grid(row=5,column=2)


B1 = Button(top, text = "1", width=10, height=2, command = lambda: insertnumber(1)); B1.grid(row=6,column=0)
B2 = Button(top, text = "2", width=10, height=2, command = lambda: insertnumber(2)); B2.grid(row=6,column=1)
B3 = Button(top, text = "3", width=10, height=2, command = lambda: insertnumber(3)); B3.grid(row=6,column=2)

B0 = Button(top, text = "0", width=10, height=2, command = lambda: insertnumber(0)); B0.grid(row=7,column=1)
Ba = Button(top, text = "+/-", width=10, height=2, command = inspos_neg); Ba.grid(row=7,column=0)
Bb = Button(top, text = ".", width=10, height=2, command = inspoint); Bb.grid(row=7,column=2)
Bc = Button(top, text = "x", width=10, height=2, command = lambda: insoperator('x')); Bc.grid(row=4,column=3)
Bd = Button(top, text = "-", width=10, height=2, command = lambda: insoperator('-')); Bd.grid(row=5,column=3)
Be = Button(top, text = "+", width=10, height=2, command = lambda: insoperator('+')); Be.grid(row=6,column=3)
Bf = Button(top, text = "=", width=10, height=2, command = fetch_result); Bf.grid(row=7,column=3)


Bg = Button(top, text = "%", width=10, height=2, command = percnt); Bg.grid(row=2,column=0)
Bh = Button(top, text = "1/x", width=10, height=2, command = invrt); Bh.grid(row=3,column=0)
Bi = Button(top, text = "x\u00b2", width=10, height=2, command = square); Bi.grid(row=3,column=1)
Bj = Button(top, text = "\u221a", width=10, height=2, command = sqrt); Bj.grid(row=3,column=2)# edit this command
Bk = Button(top, text = "\u00F7", width=10, height=2, command = lambda: insoperator('/')); Bk.grid(row=3,column=3)
Bl = Button(top, text = "<<-", width=10, height=2, command = insclearlast); Bl.grid(row=2,column=3)
Bm = Button(top, text = "CE", width=10, height=2, command = insclear2); Bm.grid(row=2,column=1) # edit this command
Bn = Button(top, text = "C", width=10, height=2, command = insclear); Bn.grid(row=2,column=2)



top.mainloop()
