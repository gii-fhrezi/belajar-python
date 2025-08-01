# nested list adalah list di dalam list
list1 = [1,2,3,4]
list2 = [3,1,2,4]
list_gabung = [list1, list2]
print(list_gabung)

# contoh penggunaan
peserta0 = ['irgi', 18 , 'pria']
peserta1 = ['achmad' , 20 , 'pria']
peserta2 = ['fahrezi', 18, 'pria']

list_peserta = [peserta0, peserta1, peserta2]
print(f'ini adalah daftar peserta = {list_peserta}')

for peserta in list_peserta:
    print(f'nama\t: {peserta[0]}')
    print(f'umur\t: {peserta[1]}')
    print(f'kelamin\t: {peserta[2]}\n')