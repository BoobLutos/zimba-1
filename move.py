# Tkinter animate via canvas.move(obj, xAmount, yAmount)
import tkinter as tk
import time
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# canvas.create_rectangle(x0, y0, x1, y1, option, ... )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
rc1 = canvas.create_rectangle(20, 260, 120, 360, outline='white', fill='blue')
rc2 = canvas.create_rectangle(20, 10, 120, 110, outline='white', fill='red')
y = x = 5
for loops in range(6):
    #time.sleep(0.025)
    time.sleep(1)
    canvas.move(rc1, x, -y)
    canvas.move(rc2, x, y)
    canvas.update()
root.mainloop()