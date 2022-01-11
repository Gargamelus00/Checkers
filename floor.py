import tkinter as tk
from tkinter import font
from tkinter.constants import CENTER


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
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="yellow")
            if a[i][j] == 15:
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="red")
                create_circle(j * 80 +120, i * 80 +120, 15, canvas, fill="black")
            elif a[i][j] == 17:
                create_circle(j * 80 +120, i * 80 +120, 30, canvas, fill="yellow")
                create_circle(j * 80 +120, i * 80 +120, 15, canvas, fill="black")

#funkcia na oznacenie stlpcov a riadkov
def text():
    list = ['A','B','C','D','E','F','G','H','1','2','3','4','5','6','7','8']
    for i in range(8):
        x = 120+i*80
        canvas.create_text(40,x,fill="black",font="Times 40",text="".join(list[i+8]))
        canvas.create_text(x,40,fill="black",font="Times 40",text="".join(list[i]))



def prevodX(suradnica):
    x = suradnica[1]
    if x == '1': return 0
    elif x == '2': return 1
    elif x == '3': return 2
    elif x == '4': return 3
    elif x == '5': return 4
    elif x == '6': return 5
    elif x == '7': return 6
    elif x == '8': return 7

def prevodY(suradnice):
    y = suradnice[0]
    if y == 'A': return 0
    elif y=='B': return 1
    elif y=='C': return 2
    elif y=='D': return 3
    elif y=='E': return 4
    elif y=='F': return 5
    elif y=='G': return 6
    elif y=='H': return 7


def tah_hraca1(ktox,ktoy,kamx,kamy):
    canvas.create_rectangle(840,585,1110,620, fill='white')
    if a[ktox][ktoy] != 5:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif a[kamx][kamy] != 1:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamx < ktox:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif abs(kamx - ktox) >= abs(2) and abs(kamy - ktoy) > abs(2):
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif ktox - ktoy == 0:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy - ktoy == 0:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy == 2+ktoy and a[ktox+1][ktoy+1] == 5:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy == 2+ktoy and a[ktox+1][ktoy+1] == 1:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif ktoy == 2+kamy and a[ktox+1][ktoy-1] == 1:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy == 2+ktoy and a[ktox+1][ktoy-1] == 5:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    else:
        a[ktox][ktoy] = 1
        if kamx == 7:
            a[kamx][kamy] = 15
        else:
            a[kamx][kamy] = 5
        if kamx == ktox+2 and kamy == ktoy + 2:
            a[ktox+1][ktoy+1] = 1
        if kamx == ktox +2 and kamy == ktoy - 2:
            a[ktox+1][ktoy-1] = 1
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[1] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")





def tah_hraca2(ktox,ktoy,kamx,kamy):
    canvas.create_rectangle(840,585,1110,620, fill='white')
    if a[ktox][ktoy] != 7:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif a[kamx][kamy] != 1:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamx > ktox:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif abs(kamx - ktox) >= abs(2) and abs(kamy - ktoy) > abs(2):
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif ktox - ktoy == 0:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy - ktoy == 0:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy == 2+ktoy and a[ktox-1][ktoy+1] == 1:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamy == 2+ktoy and a[ktox-1][ktoy+1] == 7:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif ktoy == 2+kamy and a[ktox-1][ktoy-1] == 1:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif ktoy == 2+kamy and a[ktox-1][ktoy-1] == 7:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    else:
        a[ktox][ktoy] = 1
        if kamx == 0:
            a[kamx][kamy] = 17
        else:
            a[kamx][kamy] = 7
        if kamx == ktox - 2 and kamy == ktoy + 2:
            a[ktox-1][ktoy+1] = 1
        if kamx == ktox -2 and kamy == ktoy - 2:
            a[ktox-1][ktoy-1] = 1
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[0] == 0:
            canvas.create_text(975, 600, text="Hráč č.2 vyhral",font="Times 15", width=305, fill="red")


def tah_damy1(ktox,ktoy,kamx,kamy):
    vyhodeny = 0
    kontrola = True
    if a[kamx][kamy] != 1:
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif abs(kamx - ktox) != abs(kamy-ktoy):
        canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamx > ktox and kamy > ktoy:   #pre 4. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox+i][ktoy+i] == 5 or a[ktox+i][ktoy+i] == 15:
                canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox+i][ktoy+i] == 7 or a[ktox+i][ktoy+i] == 17):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox+i][ktoy+i] = 1
            a[kamx][kamy] = 15
        else:
            canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[1] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")


    elif kamx > ktox and kamy < ktoy:   #pre 3. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox+i][ktoy-i] == 5 or a[ktox+i][ktoy-i] == 15:
                canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox+i][ktoy-i] == 7 or a[ktox+i][ktoy-i] == 17):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox+i][ktoy-i] = 1
            a[kamx][kamy] = 15
        else:
            canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[1] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")


    elif kamx < ktox and kamy < ktoy:   #pre 2. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox-i][ktoy-i] == 5 or a[ktox-i][ktoy-i] == 15:
                canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox-i][ktoy-i] == 7 or a[ktox-i][ktoy-i] == 17):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox-i][ktoy-i] = 1
            a[kamx][kamy] = 15
        else:
            canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[1] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")

    elif kamx < ktox and kamy > ktoy:   #pre 1. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox-i][ktoy+i] == 5 or a[ktox-i][ktoy+i] == 15:
                canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox-i][ktoy+i] == 7 or a[ktox-i][ktoy+i] == 17):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox-i][ktoy+i] = 1
            a[kamx][kamy] = 15
        else:
            canvas.create_text(975, 600, text="Hráč č.1 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[1] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")


