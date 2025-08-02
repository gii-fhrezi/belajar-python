print('===========PECEL LELE SEDAP GOKIL============')
menu = {
    'nasi putih':7000,
    'nasi kuning':9000,
    'lele':20000,
    'nila':20000,
    'ayam':18000,
    'teh es':7000,
    'es jeruk':10000,
}

print('================ DAFTAR MENU ================')
for item in menu:
    print(f'{item:<15} \tharga :Rp.{menu[item]:,}')# fungsi dari item:<15 adalah untuk rata kiri dengan maksimal 15 karakter
print('pembelian diatas Rp.100.000 mendapatkan diskon 7%')
print('=================================================')
beli = input('pilih menu : ')
jumlah = int(input('jumlah pesanan : '))
bayar = jumlah * menu[beli] # memanggil variable dari inputan pelanggan
if bayar > 100000:
    diskon = bayar * 0.07
    total = bayar - diskon
else:
    total = bayar
# membuat struk belanja
print('================ STRUK PEMBELIAN ================')
print('menu yang dipesan        :', beli)
print('jumlah yang dipesan      :', jumlah)
print(f'total biaya              : {bayar:,}')
print(f'total yang harus dibayar : {total:,}')