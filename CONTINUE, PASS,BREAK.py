# pass
# fungsinya adalah untuk melewatkan program tersebut tanpa eror

# contoh penggunaan pass
angka = 0
while angka < 5:
    angka += 1
    if angka == 2:
        pass # maka dia tidak akan berfungsi,karena hanya berfungsi hanya sebagai dummy/draft

    print (angka)# hasil print tetap akan menampilkan dari 1-5 karena perintah di line atas adalah pass

# 2. CONTINUE
# fungsi dari continue adalah 
# - Memaksa program langsung melompat ke iterasi berikutnya dalam sebuah loop.
# - Semua kode setelah continue di dalam loop akan dilewati (tidak dijalankan), tapi loop tetap lanjut ke perulangan berikutnya.
print('=== CONTINUE===')
angka = 0
while angka < 10:
    angka += 2
    if angka == 4: # angka 4 tidak akan ditampilkan
        continue
    print('angka sekarang = ', angka)
    print(angka)

print('=' * 12)
print('===BREAK===')
print('=' * 12)

# fungsi dari break adalah untuk Menghentikan perulangan secara paksa.
#Begitu program menemukan break, loop akan langsung berhenti total, meskipun kondisinya belum selesai.

for angka in range(1,20):
    if angka == 12:
        break
    print(angka) # maka angka akan langsung berhenti di 11,karena program menghitung dari 0

while True:
    teks = input('Ketik "stop" untuk keluar: ')
    
    if teks == 'stop':
        print('Program berhenti.')
        break  # force keluar dari loop
    
    print('Kamu mengetik:', teks)

   