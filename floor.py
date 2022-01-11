import tkinter as tk
from tkinter import StringVar, font
from tkinter.constants import CENTER, Y


#funkcia na vykreslenie kruhov figurok
def create_circle(x, y, r, canvasName, **kwargs): #center coordinates, radius
    x0,y0,x1,y1 = x - r, y - r, x + r ,y + r
    return canvasName.create_oval(x0, y0, x1, y1, **kwargs)

#funkcia na vykreslenie pozicie figurok
#cyklus na vykreslenie sachovnice
def create_figures(a):
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
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 5:
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="red")
            elif a[i][j] == 7:
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="white")

#funkcia na oznacenie stlpcov a riadkov
def text():
    list = ['A','B','C','D','E','F','G','H','1','2','3','4','5','6','7','8']
    for i in range(8):
        x = 120+i*80
        canvas.create_text(40,x,fill="black",font="Times 40",text="".join(list[i+8]))
        canvas.create_text(x,40,fill="black",font="Times 40",text="".join(list[i]))


def hrac(hrac):
    canvas.create_text(975, 100, text="Hráč č." + str(hrac) + "zadajte svoj ťah",font="Times 15", width=225, fill="black")
    a_text= canvas.create_text(840, 200, text="Zadajte pozíciu figurky, ktorou sa chcete posunúť:",font="Times 12", width=170, fill="black")
    b_text = canvas.create_text(1100, 200, text="Zadajte pozíciu, kam sa chcete dostať:",font="Times 12", width=170, fill="black")
    a_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER, textvariable= aentry).place(x=775,y=235,width=100, height=100)
    b_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER, textvariable= bentry).place(x=1050,y=235,width=100, height=100)

'''
def prevodY(hodnoty):
    y = hodnoty[0][0]
    if y == '1': return 0 
    elif y == '2': return 1
    elif y == '3': return 2
    elif y == '4': return 3
    elif y == '5': return 4
    elif y == '6': return 5
    elif y == '7': return 6
    elif y == '8': return 7
    print(y)

def prevodX(hodnoty):
    x = hodnoty[0][1]
    if x == 'A': return 0
    elif x=='B': return 1
    elif x=='C': return 2
    elif x=='D': return 3
    elif x=='E': return 4
    elif x=='F': return 5
    elif x=='G': return 6
    elif x=='H': return 7
    print(x)

def getorigin(eventorigin):
    global x,y
    x = eventorigin.x
    y = eventorigin.y
    print(x,y)

okno.bind("<Button 1>", getorigin)
'''
def spracuj():
    ae = aentry.get()
    be = bentry.get()
    hodnoty.append(list(ae))
    hodnoty.append(list(be))
    aentry.set(' ')
    bentry.set(' ')
    print(hodnoty)

velkost = 80
okno = tk.Tk()
canvas = tk.Canvas(okno, width = 1220, height = 720, bg='#c48354')
canvas.pack()

aentry = tk.StringVar()
bentry = tk.StringVar()


tk.Button(text="CONFIRM", bd='10', command= spracuj).place(x=912, y=370,width=100, height=50)

with open("zoznam_zoznamov.txt", "r") as reader:
    subor = reader.read().split()

a = []
for i in range(8):
    pom = []
    for j in range(8):
        pom.append(int(subor[i*8+j]))
    a.append(pom)



hodnoty = []
create_figures(a)
text()
hrac(1)


okno.mainloop()