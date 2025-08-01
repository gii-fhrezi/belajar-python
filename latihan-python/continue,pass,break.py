print('soal nomor 1.\n')
'''Buat program menggunakan for loop yang:
Mencetak semua angka dari 1 sampai 10,
Tapi lewati angka 5 (jangan dicetak jika angka 5).
Contoh output:
1
2
3
4
6
7
8
9
10'''

angka = 0
while angka < 10:
    angka += 1
    if angka == 5: continue # angka 5 tidak akan keluar karena sudah di beri continue
    print(angka)

print ('=== soal nomor 2.===\n')

'''Buat program menggunakan if-else yang:
Jika nilai di atas 80, tampilkan "Nilai bagus!".
Jika nilai di bawah atau sama dengan 80, gunakan pass agar program tetap jalan tanpa output apa pun.
Contoh:
Masukkan nilai: 90
Nilai bagus!
Masukkan nilai: 75
(tidak tampil apa-apa)'''

nilai = float(input('masukkan nilai : '))
if nilai > 80:
    print('nilai bagus')

else:
    pass # angka dibawah 80 tidak akan terjadi apa2

print('\n=== soal nomor 3.===')

'''Buat program yang:
Meminta user memasukkan jenis buah.
Jika buah = "apel", tampilkan: "Ini adalah buah apel!".
Jika buah bukan apel, gunakan pass agar tidak ada output.
Contoh Output:
Masukkan buah: apel
Ini adalah buah apel!
Masukkan buah: mangga
(tidak tampil apa-apa)'''

buah = (input('masukkan buah = '))
if buah == 'apel':
    print('ini adalah buah apel')
else : pass

print('=== soal nomor 4.===')
'''Buat program menggunakan for loop untuk mencetak semua angka dari 1 sampai 15,
Tapi:
Lewati angka kelipatan 3 (jangan dicetak jika angka habis dibagi 3).
Contoh Output:
1
2
4
5
7
8
10
11
13
14'''

for angka in range(1,16): # untuk menngeprint angka 1-15
    if angka % 3 == 0 : continue
    print(angka)
