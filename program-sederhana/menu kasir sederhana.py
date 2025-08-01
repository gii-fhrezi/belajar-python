# Program menu kasir sederhana
riwayat_transaksi = [] # membuat list kosong yang tujuannya untuk menyimpan riwayat belanja
while True:  # while loop utama
    print("\n==== MENU KASIR ====")
    print ('=' * 30)
    print('By. IRGI ACHMAD FAHREZI')
    print ('=' * 30)
    print("1. hitung total belanja")
    print("2. masukkan kode diskon")
    print("3. Placeholder (pass)")
    print('4. lihat riwayat total belanja')
    print("5. Keluar")

    print('kode diskon hari ini adalah = python')
    pilihan = input('pilih menu yang ingin anda gunakan (1/2/3/4/5) = ')

    if pilihan == "1":
        total = 0
        print ('\ncontoh memasukkan harga item = 12000')
        for i in range (1,6):
            harga = float(input(f'masukkan harga item ke {i} =Rp. '))
            if harga == 0:
                print('barang ini gratis,tidak perlu bayar')
                continue
        total += harga
        print(f'total belanjaan kamu adalah Rp.{total:,} ')
        riwayat_transaksi.append(total) # fungsinya adalah untuk menambahkan total harga ke list riwayat transaksi
    elif pilihan == '2':
        diskon = input('masukkan kode diskon disini: ')
        if diskon == 'python':
            print('\nselamat kamu mendapat diskon sebesar 15% \n ')
            total = 0
            print ('\ncontoh memasukkan harga item = 12000')
            for i in range (1,6):
                harga = float(input(f'masukkan harga item ke {i} =Rp. '))
                total += harga
                diskon = 0.15
                harga = total * diskon 
                harga_diskon = total - harga
                print('=' * 20)
                print(f'total belanjaan kamu sebelum diskon =Rp.{total:,} ')
                print(f'total diskon = Rp.{harga:,}')
                print(f'total belanja setelah mendapat diskon = Rp.{harga_diskon:,}')
                print('=' * 20)
                riwayat_transaksi.append(harga_diskon)
        else:
            print('\nkode diskon yang dimasukkan salah')
    elif pilihan =='3':
        print('nantikan update selanjutnyaaaaaa')
    elif pilihan =='4':
        print("\n===RIWAYAT TOTAL BELANJA===")
        if not riwayat_transaksi:
            print('belum ada transaksi')
        else:
            for idx, nilai in enumerate(riwayat_transaksi, start=1):
                print(f'transaksi {idx}: Rp. {nilai:,}')
    elif pilihan =='5':
        print('program telah berhenti, terima kasih telah menggunakan program ini')
    else:
        print('perintah yang dimasukkan salah')
    