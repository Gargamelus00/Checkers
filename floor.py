import tkinter as tk
from tkinter import font
from tkinter.constants import ANCHOR, CENTER

def create_circle(x, y, r, canvasName, **kwargs): #center coordinates, radius
    x0,y0,x1,y1 = x - r, y - r, x + r ,y + r
    return canvasName.create_oval(x0, y0, x1, y1, **kwargs)

def create_figures(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 5:
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="red")
            elif a[i][j] == 7:
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="white")

def text():
    list = ['A','B','C','D','E','F','G','H','1','2','3','4','5','6','7','8']
    for i in range(8):
        x = 120+i*80
        canvas.create_text(40,x,fill="black",font="Times 40",text="".join(list[i+8]))
        canvas.create_text(x,40,fill="black",font="Times 40",text="".join(list[i]))
    canvas.update

def hrac1():
    canvas.create_text(975, 100, text="Hráč č.1 zadajte svoj ťah",font="Times 15", width=225, fill="black")                                
    a_text= canvas.create_text(840, 200, text="Zadajte pozíciu figurky, ktorou sa chcete posunúť:",font="Times 12", width=170, fill="black")  
    a_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER).place(x=775,y=235,width=100, height=100,)
    b_text = canvas.create_text(1100, 200, text="Zadajte pozíciu, kam sa chcete dostať:",font="Times 12", width=170, fill="black")   
    b_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER).place(x=1050,y=235,width=100, height=100,) 

def hrac2():
    canvas.create_text(975, 100, text="Hráč č.2 zadajte svoj ťah",font="Times 15", width=225, fill="black")                                
    a_text= canvas.create_text(840, 200, text="Zadajte pozíciu figurky, ktorou sa chcete posunúť:",font="Times 12", width=170, fill="black")  
    a_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER).place(x=775,y=235,width=100, height=100,)
    b_text = canvas.create_text(1100, 200, text="Zadajte pozíciu, kam sa chcete dostať:",font="Times 12", width=170, fill="black")   
    b_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER).place(x=1050,y=235,width=100, height=100,) 
    

velkost = 80
okno = tk.Tk()       
canvas = tk.Canvas(okno, width = 1220, height = 720)  
canvas.pack()
color = 'white'

for y in range(8):
    for x in range(8):
        x1 = 80+x*velkost
        y1 = 80+y*velkost
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

create_figures(a)
text()
hrac1()
hrac2()
okno.mainloop()