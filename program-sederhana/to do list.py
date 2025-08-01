daftar_tugas = []
while True:
    print('TO DO LIST')
    print('by. IRGI ACHMAD FAHREZI')
    print(' 1. tambah tugas')
    print(' 2. lihat semua tugas')
    print(' 3. keluar')

    pilihan = (input('masukkan perintah (1/2/3)= '))
    if pilihan == '1':
        tugas = (input('masukkan daftar tugas📜 = '))
        print('tugas sudah berhasil ditambah ✅')
        daftar_tugas.append(tugas)
    elif pilihan == '2':
        if not daftar_tugas :
            print('kamu masih belum memiliki tugas \n ')
        else:
            print('\n📌 Ini adalah daftar tugas kamu:')
            for i, tugas in enumerate(daftar_tugas, start=1):
                print(f'{i}. {tugas}\n')
    elif pilihan == '3':
        print('telah keluar dari program ini')
        break
    else:
        print('perintah yg kamu massukkan salah')