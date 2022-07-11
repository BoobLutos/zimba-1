#x' = xcos@ -ysin@
#y' = ycos@ +xsin@


import tkinter
import math
import time
from tkinter import BOTH
from datetime import datetime
#from playsound import playsound
import winsound

top = tkinter.Tk()
C = tkinter.Canvas(top, bg = "white", height = 700, width = 900)
C.pack(fill=BOTH, expand=1)


n = 60
nn = 3600
nnn = 216000
r = 300
fontsize = 40

xposition = 400
yposition = 400
center = C.create_oval(xposition -7, yposition -7, xposition +7, yposition +7, fill="black")


def drawdots():
    for i in range(n):
        x1Points = (xposition+200*math.sin(2*math.pi*i/n));
        y1Points = (yposition-200*math.cos(2*math.pi*i/n));
        #print(x1Points,y1Points)
        
        if(i%5==0):
            circle = C.create_oval(x1Points -5, y1Points -5, x1Points +5, y1Points +5, fill="black")
        else:
            circle = C.create_oval(x1Points -2, y1Points -2, x1Points +2, y1Points +2, fill="black")




def drawhands():    
        time.sleep(0.1)
        now = datetime.now()

        current_time = now.strftime("%I:%M:%S %p") # capture time in 12 hour format indicating PM/AM
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_second = now.strftime("%S")
        seconds = float(current_second)
        minutes = float(current_minute)
        hours = float(current_hour)
        print("Current Time =", current_time)
        
        #calculate angles clockwise from the upper vertical position
        x2Points = (xposition+180*math.sin(2*math.pi*seconds/n));
        y2Points = (yposition-180*math.cos(2*math.pi*seconds/n));
        
        x3Points = (xposition+150*math.sin((2*math.pi*seconds/nn)+(2*math.pi*minutes/n)));
        y3Points = (yposition-150*math.cos((2*math.pi*seconds/nn)+(2*math.pi*minutes/n)));
        
        x4Points = (xposition+120*math.sin((2*math.pi*5*minutes/nn)+(2*math.pi*5*hours/n)));
        y4Points = (yposition-120*math.cos((2*math.pi*5*minutes/nn)+(2*math.pi*5*hours/n)));  
    
        hourhand = C.create_line(xposition,yposition,x4Points,y4Points, width = 10)
        minutehand = C.create_line(xposition,yposition,x3Points,y3Points, width = 5)
        secondhand = C.create_line(xposition,yposition,x2Points,y2Points, width = 2, fill = 'red')
        
        
        timewidget = C.create_text(400,400, font=("Purisa", fontsize),text=current_time, fill = 'grey')
        
        if(1==1):
            C.update()
            C.delete(hourhand)
            C.delete(minutehand)
            C.delete(secondhand)
            C.delete(timewidget)
            #winsound.Beep(400, 300)
        else:
            pass


drawdots()
while True:
    drawhands()
    



top.mainloop()
