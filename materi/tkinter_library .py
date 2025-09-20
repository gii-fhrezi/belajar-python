#GUI - graphical user interface
# X adalah lebar
# Y adalah panjang

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

jendela = tk.Tk() # akan memanggil si window, tetapi tidak berjalan terus menerus
jendela.configure(bg="blue") # untuk mengkonfigurasi window, salah satunya adalah mengubah warna bg
jendela.resizable(False,False) # agar si window tidak bisa diperkecil ataupun diperbesar untuk x ataupun y nya
jendela.title("irgi achmad fahrezi")
jendela.geometry("300x200") # untuk ukuran si window

# input frame
frame = ttk.Frame(jendela)
frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen komponen
# 1. nama depan
labelnamadepan = ttk.Label(frame,text="Nama Depan: ") 
labelnamadepan.pack(padx=10,fill="x",expand=True)

#entry nama depan
NAMADEPAN = tk.StringVar() # variable untuk menyimpan yg kita ketik di nama depan
entrynamadepan = ttk.Entry(frame,textvariable=NAMADEPAN)# fungsinya adalah untuk nama yg kita isi bisa tersimpan di konstanta nama depan
entrynamadepan.pack(padx=10,fill="x",expand=True)

# label nama belakang
labelnamabelakang = ttk.Label(frame,text="Nama Belakang: ") 
labelnamabelakang.pack(padx=10,fill="x",expand=True)

#entry nama belakang
NAMABELAKANG = tk.StringVar()
entrynamabelakang = ttk.Entry(frame,textvariable=NAMABELAKANG)
entrynamabelakang.pack(padx=10,fill="x",expand=True)

#tombol
def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Halo {NAMADEPAN.get()} {NAMABELAKANG.get()}"
    showinfo(title="Halo!", message=pesan)
tombol_sapa = ttk.Button(frame,text="Sapa! ", command=tombol_click)
tombol_sapa.pack(fill='x', expand=True,padx=10,pady=10)
jendela.mainloop() # setelah dipanggil begini maka baru si window akan melooping terus terusan