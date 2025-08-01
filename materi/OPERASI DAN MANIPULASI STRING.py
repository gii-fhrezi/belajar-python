# operasi dan manipulasi string

# 1. untuk menyambung string
# menggunakan operator +
nama_depan = "irgi"
nama_tengah = "achmad"
nama_belakang = "fahrezi"

nama_lengkap = nama_depan + nama_tengah + nama_belakang
print("nama lengkap =" + nama_lengkap)

# cara menambahkan spasi
nama_lengkap = nama_depan +" "+ nama_tengah +" "+ nama_belakang
print("nama lengkap dengan spasi = " + nama_lengkap)

#2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari nama lengkap adalah", str(panjang))#tidak bisa menggunakan operator (+) untuk menggabungkan string dengan integer

#3. operator dalam string
# mengecek apakah ada komponen character dalam string
i = "i"
status = i in nama_lengkap
print(i + " ada di " + nama_lengkap + "=" + str(status))

I = "I"
status = I in nama_lengkap
print(I + " ada di " + nama_lengkap + "=" + str(status))# false karena huruf yan digunakan adalah kapital

i = "i"
status = i not in nama_lengkap
print(i + " tidak ada di " + nama_lengkap + "=" + str(status))

# mengulang string
# menggunakan operator (*)
ulang = nama_depan * 3
print("nama depan diulang 3 kali =" + ulang)
print("wk" *3)
# mengulang string dengan spasi
ulang = (nama_depan + " ") * 3
print("nama depan diulang dengan spasi = " + ulang)

# indeksing string
# indeksing adalah cara untuk melihat karakter pada posisi tertentu dalam string
# indeks dimulai dari 0
# indeks menggunakan operator ( [] )
print("indeks ke-0 dari nama lengkap adalah =" + nama_lengkap[0])
print("indeks ke -1 dari nama lengkap adalah =" + nama_lengkap[-1]) # indeks -1 dimulai dari karakter terakhir
print("indeks k-0:4 dalam =" + nama_lengkap[0:5])
print("indeks k-4:7 dalam =" + nama_lengkap[4:8])# sampai indeks ke-7 tidak termasuk
print("indeks ke-[0,2,4,6,8,10] dalam =" + nama_lengkap[0:11:2]) # indeks ke-0,2,4,6,8,10

# item paling kecil dan paling besar
# menggunakan fungsi (min) dan (max)
print("item paling kecil dalam " + nama_lengkap + " adalah " + min(nama_lengkap))# yang paling kecil adalah spasi
print("item paling besar dalam " + nama_lengkap + " adalah " + max(nama_lengkap))# yang paling besar adalah z

# operator dalam bentuk method
data = "irgi achmad fahrezi"
jumlah = data.count("i") # menghitung jumlah karakter i
print("jumlah huruf i dalam " + data + " adalah " + str(jumlah))

# operator dalam method
# merubah case dari string
nama = "irgi achmad fahrezi"
nama = nama.upper() # merubah semua huruf menjadi kapital
print('nama dalam huruf kapital =' + nama)
nama = nama.lower() # merubah semua huruf menjadi huruf kecil
print ('nama dalam huruf keci =' + nama)

# pengecekan dengan isx method
# contoh pengecekan lowercase dan uppercase
nama = "IRGI ACHMAD FAHREZI"
nama_besar = nama.isupper() # untuk mengecek apakah semua huruf dalam string adalah kapital
print(nama + " adalah huruf kapital? = " + (str(nama_besar)))
nama_kecil = nama.islower() # untuk mngecek apakah semua huruf dalam string adalah huruf kecil
print(nama + " adalah huruf kecil? =" + (str(nama_kecil)))

# isalpha() untuk mengecek apakah semua huruf
# isalnum() untuk mengecek apakah semua huruf dan angka
# isdecimal() untuk mengecek apakah semua karakter adalah angka
# isspace() untuk mengecek apakah semua karakter adalah spasi (spasi, tab, newline \n)
# isdigit() untuk mengecek apakah semua karakter adalah digit (angka)
# istitle() untuk mengecek apakah semua dimulai dari huruf kapital

judul = "Belajar Python Dasar"
judul_title = judul.istitle() # untuk mengecek apakah setiap kata dimulai dengan huruf kapital
print(judul + " apakah judul ini adalah title? = " + str(judul_title))

#ngecek komponen startswith dan endswith
judul = "belajar python dasar"
awal = judul.startswith("belajar") # untuk mengecek apakah string dimulai dengan kata tertentu
print(judul + " apakah dimulai dengan kata belajar ? =" + str(awal))
# versi lebih sederhana tanpa variabel
awal_langsung = "belajar python dasar".startswith("python")
print(judul + " apakah dimulai dengan kata python ? =" + str(awal_langsung))

judul = "belajar python dasar"
akhir = judul.endswith("dasar") # untuk mengecek apakah string diakhiri dengan kata tertentu
print(judul + " apakah diakhiri dengan kata dasar ? =" + str(akhir))
#versi sederhana
akhir_langsung = "belajar python dasar".endswith("belajar")
print(judul + " apakah diakhiri dengan kata belajar ? = " + str(akhir_langsung))

# pengggabungan komponen string
pisah = ['irgi', 'achmad', 'fahrezi']
gabung = ' '.join(pisah) # untuk menggabungkan karakter spasi dalam setiap list
print(pisah)
print(gabung)
gabung = '111'.join(pisah) # untuk menggabungkan karakter 111 dalam setiap list
print(gabung)

# memisahkan komponen string
gabung = 'irgi111achmad111fahrezi'
pisah = gabung.split("111") # untuk memisahkan string dari karakter yg ada di dalam kurung
print(gabung)
print(pisah) # hasilnya adalah list
pisah = gabung.split("i") # untuk memisahkan string dari karakter yg ada di dalam kurung
print(pisah)

# melakukan rata kanan, kiri, dan tengah
# menggunakan method (ljust, rjust, center)
kanan = "kanan".rjust(20) # untuk melakuka rata kanan
print('"' + kanan + '"')
kiri = "kiri".ljust(20,"=") # untuk melakuka rata kiri
print('"' + kiri + '"')
tengah = "tengah".center(20,"^") # untuk melakuka rata tengah
print('"' + tengah + '"')

