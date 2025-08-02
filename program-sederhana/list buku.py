# membuat daftar buku dari input pengguna

print('============== PROGRAM DAFTAR BUKU ==============')
list_buku = []
while True :
    judul = input('masukkan judul buku \t: ')
    penulis = input('masukkan nama penulis \t: ') 

    buku_baru = [judul,penulis] # membuat list buku dari hasil input pengguna
    list_buku.append(buku_baru) # menambahkan data dari buku baru ke list buku

    print('\n\n', '=' * 10, 'data buku', '='*10)
    for index,buku in enumerate(list_buku):
        print(f'{index+1}  |  {buku[0]}  |  {buku[1]}')

    print('\n\n', '='*20) 
    lanjut = input('apakah anda ingin menambahkan buku lagi ? (y/n) : ')
    if lanjut == 'n':
        break

print('program telah selesai')
