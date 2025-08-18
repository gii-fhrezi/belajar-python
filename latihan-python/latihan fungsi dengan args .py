'''
Buat sebuah fungsi bernama jumlahkan yang:
1. Bisa menerima banyak angka sekaligus (tidak terbatas jumlahnya) menggunakan *args.
2. Menggunakan for angka in args untuk menghitung total semua angka.
3. Mencetak hasil penjumlahan tersebut.
'''

def jumlahkan(*args):
    total = 0
    for angka in args:
        total += angka
    print(f'hasil nya adalah {total}')

jumlahkan(1,4,5,7,4,7)

'''
buat fungsi jumlahkan_semua(*args) 
yang akan menjumlahkan semua angka yang dimasukkan dan mengembalikan hasilnya.
Contoh:
print(jumlahkan_semua(2, 4, 6, 8))  
# Output: 20
'''

def jumlahkan_semua(*args):
    total = 0
    for angka in args:
        total += angka
    return total

print (jumlahkan_semua(2, 3, 4, 5))

'''
Buat fungsi rata_rata(*args) yang menerima banyak angka dan mengembalikan nilai rata-ratanya.

Contoh:
print(rata_rata(10, 20, 30))  
# Output: 20.0
'''

def rata_rata(*args):
    total = 0
    for angka in args:
        total += angka
        rata2 = total / len(args)
    return total
    
print(rata_rata(50,50,75,43))

'''
Buat fungsi gabung_kata(*args) yang menerima banyak string dan menggabungkannya menjadi satu kalimat.

Contoh:
print(gabung_kata("Halo", "nama", "saya", "Irgi"))
# Output: Halo nama saya Irgi
'''

def gabung_kata(*args):
    kalimat = ""
    for kata in args:
        kalimat += kata + ' '
    return kalimat.strip()
print(gabung_kata("halo","nama","saya","irgi"))

'''
Buat fungsi bernama jumlahkan_semua yang menerima banyak angka dengan *args,
 lalu mengembalikan hasil penjumlahannya.
Contoh pemanggilan:

print(jumlahkan_semua(2, 3, 5, 7))
'''

def jumlahkan_semua(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    print(hasil)
jumlahkan_semua(2,3,5,7)

'''
Buat fungsi bernama kali_semua yang menerima banyak angka dengan *args,
lalu mengembalikan hasil perkaliannya.
Contoh pemanggilan:

print(kali_semua(2, 3, 4))
'''

def kali_semua(*args):
    total = 1
    for angka in args:
        total *= angka
    return total
        
print(kali_semua(2,3,4))

'''
Buat fungsi cari_maksimum yang menerima banyak angka dengan *args,
 lalu mengembalikan angka yang paling besar.
Contoh:

print(cari_maksimum(2, 10, 3, 8, 7))
'''

def cari_maksimum(*args):
    maksimum = args[0]
    for angka in args:
        if angka >= maksimum:
            maksimum = angka
    print(f"angka terbesar adalah {maksimum}")

cari_maksimum(34,8,90,12)

'''
====penjelasan====
✅ Penjelasan singkat:

args[0] → digunakan sebagai nilai awal (sementara dianggap terbesar).
for angka in args: → loop untuk memeriksa semua angka yang dimasukkan.
if angka > terbesar: → kalau ketemu angka yang lebih besar, nilai terbesar diganti.
Setelah loop selesai → variabel terbesar menyimpan angka paling besar.

📌 Output dari kode di atas adalah:

angka terbesar adalah 22
'''

'''
sekarang buat yg versi terkecilnya
'''

def cari_terkecil(*args):
    terkecil = args[0]   # ambil angka pertama sebagai pembanding awal
    for angka in args:
        if angka < terkecil:
            terkecil = angka
    print(f'angka terkecil adalah {terkecil}')

cari_terkecil(10, 5, 22, 7, 13)

'''
contoh soal gabung kata string
'''

def gabung_kata(*args):
    kata = ''
    for kalimat in args:
        kata += kalimat + ' '
    return kata.strip()
print (gabung_kata('irgi','achmad','fahrezi'))    

def gabung_kata(*args):
    kata = ''
    for kalimat in args:
        kata += kalimat + ' '
    return kata.strip()
print(gabung_kata('aksel','raynand'))
