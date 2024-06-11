import Labirent_çözme as Labirent_aç
import Labirent_okuma
import Labirent_üretme
import Labirent_oyna
import tkinter as tk

root = tk.Tk()
root.title("Gezgin Robot")
bg = tk.PhotoImage(file = "image.png")
label = tk.Label(root,image=bg)
label.pack()
label1 = tk.Label(root, text="HOŞGELDİNİZ", font=("Arial", 30))
label1.pack()
canvas_genişlik = 420
canvas_yükseklik = 130
canvas = tk.Canvas(root, width=canvas_genişlik, height=canvas_yükseklik)
a_button = tk.Button(root, text="Labirenti çöz", command=lambda: Labirent_aç.çalıştır())
a_button.pack()
b_button = tk.Button(root, text="Labirenti oku", command=lambda: Labirent_okuma.çalıştır())
b_button.pack()
c_button = tk.Button(root, text="Labirenti üret", command=lambda: Labirent_üretme.çalıştır())
c_button.pack()
d_button = tk.Button(root, text="Labirenti oyna", command=lambda: Labirent_oyna.çalıştır())
d_button.pack()
canvas.pack()
root.mainloop()