def tah_damy2(ktox,ktoy,kamx,kamy):
    vyhodeny = 0
    kontrola = True
    if a[kamx][kamy] != 1:
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif abs(kamx - ktox) != abs(kamy-ktoy):
        canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
    elif kamx > ktox and kamy > ktoy:   #pre 4. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox+i][ktoy+i] == 7 or a[ktox+i][ktoy+i] == 17:
                canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox+i][ktoy+i] == 5 or a[ktox+i][ktoy+i] == 15):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox+i][ktoy+i] = 1
            a[kamx][kamy] = 17
        else:
            canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[0] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")


    elif kamx > ktox and kamy < ktoy:   #pre 3. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox+i][ktoy-i] == 7 or a[ktox+i][ktoy-i] == 17:
                canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox+i][ktoy-i] == 5 or a[ktox+i][ktoy-i] == 15):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox+i][ktoy-i] = 1
            a[kamx][kamy] = 17
        else:
            canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[0] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")


    elif kamx < ktox and kamy < ktoy:   #pre 2. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox-i][ktoy-i] == 7 or a[ktox-i][ktoy-i] == 17:
                canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox-i][ktoy-i] == 5 or a[ktox-i][ktoy-i] == 15):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox-i][ktoy-i] = 1
            a[kamx][kamy] = 17
        else:
            canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[0] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")

    elif kamx < ktox and kamy > ktoy:   #pre 1. kvadrant
        for i in range(1,abs(ktox-kamx)):
            if a[ktox-i][ktoy+i] == 7 or a[ktox-i][ktoy+i] == 17:
                canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
                kontrola = False
            if (a[ktox-i][ktoy+i] == 5 or a[ktox-i][ktoy+i] == 15):    #testovanie či niesú 2 cudzie figúrky pri sebe
                if vyhodeny == 0:
                    vyhodeny = 1
                else:
                    kontrola = False
            else:
                vyhodeny = 0
        if kontrola == True:
            a[ktox][ktoy] = 1
            for i in range(abs(ktox-kamx)):
                a[ktox-i][ktoy+i] = 1
            a[kamx][kamy] = 17
        else:
            canvas.create_text(975, 600, text="Hráč č.2 zadali ste neplatný ťah",font="Times 15", width=305, fill="red")
        create_figures(a)
        vstupA.set('')
        vstupB.set('')
        if pocet_figurok()[0] == 0:
            canvas.create_text(975, 600, text="Hráč č.1 vyhral",font="Times 15", width=305, fill="red")




def pocet_figurok():
    zlte = 0
    cervene = 0
    for i in range(8):
        for j in range(8):
            if a[i][j] == 5 or a[i][j] == 15:
                cervene = cervene + 1
            elif a[i][j] == 7 or a[i][j] == 17:
               zlte = zlte + 1
    return cervene,zlte



def spracuj1():
        KTO = vstupA.get()
        KAM = vstupB.get()
        ktox = prevodX(KTO)
        ktoy = prevodY(KTO)
        kamx = prevodX(KAM)
        kamy = prevodY(KAM)
        if a[ktox][ktoy] == 15:
            tah_damy1(ktox,ktoy,kamx,kamy)
        else:
            tah_hraca1(ktox,ktoy,kamx,kamy)



def spracuj2():
        KTO = vstupA.get()
        KAM = vstupB.get()
        ktox = prevodX(KTO)
        ktoy = prevodY(KTO)
        kamx = prevodX(KAM)
        kamy = prevodY(KAM)
        if a[ktox][ktoy] == 17:
            tah_damy2(ktox,ktoy,kamx,kamy)
        else:
            tah_hraca2(ktox,ktoy,kamx,kamy)







velkost = 80
okno = tk.Tk()
canvas = tk.Canvas(okno, width = 1220, height = 720)
canvas.pack()


with open("zoznam_zoznamov.txt", "r") as reader:
    subor = reader.read().split()

a = []

for i in range(8):
    pom = []
    for j in range(8):
        pom.append(int(subor[i*8+j]))
    a.append(pom)







create_figures(a)
text()

vstupA = tk.StringVar()
vstupB = tk.StringVar()


canvas.update()
canvas.create_rectangle((790,70, 1205, 110), fill='green')
canvas.create_text(1000, 95, text="Zadaj súradnice a klikni na svojho hráča:",font="Times 15", width=405, fill="black")
a_text= canvas.create_text(840, 200, text="Zadajte pozíciu figurky, ktorou sa chcete posunúť:",font="Times 12", width=170, fill="black")
b_text = canvas.create_text(1100, 200, text="Zadajte pozíciu, kam sa chcete dostať:",font="Times 12", width=170, fill="black")
a_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER, textvariable= vstupA).place(x=775,y=235,width=100, height=100)
b_Entry = tk.Entry(background="white", font="Times 30", justify=CENTER, textvariable= vstupB).place(x=1050,y=235,width=100, height=100)
tk.Button(okno,text="HRAČ 1", bd='10', command=spracuj1).place(x=830, y=370,width=100, height=50)
tk.Button(okno,text="HRAČ 2", bd='10', command=spracuj2).place(x=980, y=370,width=100, height=50)
okno.mainloop()
