import os
import time
os.system('cls')

def countdown():
    detik = int(input("masukkan durasi dalam format detik  =" ))# karena hasil input berupa str maka perlu diubah menjadi int
    print("hitung mundur dimulai dari sekarang....")
    temp =  detik
    while temp != 0 : # selama detik tidak sama dengan 0
        print('\b' * len(str(temp)), end='')
        time.sleep(1)
        temp -= 1
        print(temp,end='')
    print(f'\nhitung mundur sudah berakhir....\n')

print('===== SELAMAT DATANG DI PROGRAM HITUNG MUNDUR =====')

while True:
    pilihan = input('apakah anda ingin menggunakan program ini? (y/n)  = ')
    if pilihan == 'y':
        countdown()
    elif pilihan == 'n':
        print("program telah berhenti, terima kasih telah menggunakan program ini!!")
        break
    else:
        print("perintah yang anda masukkan tidak valid!!")
