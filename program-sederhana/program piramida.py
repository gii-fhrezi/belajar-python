import os
os.system("cls")

n = 6 # ukuran tinggi piramida

print('========================')
print('Program Piramida Bintang')
print('========================')


print('''
1.Piramida Kiri (naik)
2.Piramida Kiri (turun)
3.Piramida kanan (naik)
4.Piramida Kanan (turun)
5.Piramida sama kaki (centered naik)
6.Piramida samakaki Terbalik (centerred turun)
7.Belah Ketupat
8.Piramida kotak kosong
      ''')

perintah = int(input("Masukkan pola nomor berapa yang anda inginkan! = "))

if perintah == 1:
    print("Piramida Kiri (naik)")
    for i in range (1, n+1):
        print("*" * i)

elif perintah == 2:
    print ("2.Piramida Kiri (turun)")
    for i in range (n, 0, -1): # artinya adalah loop dimulai dari 5 - 0, dan setiap loop dikurang 1
        print ("*" * i)

elif perintah == 3:
    print ("3.Piramida kanan (naik)")
    for i in range(1, n+1):
        spasi = " " * (n - 1)
        bintang = "*" * i
        print(spasi+bintang)

elif perintah == 4:
    print("4.Piramida Kanan (turun)")
    for i in range (n, 0, -1):
        spasi =" " * (n-1)
        bintang = "*" * i
        print(spasi+bintang)

elif perintah == 5:
    print ("5.Piramida sama kaki (centered naik)")
    for i in range (1, n+1):
        spasi = " " * (n - i)
        bintang = "*" * (2*i -1)
        print(spasi+bintang)

elif perintah == 6:
    print("6.Piramida samakaki Terbalik (centerred turun)")
    for i in range (n, 0, -1):
        spasi = " " * (n - i)
        bintang = "*" * (2*i -1)
        print(spasi+bintang)

elif perintah == 7:
    print("7.Belah Ketupat")
    # gabungan dari centered
    # bagian atas
    for i in range(0, n+1):
        spasi = " " * (n-i)
        bintang= "*" * (2*i - 1)
        print(spasi+bintang)
    
    #bagian bawah
    for i in range(n, 0, -1):
        spasi = " " * (n-i)
        bintang = "*" * (2*i - 1)
        print(spasi+bintang)

elif perintah == 8:
    print("8.Piramida kotak kosong")
    for i in range(1, n+1):
        if i == 1:
            print(' ' * (n - i) + '*') # untuk bagian paling atas
        elif i == n:
            print('*' * (2*i - 1)) # untuk bagian paling bawah
        else:
            tengah_kosong = ' ' * (2*i - 3)
            print(' ' * (n - i) + '*' + tengah_kosong + '*') # untuk bagian tengah

else:
    print("input yang anda masukkan tidak valid!!")
    