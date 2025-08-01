# operasi data
# index atau posisi dari tiap data adalah
#        0          1          2
data = ['irgi', 'achmad', 'fahrezi']
# index dari belakang
#        -3         -2          -1
data = ['irgi', 'achmad', 'fahrezi']

# mengambil salah satu data dari list 
ambil = data[0] # maka akan mengambil data pertama yaitu irgi
print (ambil)

ambil = data[1]
print(ambil)

# jika ingin langsung mengambil data terakhir
ambil = data[-1]
print(ambil)

# mengambil info jumlah data dalam list
panjang = len(data)
print(panjang)

# manipulasi data list
# menambahkan item sesuai posisi list
print(f'ini adalah data sebelum di ubah =\n {data}')
data.insert(1,'aksel')# data.insert (posisi yg akan ditambah, data yg akan ditambah)
print(f'ini adalah data sesudahh di ubah =\n {data}')


# # menambah data di akhir list
data.append('raynand')
print(f'ini adalah data sesudah menambahkan data lagi di akhir =\n {data}')

# menambahkan list di dalam list
data2 = ['aksel', 'raynand']
data.extend(data2)
print(f'ini adalah data sesudah menggabungkan dua list = \n {data}')

#merubah data
data[2]='hai' # data[posisi data yg akan diubah]
print(f'ini adalah data setelah (achmad) di ubah = \n{data}')

#menghapus data dalam list
data.remove('hai')
print(f'ini adalah data setelah (hai) di hapus = \n{data}')

#menghapus data paling belakang
data.pop()
print(f'ini adalah data sesudah yg paling akhir di hapus = \n {data}')

# menghitung jumlah data pada list
data = [1,8,9,0,7,6,8,6,5,5,5,4,4,3,8,9,1]
print  ('\n', data)
banyak1 = data.count(5) # menghitung berapa jumlah angka 5 di dalam list
print(f'banyak angka 5 pada list adalah = {banyak1}')

#mengambil posisi data(index)
datahuruf = ['irgi', 'achmad','fahrezi','aksel','raynand']
print (datahuruf)
indexirgi = datahuruf.index('irgi')# mencari posisi irgi di dalam list
print('posisi irgi di dalam list adalah = ', indexirgi)

# mengurutkan list
data = [1,8,9,0,7,6,8,6,5,5,5,4,4,3,8,9,1]
datahuruf = ['irgi', 'achmad','fahrezi','aksel','raynand']
print(f'ini adalah list sebelum di urutkan = \n{data} \n {datahuruf}')
data.sort() # untuk melakukan sorting list tidak diperlukan membuat variable baru
datahuruf.sort()
print(f'ini adalah data sesudah diurutkan = \n{data} \n {datahuruf} ')

#memutar balikkan list
# untuk melakukan operasi ini,list harus diurutkan dari yg terkecil terlebih dahulu
data.reverse()
datahuruf.reverse()
print('ini adalah data sesudah di reversi = \n' , data)
print('ini adalah data sesudah di reversi = \n' , datahuruf)

