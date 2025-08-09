# membuat program dimana sebuah dictionary yg isinya input dari pengguna

import datetime
import os
import string
import random

data_mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

DataDiriMahasiswa = {}
while True:
    os.system('cls') # untuk mengclear tampilan terminal
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print('-' * 20)

    # membuat input pengguna agar masuk ke dict dengan cara 
    mahasiswa = dict.fromkeys(data_mahasiswa_template.keys())# jika di print maka setiap biodata mahasiswa akan none
    #print(mahasiswa)
    # memasukkan biodata mahasiwa
    mahasiswa['nama']=input('nama mahasiswa = ')
    mahasiswa['nim'] =input('masukkan nim = ')
    mahasiswa['sks_lulus']= int(input('masukkan jumlah sks = '))
    TAHUN = int(input('masukkan tahun lahir (0000) = '))
    BULAN = int(input('masukkan bulan lahir (1-12) = '))
    TANGGAL = int(input('masukkan tanggal lahir (00) = '))
    mahasiswa['lahir']=datetime.datetime(TAHUN,BULAN,TANGGAL)

    # agar kita 
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    DataDiriMahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Lahir':<10}")
    print("-"*50)

    for mahasiswa in DataDiriMahasiswa:
        KEY = mahasiswa

        NAMA = DataDiriMahasiswa[KEY]['nama'] 
        NIM = DataDiriMahasiswa[KEY]['nim'] 
        SKS = DataDiriMahasiswa[KEY]['sks_lulus']
        LAHIR = DataDiriMahasiswa[KEY]['lahir'].strftime("%x") 

        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:<10}")
        
    lanjut = input('apakah anda ingin memasukkan data mahasiswa lagi ? (y/n) = ')
    if lanjut == 'n':
        break
    print('\nprogram telah berakhir, terima kasih telah menggunakannya')