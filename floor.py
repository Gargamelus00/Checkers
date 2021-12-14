import tkinter as tk

velkost = 80
okno = tk.Tk()
canvas = tk.Canvas(okno, width = 640, height = 640)
canvas.pack()
color = 'white'

for y in range(8):
    for x in range(8):
        x1 = x*velkost
        y1 = y*velkost
        x2 = x1 + velkost
        y2 = y1 + velkost
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:
            color = 'white'
    if color == 'white':
        color = 'black'
    else:
        color = 'white'
        
okno.mainloop()