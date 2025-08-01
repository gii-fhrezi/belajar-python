print ('=' * 14)
print('SOAL LATIHAN 1')
print ('=' * 14)
'''Dari list berikut:
angka_list = [5, 8, 10, 3, 7]
Buat program yang:

1. Menggunakan for loop.
2. Menjumlahkan semua angka di dalam list tersebut.
3. Menampilkan total jumlah angka.

Contoh output:
Total jumlah angka: 33'''

# jawab

angka_list = [5, 8, 10, 3, 7]
total = 0 # tempat menyimpan hasil penjumlahan semua angka
for angka in angka_list:
    total = total + angka

print(f'total jumlah angka: {total}')

print ('=' * 14)
print ('\n','=' * 14)
print('SOAL LATIHAN 2')
print ('=' * 14)    

'''Buat program Python yang:
Menggunakan for loop.
Menampilkan pola segitiga dari bintang (*).
Contoh output yang diharapkan:
*
**
***
****
*****'''

## jawab
for i in range(0,6):
    print('*' * i)

print ('=' * 14)
print ('\n','=' * 14)
print('SOAL LATIHAN 3')
print ('=' * 14)    

'''Buat program Python yang:
Menggunakan for loop.
Mencetak semua bilangan ganjil dari 1 sampai 20.
Contoh output:
1
3
5
7
9
...
19'''

# jawab
for angka in range(1, 21):  # dimulai dari 1 sampai 20
    if angka % 2 != 0:  # cek apakah angka ganjil
        print(angka)


print ('=' * 14)
print ('\n','=' * 14)
print('SOAL LATIHAN 4')
print ('=' * 14)    


'''Buat program Python yang:

Meminta pengguna memasukkan 5 nilai angka (bisa nilai ujian).
Menggunakan for loop untuk menginput nilainya.
Menjumlahkan semua nilai tersebut.
Menampilkan total dan rata-rata nilainya.'''

for i in range(1, 6):
    nilai = float(input(f'Masukkan nilai ke-{i}: '))# akan mengulang perintah ini sebanyak 5x
    total = total + nilai  # setiap input ditambahkan ke total

print(f'Total nilai = {total}')
rata_rata = total / 5
print(f'Rata-rata nilai = {rata_rata}')
