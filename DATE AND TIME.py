# date and time
# menggunakan import

import datetime as dt # fungsi dari as dt adalah kita bisa menggunakan fungsi datetime menjadi dt
print(5* '=' + 'APLIKASI PENGHITUNG UMUR' + 5* '=')
print('silahkan masukkan tanggal,bulan dan tahun lahir anda')
tanggal = int(input('tanggal \t= '))
bulan = int(input('bulan \t\t= '))
tahun = int(input('tahun \t\t= '))

tanggalLahir = dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir anda adalah = {tanggalLahir}')

# untuk menebak umur maka kita perlu untuk mengurangkan hari ini dengan tanggal lahir
hariIni = dt.date.today()
print(f'hari ini tanggal {hariIni}')
umur_hari = hariIni - tanggalLahir # hasilnya akan berbentuk hari, maka perlu diubah menjadi tahun dengan cara dibawah
umur_tahun = umur_hari.days // 365 # untuk menebak tahun
umur_bulan = (umur_hari.days %365) // 30  # untuk menebak bulan
print (f'hari anda lahir adalah {tanggalLahir:%A}')
print (f"umur anda adalah {umur_tahun} tahun dan {umur_bulan} bulan")
