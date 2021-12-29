import tkinter as tk

def create_circle(x, y, r, canvasName, **kwargs): #center coordinates, radius
    x0,y0,x1,y1 = x - r, y - r, x + r ,y + r
    return canvasName.create_oval(x0, y0, x1, y1, **kwargs)

def create_figures(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 5:
                create_circle(j * 80 +40, i * 80 +40, 30, canvas, fill="red")
            elif a[i][j] == 7:
                create_circle(j * 80 +40, i * 80 +40, 30, canvas, fill="white")

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
        
with open("nacitanie3.txt", "r") as reader:
    subor = reader.read().split()
    
a = []
for i in range(8):
    pom = []
    for j in range(8):
        pom.append(int(subor[i*8+j]))
    a.append(pom)
print(a)

create_figures(a)
okno.mainloop()