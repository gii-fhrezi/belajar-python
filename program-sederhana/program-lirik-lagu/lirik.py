import os
os.system('cls')
import sys
import pygame
import time

import pygame

pygame.mixer.init()
pygame.mixer.music.load("malapetaka1.mp3")  
pygame.mixer.music.play()            




def panggil_lirik():
    lirik = [
        ("Walau ku hafal di luar kepala",0.2),# buat kasih jeda printan per karakter
        ("Perangai mata sebibir-bibirnya",0.12),
        ("Tapi tetap tak bisa ku membaca",0.11),

        ("Yang kau rasaa",0.2),
        ("Tentang kitaaaa",0.2),

        ("Alah, malapetaka atau malah awalnya",0.12),
        ("Kisah bahagia",0.17),
        ("Teman selama-lamanya",0.11),
        ("atau akan jadi bumerangku dan kau berbeda",0.10),
        ("Biar lusa ku lukaaaaa",0.17),
        ("Air turun dari maataaa",0.15),
        ("Katakan yang sebenarnya",0.15),
    ]
    delay = [0.2, 0.2, 0.3, 1.75, 0.3, 0.4, 1, 0.5, 1.2, 0.8, 0.8, 0.3] # buat kasih jeda kapan masuk antar baris
    print("/n ==malapetaka - juicy luicy==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
panggil_lirik()
