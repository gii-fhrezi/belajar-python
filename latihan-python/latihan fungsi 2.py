# membuat program perhitungan luas dan keliling persegi
import os
os.system('cls')

#header
'''
print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI':^40}")
print(f"{'-'*40:^40}")

#input user
lebar = int(input('masukkan nilai lebar = '))
panjang = int(input('masukkan nilai panjang = '))

#menghitung luasnya
luas = panjang*lebar
keliling = 2*(panjang + lebar)

#menampilkan hasilnya
print(f'hasil perhitungan luasnya adalah = {luas}')
print(f'hasil perhitungan kelilingnya adalah = {keliling}')
''' 
# kita bisa meringkas program diatas menggunakan fungsi def agar ketika ingin menambahkan atau menghapus
# fitur menjaadi lebih mudah

def header():
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI':^40}")
    print(f"{'-'*40:^40}")
def input_pilihan():
    '''fungsi input pilihan'''
    klik = int(input("Mau menghitung apa?\nKetik 1 untuk luas\nKetik 2 untuk keliling\nKetik 3 untuk hitung semua\n>>>"))    
    return klik
def input_user():
    lebar = int(input('masukkan nilai lebar = '))
    panjang = int(input('masukkan nilai panjang = '))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    return 2*(lebar + panjang)

def milih(KLIK):
    '''fungsi milih'''
    if KLIK == 1:
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        return display("luas",LUAS)

    elif KLIK == 2:
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        return display("keliling",KELILING)

    elif KLIK == 3:
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        return display("luas", LUAS) , display("keliling",KELILING)
    
    else:
        return display("...ngitung apa?? ketik yang bener!!!",0)
    

def display(message,value):
    print(f'hasil perhitungan {message} = {value}')

# program utamanya
while True:
    header()
    KLIK = input_pilihan()
    pilihan = milih(KLIK)

    iscontinue = input('apakah lanjut (y/n) ? = ')
    if iscontinue == 'n':
        break
print('program telah berhenti , terima kasih')
