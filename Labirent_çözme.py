import tkinter as tk
from tkinter import messagebox
import time
def çalıştır():

    root = tk.Tk()
    root.title("Gezgin Robot")

    def get_LabirentX():
        with open("LabirentX.txt") as f:
            lines = f.read().splitlines()
            return [line.strip() for line in lines]
    global labirent
    labirent = get_LabirentX()
    label = tk.Label(root, text="Labirent", font=("Arial", 24))
    label.pack()
    canvas_genişlik = 640
    canvas_yükseklik = 480
    canvas = tk.Canvas(root, width=canvas_genişlik, height=canvas_yükseklik)
    canvas.pack()

    def draw_labirent():
        canvas.delete('all')

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
                    canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
                elif labirent[i][j] == 'X':
                    canvas.create_rectangle(x1, y1, x2, y2, fill='green')
                elif labirent[i][j] == 'Y':
                    canvas.create_rectangle(x1, y1, x2, y2, fill='red')
                elif labirent[i][j] == 'V':
                    canvas.create_rectangle(x1, y1, x2, y2, fill='blue')

        root.update()

    def draw_yol(yol):
        hücre_genişlik = canvas_genişlik // len(labirent[0])
        hücre_yükseklik = canvas_yükseklik // len(labirent)
        yol.pop(0)
        yol.pop(len(yol)-1)
        for p1 in yol:
            i=p1[0]
            j=p1[1]
            x1 = j * hücre_genişlik
            y1 = i * hücre_yükseklik
            x2 = x1 + hücre_genişlik
            y2 = y1 + hücre_yükseklik
            root.after(1)
            canvas.create_rectangle(x1, y1, x2, y2, fill='white')

            root.update()


    def çöz_labirent(labirent):
        tik = time.perf_counter()
        start_satır, start_sütun = None, None
        for satır in range(len(labirent)):
            for sütun in range(len(labirent[satır])):
                if labirent[satır][sütun] == 'X':
                    start_satır, start_sütun = satır, sütun
                    break
            if start_sütun is not None:
                break
        if start_satır is None:
            return None

        stack = [(start_satır, start_sütun, [])]
        gezilmiş = set()
        while stack:
            satır, sütun, yol = stack.pop()
            if labirent[satır][sütun] == 'Y':
                draw_yol(yol + [(satır, sütun)])
                tak = time.perf_counter()
                zaman = tk.StringVar()
                zaman.set(tak - tik)
                zaman_box = tk.Entry(root,width=20,font=("Arial", 10),textvariable=zaman)
                zaman_box.place(x=0, y=0)
                messagebox.showinfo("Çözüm süresi (s.)", tak-tik)
                return yol + [(satır, sütun)]
            if (satır, sütun) in gezilmiş:
                continue
            gezilmiş.add((satır, sütun))
            if satır > 0 and labirent[satır - 1][sütun] != '#':
                stack.append((satır - 1, sütun, yol + [(satır, sütun)]))
            if satır < len(labirent) - 1 and labirent[satır + 1][sütun] != '#':
                stack.append((satır + 1, sütun, yol + [(satır, sütun)]))
            if sütun > 0 and labirent[satır][sütun - 1] != '#':
                stack.append((satır, sütun - 1, yol + [(satır, sütun)]))
            if sütun < len(labirent[satır]) - 1 and labirent[satır][sütun + 1] != '#':
                stack.append((satır, sütun + 1, yol + [(satır, sütun)]))
        tak = time.perf_counter()
        print(tak - tik)

        return None
    çöz_button = tk.Button(root, text="Labirenti Çöz", command=lambda:çöz_labirent(labirent))
    çöz_button.pack()
    çıkış_button = tk.Button(root, text="Çıkış", command=lambda:root.quit())
    çıkış_button.pack()
    draw_labirent()

    root.mainloop()
# çalıştır()
