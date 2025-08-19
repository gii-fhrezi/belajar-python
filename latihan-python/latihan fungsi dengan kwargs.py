import os
os.system('cls')

'''
Apa itu **kwargs?

kwargs (kepanjangan dari keyword arguments) 
adalah cara agar fungsi bisa menerima argumen dalam bentuk pasangan kunci-nilai (dictionary).
*args dipakai untuk banyak argumen tanpa nama (seperti list).
**kwargs dipakai untuk banyak argumen dengan nama (seperti dictionary).'''

# contoh
def biodata(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value} ")
biodata(nama= "irgi", umur = 18, hobi = 'coding', asal ='sinambek')

'''
Alur Pemrograman **kwargs

---Pemanggilan Fungsi---
Saat kita memanggil biodata(nama="Irgi", umur=18, hobi="Coding"), 
semua argumen dalam bentuk key=value akan otomatis dikumpulkan menjadi dictionary.
Hasilnya:
kwargs = {"nama": "Irgi", "umur": 18, "hobi": "Coding"}

---Penyimpanan ke kwargs----
Fungsi menerima dictionary ini sebagai kwargs.
Jadi di dalam fungsi, kwargs bisa diakses seperti dictionary biasa.

---Perulangan dengan .items()---
Baris for key, value in kwargs.items(): akan mengambil tiap pasangan key dan value.
Misalnya:

("nama", "Irgi")
("umur", 18)
("hobi", "Coding")
Output
Setiap pasangan akan dicetak dalam format:

nama: Irgi
umur: 18
hobi: Coding

Jadi sederhananya: argumen key=value yang kita kirim → dikumpulkan jadi dictionary → di-loop → ditampilkan isinya.'''



'''
Buat fungsi bernama profil yang menerima data **kwargs dan menampilkan semua informasi yang diberikan.
Contoh pemanggilan:

profil(nama="Irgi", umur=18, hobi="coding", kota="Pekanbaru")'''

def profil(**kwargs):
    for key , value in kwargs.items():
        print(f'{key} = {value}')

profil(nama = 'irgi', umur = 18, hobi = 'coding', kota = 'pekanbaru')

'''
Buat fungsi bernama data_mahasiswa yang menerima **kwargs,
lalu hanya menampilkan nama dan nim (jika ada di dalam kwargs).
Contoh:

data_mahasiswa(nama="Fahrezi", nim="12345", jurusan="TI")'''

def data_mahasiswa(**kwargs):
    if 'nama' in kwargs:
        print('nama =', kwargs.get('nama','tidak ada'))# jika tidak mengisi nama maka input nya akan 'tidak ada'
        print('nim = ', kwargs.get('nim', 'tidak ada'))
data_mahasiswa(nama = 'fahrezi' , jurusan = 'TI')

# versi lain
def data_buku(**kwargs):
    if 'nama' in kwargs:
        print(f'nama buku = {kwargs["nama"]}')
    if 'genre' in kwargs:
        print(f'genre buku = {kwargs["genre"]}')
data_buku(nama = 'dongeng si kancil', genre = 'fantasi', penulis = 'ohim')

# contoh 3
def biodata(**kwargs):
    print('nama = ', kwargs.get('nama', 'tidak ada'))
    print('umur = ', kwargs.get('umur', 'tidak ada'))
    print('asal = ', kwargs.get('asal', 'tidak ada'))
biodata(nama = 'ohim', umur = '18' , asal = 'sinambek', berat= 80)

'''
soal 3
Buat fungsi produk yang menerima **kwargs dan menghitung total harga dari produk yang ada.
Contoh:
produk(buku=20000, pensil=5000, tas=150000)
Output:

Total harga = 175000'''
def produk(**kwargs):
    total = 0
    for nama_barang , harga in kwargs.items():#Dengan .items(), kita langsung dapat key dan value sekaligus.
        total += harga
    print(f'total harga = {total:,}')
produk(buku=20000, pensil=5000, tas=150000)