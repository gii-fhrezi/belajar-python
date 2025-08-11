''' Fungsi dengan argument (input)'''
import os
os.system('cls')
# Template
# def nama_fungsi(argument):
#     Badan fungsi


def hello_world(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}")


hello_world("irgi")
hello_world("Achmad")

# program tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota = ["irgi","achmad","fahrezi"]

say_hi(anggota)