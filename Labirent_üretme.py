import random
import tkinter as tk
from tkinter import messagebox


def çalıştır():
    root = tk.Tk()
    root.title("Gezgin Robot")
    canvas1 = tk.Canvas(root, width=400, height=300)
    canvas1.pack()
    label1 = tk.Label(root, text="Labirentin uzunluk ve genişliğini giriniz", font=("Arial", 10))
    label1.pack()
    entry1 = tk.Entry(root)
    canvas1.create_window(200, 140, window=entry1)
    entry2 = tk.Entry(root)
    canvas1.create_window(200, 100, window=entry2)
    global x1, x2

    def sayı_al():
        yükseklik = entry1.get()
        genişlik = entry2.get()
        yükseklik=int(yükseklik)
        genişlik = int(genişlik)
        if yükseklik > 2 and genişlik > 2:
            messagebox.showinfo("Veriler alındı","Girdiğiniz veriler")
            messagebox.showinfo("Veriler alındı", "Oyunu tekrar başlatın")
            root.quit()
            canvas1.quit()
        else:
            messagebox.showerror("Hatalı Sayı","Lütfen sayıları 2'den büyük girin")
        return yükseklik, genişlik

    button1 = tk.Button(root, text="Verileri gönder", command=lambda: sayı_al())
    button1.pack()
    canvas1.create_window(200, 180, window=button1)
    root.mainloop()

    def sarılı_hücreler(rand_engel):
        s_hücreler = 0
        if (labirent[rand_engel[0] - 1][rand_engel[1]] == ' '):
            s_hücreler += 1
        if (labirent[rand_engel[0] + 1][rand_engel[1]] == ' '):
            s_hücreler += 1
        if (labirent[rand_engel[0]][rand_engel[1] - 1] == ' '):
            s_hücreler += 1
        if (labirent[rand_engel[0]][rand_engel[1] + 1] == ' '):
            s_hücreler += 1

        return s_hücreler

    engel = '#'
    hücre = ' '
    ziyaret_edilmemiş = 'u'
    yükseklik,genişlik=sayı_al()
    labirent = []

    for i in range(0, yükseklik):
        line = []
        for j in range(0, genişlik):
            line.append(ziyaret_edilmemiş)
        labirent.append(line)

    başlangıç_yükseklik = int(random.random() * yükseklik)
    başlangıç_genişlik = int(random.random() * genişlik)
    if (başlangıç_yükseklik == 0):
        başlangıç_yükseklik += 1
    if (başlangıç_yükseklik == yükseklik - 1):
        başlangıç_yükseklik -= 1
    if (başlangıç_genişlik == 0):
        başlangıç_genişlik += 1
    if (başlangıç_genişlik == genişlik - 1):
        başlangıç_genişlik -= 1

    labirent[başlangıç_yükseklik][başlangıç_genişlik] = hücre
    engeller = []
    engeller.append([başlangıç_yükseklik - 1, başlangıç_genişlik])
    engeller.append([başlangıç_yükseklik, başlangıç_genişlik - 1])
    engeller.append([başlangıç_yükseklik, başlangıç_genişlik + 1])
    engeller.append([başlangıç_yükseklik + 1, başlangıç_genişlik])

    labirent[başlangıç_yükseklik - 1][başlangıç_genişlik] = '#'
    labirent[başlangıç_yükseklik][başlangıç_genişlik - 1] = '#'
    labirent[başlangıç_yükseklik][başlangıç_genişlik + 1] = '#'
    labirent[başlangıç_yükseklik + 1][başlangıç_genişlik] = '#'

    while (engeller):
        rand_engel = engeller[int(random.random() * len(engeller)) - 1]

        if (rand_engel[1] != 0):
            if (labirent[rand_engel[0]][rand_engel[1] - 1] == 'u' and labirent[rand_engel[0]][rand_engel[1] + 1] == ' '):
                s_hücreler = sarılı_hücreler(rand_engel)

                if (s_hücreler < 2):
                    labirent[rand_engel[0]][rand_engel[1]] = ' '

                    if (rand_engel[0] != 0):
                        if (labirent[rand_engel[0] - 1][rand_engel[1]] != ' '):
                            labirent[rand_engel[0] - 1][rand_engel[1]] = '#'
                        if ([rand_engel[0] - 1, rand_engel[1]] not in engeller):
                            engeller.append([rand_engel[0] - 1, rand_engel[1]])

                    if (rand_engel[0] != yükseklik - 1):
                        if (labirent[rand_engel[0] + 1][rand_engel[1]] != ' '):
                            labirent[rand_engel[0] + 1][rand_engel[1]] = '#'
                        if ([rand_engel[0] + 1, rand_engel[1]] not in engeller):
                            engeller.append([rand_engel[0] + 1, rand_engel[1]])

                    if (rand_engel[1] != 0):
                        if (labirent[rand_engel[0]][rand_engel[1] - 1] != ' '):
                            labirent[rand_engel[0]][rand_engel[1] - 1] = '#'
                        if ([rand_engel[0], rand_engel[1] - 1] not in engeller):
                            engeller.append([rand_engel[0], rand_engel[1] - 1])

                for engel in engeller:
                    if (engel[0] == rand_engel[0] and engel[1] == rand_engel[1]):
                        engeller.remove(engel)

                continue

        if (rand_engel[0] != 0):
            if (labirent[rand_engel[0] - 1][rand_engel[1]] == 'u' and labirent[rand_engel[0] + 1][rand_engel[1]] == ' '):

                s_hücreler = sarılı_hücreler(rand_engel)
                if (s_hücreler < 2):
                    labirent[rand_engel[0]][rand_engel[1]] = ' '

                    if (rand_engel[0] != 0):
                        if (labirent[rand_engel[0] - 1][rand_engel[1]] != ' '):
                            labirent[rand_engel[0] - 1][rand_engel[1]] = '#'
                        if ([rand_engel[0] - 1, rand_engel[1]] not in engeller):
                            engeller.append([rand_engel[0] - 1, rand_engel[1]])

                    if (rand_engel[1] != 0):
                        if (labirent[rand_engel[0]][rand_engel[1] - 1] != ' '):
                            labirent[rand_engel[0]][rand_engel[1] - 1] = '#'
                        if ([rand_engel[0], rand_engel[1] - 1] not in engeller):
                            engeller.append([rand_engel[0], rand_engel[1] - 1])

                    if (rand_engel[1] != genişlik - 1):
                        if (labirent[rand_engel[0]][rand_engel[1] + 1] != ' '):
                            labirent[rand_engel[0]][rand_engel[1] + 1] = '#'
                        if ([rand_engel[0], rand_engel[1] + 1] not in engeller):
                            engeller.append([rand_engel[0], rand_engel[1] + 1])

                for engel in engeller:
                    if (engel[0] == rand_engel[0] and engel[1] == rand_engel[1]):
                        engeller.remove(engel)

                continue

        if (rand_engel[0] != yükseklik - 1):
            if (labirent[rand_engel[0] + 1][rand_engel[1]] == 'u' and labirent[rand_engel[0] - 1][rand_engel[1]] == ' '):

                s_hücreler = sarılı_hücreler(rand_engel)
                if (s_hücreler < 2):
                    labirent[rand_engel[0]][rand_engel[1]] = ' '

                    if (rand_engel[0] != yükseklik - 1):
                        if (labirent[rand_engel[0] + 1][rand_engel[1]] != ' '):
                            labirent[rand_engel[0] + 1][rand_engel[1]] = '#'
                        if ([rand_engel[0] + 1, rand_engel[1]] not in engeller):
                            engeller.append([rand_engel[0] + 1, rand_engel[1]])
                    if (rand_engel[1] != 0):
                        if (labirent[rand_engel[0]][rand_engel[1] - 1] != ' '):
                            labirent[rand_engel[0]][rand_engel[1] - 1] = '#'
                        if ([rand_engel[0], rand_engel[1] - 1] not in engeller):
                            engeller.append([rand_engel[0], rand_engel[1] - 1])
                    if (rand_engel[1] != genişlik - 1):
                        if (labirent[rand_engel[0]][rand_engel[1] + 1] != ' '):
                            labirent[rand_engel[0]][rand_engel[1] + 1] = '#'
                        if ([rand_engel[0], rand_engel[1] + 1] not in engeller):
                            engeller.append([rand_engel[0], rand_engel[1] + 1])

                for engel in engeller:
                    if (engel[0] == rand_engel[0] and engel[1] == rand_engel[1]):
                        engeller.remove(engel)

                continue

        if (rand_engel[1] != genişlik - 1):
            if (labirent[rand_engel[0]][rand_engel[1] + 1] == 'u' and labirent[rand_engel[0]][rand_engel[1] - 1] == ' '):

                s_hücreler = sarılı_hücreler(rand_engel)
                if (s_hücreler < 2):
                    labirent[rand_engel[0]][rand_engel[1]] = ' '

                    if (rand_engel[1] != genişlik - 1):
                        if (labirent[rand_engel[0]][rand_engel[1] + 1] != ' '):
                            labirent[rand_engel[0]][rand_engel[1] + 1] = '#'
                        if ([rand_engel[0], rand_engel[1] + 1] not in engeller):
                            engeller.append([rand_engel[0], rand_engel[1] + 1])
                    if (rand_engel[0] != yükseklik - 1):
                        if (labirent[rand_engel[0] + 1][rand_engel[1]] != ' '):
                            labirent[rand_engel[0] + 1][rand_engel[1]] = '#'
                        if ([rand_engel[0] + 1, rand_engel[1]] not in engeller):
                            engeller.append([rand_engel[0] + 1, rand_engel[1]])
                    if (rand_engel[0] != 0):
                        if (labirent[rand_engel[0] - 1][rand_engel[1]] != ' '):
                            labirent[rand_engel[0] - 1][rand_engel[1]] = '#'
                        if ([rand_engel[0] - 1, rand_engel[1]] not in engeller):
                            engeller.append([rand_engel[0] - 1, rand_engel[1]])

                for engel in engeller:
                    if (engel[0] == rand_engel[0] and engel[1] == rand_engel[1]):
                        engeller.remove(engel)

                continue

        for engel in engeller:
            if (engel[0] == rand_engel[0] and engel[1] == rand_engel[1]):
                engeller.remove(engel)

    for i in range(0, yükseklik):
        for j in range(0, genişlik):
            if (labirent[i][j] == 'u'):
                labirent[i][j] = '#'

    for i in range(0, genişlik):
        if (labirent[1][i] == ' '):
            labirent[0][i] = ' '
            break

    for i in range(genişlik - 1, 0, -1):
        if (labirent[yükseklik - 2][i] == ' '):
            labirent[yükseklik - 1][i] = ' '
            break

    p1 = random.randint(0,yükseklik-1)
    p2 = random.randint(0,genişlik-1)

    while True:
        if labirent[p1][p2]== ' ':
            labirent[p1][p2] = 'X'

            break
        p1 = random.randint(0, yükseklik - 1)
        p2 = random.randint(0, genişlik - 1)
    while True:
        if labirent[p1][p2]== ' ':
            labirent[p1][p2] = 'Y'

            break
        p1 = random.randint(0, yükseklik - 1)
        p2 = random.randint(0, genişlik - 1)
    ek_duvar = []
    for satır in range(genişlik):
        ek_duvar.append('#')
    labirent.insert(0,ek_duvar)
    labirent.insert(yükseklik+1,ek_duvar)
    with open('LabirentX.txt', 'w') as f:
        for line in labirent:
            for words in line:
                f.write("%s"%words)
            f.write("\n")
# çalıştır()