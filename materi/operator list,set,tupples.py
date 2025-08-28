import os
os.system('cls')
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ['apples','banana','orange','coconut','pineapples']

#  ========================
#  ===== OPERATOR LIST ====
#  ========================
# fruits.append('jagung') adding value in the end
# fruits.insert(2,'semangka') adding value sesuai urutan yang kita perintah
'''angka = [1,2,3]
fruits.extend([angka]) # menambahkan list kedalam list'''
# cara kedua dari extend
# fruits.extend([1,2,3])
# fruits.remove('orange') menghapus salah satu value
# fruits.pop(2) menghapus salah satu value menggunakan index/posisi value
# fruits.clear() mengapus semua value
'''#posisi = fruits.index('coconut') untuk mengetahui posisi dari value kalau list terlalu panjang
#print(posisi)'''
'''jumlahh = fruits.count('apples') untuk menghitung berapa jumlah value yg kita cari di list
print(jumlahh)''' 
'''urutan = fruits.sort() untuk mengurutkan value a-z, 0-9
print(urutan)'''
'''revers = fruits.reverse() untuk memutar balikkan urutan value
print (revers)''' 
'''list_copy = fruits.copy() untuk mengcopy list
print(list_copy)''' 



#  ========================
#  ===== OPERATOR SET ====
#  ========================

angka = {1,2,3,4,5} # ketika datanya adalah string, saat di print maka urutan valuenya akan selalu acak
 
# angka.add(6) menambahkan value
# angka.remove(2) menghapus value (eror jika tidak ada value yg akan dihapus)
# angka.discard(6) menghapus value (tidak akan eror jika tidak ada value yg akan dihapus)
# angka.pop() menghapus value secara acak
# angka.clear() menghapus semua value
# copi = angka.copy() menyalin set
# angka.update([6,7]) mmenambah langsung banyak value




#  ========================
#  ===== OPERATOR TUPPLES ====
#  ========================

warna = ('biru','merah','hijau', 'hijau')
'''hitung = warna.count('hijau') menghitung jumlah value
print(hitung)'''
posisi = warna.index('merah')
print(posisi)
for i in warna:
    print(i)