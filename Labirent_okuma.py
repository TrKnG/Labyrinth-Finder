import random
from tkinter import messagebox

def çalıştır():
    f = open ( 'url1.txt' , 'r')
    say = 0
    satırlar = f.readlines()
    l = []
    labirent=[]
    for satır in satırlar:
        say +=1
        rakamlar = satır.rstrip('\n')
        rakamlar = ''.join(('#',rakamlar,'#'))
        for rakam in rakamlar:
            l.append(rakam)
    say = say + 2

    while l != []:
        labirent.append(l[:say])
        l = l[say:]
    ek_duvar = []
    for satır in range(say):
        ek_duvar.append('#')
    labirent.insert(0,ek_duvar)
    labirent.insert(say-1,ek_duvar)

    p1 = random.randint(0,say-1)
    p2 = random.randint(0,say-1)

    while True:
        if labirent[p1][p2]== '0':
            labirent[p1][p2] = 'X'

            break
        p1 = random.randint(0, say - 1)
        p2 = random.randint(0, say - 1)
    while True:
        if labirent[p1][p2]== '0':
            labirent[p1][p2] = 'Y'

            break
        p1 = random.randint(0, say - 1)
        p2 = random.randint(0, say - 1)
    for sutun in labirent:
        a = 0
        for satir in sutun:
            if satir != '0' and satir != 'X' and satir != 'Y':
                sutun[a] = '#'
            if satir == '0':
                sutun[a] = ' '
            a = a+1

    messagebox.showinfo("Veriler alındı","Url dosyasındaki veriler okundu")
    messagebox.showinfo("Veriler alındı", "Oyunu tekrar başlatın")
    with open('LabirentX.txt', 'w') as f:
        for line in labirent:
            for words in line:
                f.write("%s"%words)
            f.write("\n")

# çalıştır()