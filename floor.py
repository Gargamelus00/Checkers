import tkinter as tk
from tkinter.constants import W

def create_circle(x, y, r, canvasName, **kwargs): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, **kwargs)





def create_figure():
    create_circle(120,40, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(280,40, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(440,40, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(600,40, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(40, 120, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(200,120, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(360,120, 30, canvas,  fill="black", outline="white", width=5)
    create_circle(520,120, 30, canvas,  fill="black", outline="white", width=5)

    create_circle(40, 600, 30, canvas,  fill="white")
    create_circle(200, 600, 30, canvas,  fill="white")
    create_circle(360, 600, 30, canvas,  fill="white")
    create_circle(520, 600, 30, canvas,  fill="white")
    create_circle(120,520, 30, canvas,  fill="white")
    create_circle(280,520, 30, canvas,  fill="white")
    create_circle(440,520, 30, canvas,  fill="white")
    create_circle(600,520, 30, canvas,  fill="white")

velkost = 80
okno = tk.Tk()
canvas = tk.Canvas(okno, width = 640, height = 640)
canvas.pack()
color = 'red'

for y in range(8):
    for x in range(8):
        x1 = x*velkost
        y1 = y*velkost
        x2 = x1 + velkost
        y2 = y1 + velkost
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'red':
            color = 'black'
        else:
            color = 'red'
    if color == 'red':
        color = 'black'
    else:
        color = 'red'
        
create_figure()
okno.mainloop()