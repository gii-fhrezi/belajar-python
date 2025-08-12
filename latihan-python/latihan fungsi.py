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