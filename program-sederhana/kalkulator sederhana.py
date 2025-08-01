judul = 'KALKULATOR SEDERHANA'
panjang = len(judul) + 12
print('=' * panjang)
print('=' * 6 + judul + '=' * 6)
print('=' * panjang)


print('\n' + '1. PERTAMBAHAN')
print('2. PENGURANGAN')
print('3. PERKALIAN')
print('4. PEMBAGIAN')

perintah = (input('masukkan perintah (1/2/3/4) = '))

if perintah not in ['1', '2', '3', '4']:
    print('ERROR, PERINTAH YANG DIMASUKKAN SALAH')

else:
    angka1 = float(input('MASUKKAN ANGKA PERTAMA = '))
    angka2 = float(input('MASUKKAN ANGKA KEDUA = '))

    if perintah == '1':
        tambah = angka1 + angka2
        print (f'hasilnya adalah =  {tambah}')

    elif perintah == '2':
        kurang = angka1 - angka2
        print(f'hasilnya adalah = {kurang}')

    elif perintah == '3':
        kali = angka1 * angka2
        print(f'hasilnya adalah = {kali}')

    elif perintah == '4':
        if angka2 != 0:
            bagi = angka1 / angka2
            print (f'hasilnya adalah = {bagi}')
        else:
            print('\nERROR, TIDAK BISA DIBAGI DENGAN 0')

print('\n')
print ( '=' * 31)
print ('=' * 3, 'By. IRGI ACHMAD FAHREZI', '=' * 3)
print ('=' * 31)
    