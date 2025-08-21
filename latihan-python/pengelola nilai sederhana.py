import os
os.system('cls')

def nilai_mahasiswa(*args,**kwargs):
    total = 0 
    for nilai in args:
        total += nilai
    rata2 = total /len(args) if args else 0
    print("===== DATA MAHASISWA =====")
    for key,value in kwargs.items():
        print(f'{key}: {value}')
    print(f'/n Nilai = {args}')
    print(f'Rata Rata nilai = {rata2:.2f}')

nilai_mahasiswa(
    90,89,76,89,90,
    nama = 'irgi achmad fahrezi',
    nim = '122007',
    jurusan = 'teknik informatika'
        )