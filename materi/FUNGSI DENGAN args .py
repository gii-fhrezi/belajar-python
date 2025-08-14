'''
*args di Python adalah cara untuk membuat fungsi yang bisa menerima jumlah argumen yang tidak terbatas 
tanpa harus menentukan jumlahnya satu per satu di definisi fungsi.

-Penjelasan Singkat-

*args akan mengumpulkan semua argumen tambahan yang dikirim ke fungsi menjadi sebuah tuple.
Sangat berguna kalau kita tidak tahu berapa banyak nilai yang akan dimasukkan pengguna.
'''

# memasukan data/argument
# contoh kasus yang tidak menggunakan args
# hanya bisa memasukkan 3 argumen saja
def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",100,120])

# jika dibuat dengan args
# maka kita bebas ingin membuat berapapun argumen yang dibutuhkan

def fungsi(*args): #*args bisa diganti dengan kata apapun,asalkan masih ada * didepannya
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",120,120)

# studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    
    return output
# bisa dengan 9 nilai
hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")
 
# bisa dengan 3 nilai 
hasil = tambah(10,5,15)
print(f"hasil = {hasil}")