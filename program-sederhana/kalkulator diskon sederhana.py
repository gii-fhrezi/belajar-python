# untuk menghitung diskon
# meminta input harga belanja pelanggan
# daftar diskon
# Rp.500.000,00 = 30%
# Rp.300.000,00 = 20%
#Rp. 150.000,00 = 7%

print('=' * 21)
print('PROGRAM HITUNG DISKON')
print('=' * 21)

total = float(input('MASUKKAN TOTAL BELANJAAN ANDA DALAM RUPIAH (cth, 12000) = '))
print('\n')
if total > 499000:
    diskon = 0.30
    print('SELAMAT KAMU DAPAT DISKON 30%')
elif total > 299000:
    diskon = 0.20
    print('SELAMAT KAMU DAPAT DISKON 20%')
elif total > 149000:
    diskon = 0.07
    print('SELAMAT KAMU DAPAT DISKON 7%')
else:
    diskon = 0
    print('KAMU TIDAK MENDAPATKAN DISKON')
print ('\n')
if diskon > 0:
    harga_diskon = total * diskon
    total_diskon = total - harga_diskon
    print('\n')
    print(f'kamu mendapatkan diskon sebesar = Rp.{harga_diskon:,}')
    print(f'harga yang harus dibayar = Rp.{total_diskon:,}')

print ('=' * 30)
print('By. IRGI ACHMAD FAHREZI')
print ('=' * 30)
