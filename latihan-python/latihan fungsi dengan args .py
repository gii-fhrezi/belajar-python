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

def gabung_kata(*args):
    hasil = ""
    for kata in args:
        hasil += kata + " "
    return hasil.strip()

print(gabung_kata("Halo", "nama", "saya", "Irgi"))