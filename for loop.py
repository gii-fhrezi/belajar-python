# loop (pengulangan)
# contoh kodenya seperti ini
# for kondisi:
#    aksi

# loop dengan list
angka_list = [1,2,3,4,5]
print(angka_list)

for i in angka_list:
    print(f'i sekarang --> {angka_list}')
print (10 * '=', '\n') 

for i in angka_list:
    print(f'i sekarang --> {i}') # i akan melakukan print setiap data yg ada 
print (10 * '=', '\n') 
# dengan range
angka_range = range(6)#maka akan melakukan print dari 0-5
print (10 * '=', '\n') 
for i in angka_range:
    print (f'i sekarang --> {i}')

print('\n')
angka_range = range (1,9) # akan melakukan print dari satu sampai delapan(karena dimulai dari 0)
for i in angka_range:
    print(f'i sekarang --> {i}')

# kita bisa bebas memasukkan kata apa saja  dalam loop
angka_range = range (1,5)
for i in angka_range:
    print (f'IRGI ACHMAD FAHREZI')

# loop menggunakan data string

data_str = 'IRGI ACHMAD FAHREZI'
for huruf in data_str: # huruf akan menjadi value
    print(huruf)

# bisa juga melakukan tambah,kali,bagi,kurang
for i in range(1,6):
    print ('*' * i)

for i in range(1,11):
    print(i)

nama = input('masukkan teks: ')
for i in range(1,6):
    print(nama)


