import os
import time

os.system('cls')

def countdown():
    waktu = int(input('masukkan durasi dalam format detik = '))
    print('memulai hitung mundur!')
    while waktu >= 0:
        print(f'\r{waktu}', end=' detik',flush=True)
        time.sleep(1)# durasi program terjeda = 1 detik
        waktu -= 1
    print('\nhitung mundur sudah selesai!\n')

while True:
    perintah = input('apakah anda ingin menggunakan program ini? (y/n)')
    if perintah == 'y':
        countdown()
    elif perintah == 'n':
        print('program telah berhenti!!')
        break
    else:
        print('perintah yang anda gunakan salah!!')
