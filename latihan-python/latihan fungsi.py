import os
os.system('cls')
# 1.Buatlah fungsi bernama tambah yang menerima 2 argumen (misalnya a dan b) lalu menampilkan hasil penjumlahannya.

def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print (f'hasil penjumlahan = {hasil}')

tambah(12,34)

# 2.Buatlah fungsi bernama perkenalan yang menerima 2 argumen: nama dan umur, lalu cetak kalimat:

def perkenalan(nama,umur):
    print(f'halo, nama saya {nama} dan umur saya {umur} tahun')

perkenalan('irgi',18)
"""
3. Buat fungsi diskon yang menerima harga dan persentase diskon, lalu menghitung harga setelah diskon.

📌 Contoh hasil yang diharapkan:
diskon(200000, 10) ➡ Harga setelah diskon: Rp180000

"""

def diskon(harga,diskon):
    potongan = harga * (diskon / 100)
    total_diskon = harga - potongan
    print (f'harga setelah diskon {total_diskon:,}')

diskon(20000,15)

print(
'''
----berikut adalah contoh dari kapan penggunaan return dalam def----
''')

def tanpa_return(angka1,angka2):
    kali = angka1 * angka2
    print (f'hasilnya adalah {kali}')
hasil = tanpa_return(12,2)
print(f'berikut nilai nya = {hasil}')# hasilnya akan none karena kita tidak menggunakan return

def pakai_return(angka1,angka2):
    kali = angka1 * angka2
    return kali
hasil = pakai_return(12,2)
print(f'berikut nilainya kalau pakai return = {hasil * 2}')

print('''
🔑 Intinya:

print → hanya tampilkan ke layar (hasilnya tidak bisa dipakai ulang).
return → mengirim balik nilai ke luar fungsi 
(hasilnya bisa disimpan, diproses lagi, atau dipakai dalam perhitungan selanjutnya).''')

'''
Buat fungsi bernama jumlah_angka yang menerima banyak angka dengan *args dan mengembalikan hasil penjumlahannya.
Contoh:
print(jumlah_angka(2, 3, 5))  # Output: 10'''

def jumlah_angka (*args):
    kosong = 0
    for angka in args:
        kosong += angka
    return kosong 

print(jumlah_angka(2,3,5))
'''
Buat fungsi bernama cari_terbesar yang menerima banyak angka dengan *args dan mengembalikan angka yang paling besar.
Contoh:
print(cari_terbesar(2, 9, 5, 1, 7))  # Output: 9'''

def cari_terbesar(*args):
    terbesar = args[0]
    for angka in args:
        if angka > terbesar:
            terbesar = angka
    return terbesar
print(cari_terbesar(-10, -5, -7, -20))   
print(cari_terbesar(-10, 0, 5, -3, 8))  


'''
Buat fungsi bernama gabung_kata yang menerima banyak string dengan *args 
dan mengembalikan semua string digabung jadi satu kalimat.
Contoh:

print(gabung_kata("Aku", "suka", "Python"))  '''

def gabung_kata (*args):
    kata = ''
    for kalimat in args:
        kata += kalimat + ' '
    return kata.strip()
print(gabung_kata('aku','suka','python'))

'''
Buat fungsi bernama hitung_rata yang menerima banyak angka dengan *args dan mengembalikan rata-ratanya.
Contoh:
print(hitung_rata(10, 20, 30, 40))  # Output: 25'''

def hitung_rata (*args):
    rata2 = 0
    for angka in args:
        rata2 += angka
    hasil = rata2 / len(args)
    return hasil
print(hitung_rata(10,20,30,40))

def cari_terbesar(*args):
    simpan = args[0]
    for angka in args:
        if angka > simpan:
            simpan = angka
    return simpan
print(cari_terbesar(-10,-20,-2))
