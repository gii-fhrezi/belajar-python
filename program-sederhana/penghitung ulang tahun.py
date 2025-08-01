# mengimport modul datetime dari library python
from datetime import datetime
sekarang = datetime.now()
print(f'sekarang tanggal {sekarang}') # maka output nya akan menghasilkan koma dibelakang nya, untuk mengubahnya 
print(f'sekarang tanggal {sekarang:%d-%m-%y}') # d= day m= month y= year

# untuk menampilkan jam nya saja tanpa tanggal
print(f'sekarang jam {sekarang:%H.%M}') # kita bisa mengubah tanda titik diantara %H dan %M menjadi karakter lain yg kita mau
print(f'sekarang jam {sekarang:%H.%M.%S}') # jika ingin menambahkan dengan detik juga
 
tanggal_lahir = input(f'masukkan tanggal lahir anda (DD:MM:YYYY) : ')
tanggal_lahir = datetime.strptime(tanggal_lahir, '%d:%m:%Y')


sekarang = datetime.now() # mendapatkan waktu sekarang
ulang_tahun = tanggal_lahir.replace(year=sekarang.year)# Membuat ulang tahun di tahun ini dengan mengganti year dari tanggal_lahir
# menjadi year dari sekarang

# mengecek jika ulang tahun di tahun ini sudah lewat
if ulang_tahun < sekarang:
    # Jika sudah lewat, kita hitung untuk tahun depan (+1 tahun)
    ulang_tahun = ulang_tahun.replace(year=sekarang.year + 1)

sisa_hari = (ulang_tahun - sekarang).days# Menghitung selisih hari antara ulang tahun berikutnya dan sekarang
print(f'ulang tahun anda berikutnya dalam {sisa_hari} hari! ')