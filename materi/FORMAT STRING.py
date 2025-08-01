# fungsi dari format string adalah untuk mengubah format suatu string menjadi format yang diinginkan
# dan juga untuk mengubah tipe data lain menjadi string

float = 3.14
print("nilai angka float = " + str(float))
# bisa diringkas dengan diformat dan tidak perlu mengetik str()
format_float = f"nilai angka float = {float}"
print(format_float)

# bisa juga dengan tipe data lain 
boolean = True
format_boolean = f"format boleean adalah {boolean}"
print(format_boolean)

# memformat ordo bilangan
angka = 12345678
format_str = f"angka {angka:,}" # menambahkan koma sebagai pemisah ribuan
print(format_str)

# bilangan desimal
angka_des = 3456.5872
format_des = f"angka desimal {angka_des:.3f}" #fungsi dari .3f adalah untuk hanya menampilkan 3 angka dbelakang koma
print(format_des)

# menampilkan leading zero
angka_des = 3456.5872
format_zero = f"angka desimal {angka_des:10.3f}" #fungsi dari :10.3f adalah untuk menampilkan 10 karakter dengan 3 angka dibelakang koma
print(format_zero)# maka akan ditambahkan spasi di depan angka desimal agar total karakter menjadi 10

# menampilkan leading zero dengan format 0
angka_des = 11111.11111
format_des = f"format desimal {angka_des:010.3f}" #""" fungsi dari 010 adalah untuk menampilkan 10 karakter dengan
# angka dibelakang koma dan menambahkan 0 di depan desimal jika jumla karakter kurang dari yang ditentukan"""
print (format_des)

# mwnampilkan nilai plus dan minus
angka = -123
angka2 = 123
format_plus = f"angka {angka:-}" # fungsi dari - adalah untuk menampilkan tanda plus atau minus
format_minus = f"angka minus {angka2:+}" 
print(format_plus)
print(format_minus)

# memformat persentase
persen = 0.750
format_persenn = f"persentase {persen:%}" # fungsi dari :% adalah untuk menampilkan persentase
print(format_persenn)
format_persenn = f"persentase {persen:.2%}" # fungsi dari :.2% adalah untuk menampilkan persentase dengan 2 angka dibelakang koma 
print(format_persenn)

# kita bisa melakukan operasi aritmatika di dalam placeholder atau format string {}
harga = 12000
jumlah = 3
total = f'total harga {harga*jumlah}'
print(total)
total = f'total harga Rp. {harga*jumlah:,}'# jika ingin ditampilkan dengan menggunakan koma
print(total)

# memformat angka lain (binary, octal, hexadecimal

angka = 255
format_biner = f"biner {bin(angka)}" # fungsi dari bin() adalah untuk mengubah angka menjadi biner
print(format_biner)
format_octal = f"octal {oct(angka)}" # fungsi dari oct() adalah untuk mengubah angka menjadi octal
print(format_octal)
format_hexa = f"hexadecimal {hex(angka)}" # fungsi dari hex() adalah untuk mengubah angka menjadi hexadecimal
print(format_hexa)


