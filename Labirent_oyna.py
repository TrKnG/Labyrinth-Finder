import tkinter as tk
from tkinter import messagebox
import time

def get_LabirentX():
    with open("LabirentX.txt") as f:
        lines = f.read().splitlines()
        return [line.strip() for line in lines]


global labirent
labirent = get_LabirentX()

for satır in range(len(labirent)):
    for sütun in range(len(labirent[satır])):
        if labirent[satır][sütun] == 'X':
            robot_satır, robot_sütun = satır, sütun
            break

def draw_labirent():
    hücre_genişlik = canvas_genişlik // len(labirent[0])
    hücre_yükseklik = canvas_yükseklik // len(labirent)
    for i in range(len(labirent)):
        for j in range(len(labirent[0])):
            x1 = j * hücre_genişlik
            y1 = i * hücre_yükseklik
            x2 = x1 + hücre_genişlik
            y2 = y1 + hücre_yükseklik
            if labirent[i][j] == '#':
                canvas.create_rectangle(x1, y1, x2, y2, fill='black')
            elif labirent[i][j] == ' ':
                canvas.create_rectangle(x1, y1, x2, y2, fill='white')
            elif labirent[i][j] == 'Y':
                canvas.create_rectangle(x1, y1, x2, y2, fill='red')
            elif labirent[i][j] == 'X':
                canvas.create_rectangle(x1, y1, x2, y2, fill='blue')


def draw_robot():
    hücre_genişlik = canvas_genişlik // len(labirent[0])
    hücre_yükseklik = canvas_yükseklik // len(labirent)
    x1 = robot_sütun * hücre_genişlik
    y1 = robot_satır * hücre_yükseklik
    x2 = (x1  + hücre_genişlik)
    y2 = (y1 + hücre_yükseklik)
    canvas.create_oval(x1, y1, x2, y2, fill='blue')


def move_robot(direction):
    global robot_satır, robot_sütun

    if labirent[robot_satır][robot_sütun] == 'Y':
        tak=time.perf_counter()
        messagebox.showinfo("Başarılı","Gitmek istediğiniz yere ulaştınız.")
        zaman = tk.StringVar()
        zaman.set(tak - tik)
        zaman_box = tk.Entry(root, width=20, font=("Arial", 10), textvariable=zaman)
        zaman_box.place(x=0, y=0)
        messagebox.showinfo("Çözüm süresi (s.)", tak - tik)
    elif direction == 'up' and robot_satır > 0 and labirent[robot_satır-1][robot_sütun] != '#':
        robot_satır -= 1
    elif direction == 'down' and robot_satır < len(labirent)-1 and labirent[robot_satır+1][robot_sütun] != '#':
        robot_satır += 1
    elif direction == 'left' and robot_sütun > 0 and labirent[robot_satır][robot_sütun-1] != '#':
        robot_sütun -= 1
    elif direction == 'right' and robot_sütun < len(labirent[0])-1 and labirent[robot_satır][robot_sütun+1] != '#':
        robot_sütun += 1

    draw_robot()

def controller(event):

    if event.keysym == 'Up':
        move_robot('up')
    elif event.keysym == 'Down':
        move_robot('down')
    elif event.keysym == 'Left':
        move_robot('left')
    elif event.keysym == 'Right':
        move_robot('right')

def çalıştır():
    global tak,tik
    tik=time.perf_counter()
    global canvas, root
    root = tk.Tk()
    root.title("Gezgin Robot")
    label = tk.Label(root, text="Labirent", font=("Arial", 24))
    label.pack()
    global canvas_genişlik,canvas_yükseklik
    canvas_genişlik = 640
    canvas_yükseklik = 480
    canvas = tk.Canvas(root, width=canvas_genişlik, height=canvas_yükseklik)
    canvas.pack()
    canvas.bind('<KeyPress>', controller)
    canvas.focus_set()
    çıkış_button = tk.Button(root, text="Çıkış", command=lambda: root.quit())
    çıkış_button.pack()
    draw_labirent()
    draw_robot()
    root.mainloop()
# çalıştır()