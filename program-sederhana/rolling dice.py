import random
import os
os.system("cls")

def roll_dice():
    dice_number = random.randint (1,6)
    return dice_number

print("===SILAHKAN PUTAR DADU ANDA===")

while True:
    choice = input("apakah anda ingin bermain? (y/n) = ")
    if choice == "y":
        print("dadu sedang diputar....")
        number = roll_dice()
        print(f'nomor dadu anda adalah = {number}')
    elif choice == 'n':
        print('terima kasih, program telah berhenti!!')
        break
    else:
        print('perintah yang anda masukkan salah!!')