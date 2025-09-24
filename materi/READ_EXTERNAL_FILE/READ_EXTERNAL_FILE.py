# membaca file dari luar/external

print('='* 5, " READ EXTERNAL FILE ", '='*5)

file = open("file.txt", mode="r") # membuka file.txt dengan mode read saja

# untuk mengecek apakah file nya bisa di read atau di write/edit
print(f'status read: {file.readable()}')
print(f'status write: {file.writable()}')

# baca seluruh  isi file
# print(file.read())

# baca per baris
# print(file.readline()) # print bris pertama
# print(file.readline()) # print baris kedua

# baca semua baris sebagai list
print(file.readlines())

#setiap setelah membuka file kita harus menutupna agar tidak error
file.close() # untuk menutup file
print(f'apakah file sudah di close? :{file.closed}')

# ada teknik lain agar file ini bisa menutup dengan otomatis yaitu

with open("file.txt",mode="r") as file:
    content = file.readline()
    print(content,end="") # fungsi dari end="" adalah uuntuk menghilangkan enter saat di print
    print(f"apakah file sudah diclose? :{file.closed}")

# maka file sudah diclose dengan otomatis
print(f"apakah file sudah diclose? :{file.closed}")

