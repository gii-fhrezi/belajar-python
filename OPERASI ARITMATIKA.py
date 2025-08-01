# operasi aritmatika
print ("===operasi aritmatika===")
a = 12
b = 5

# operasi tambah
hasil = a + b
print (a, '+',b,'=', hasil)

#operasi kurang
hasil = a - b
print (a, '-',b,'=', hasil)

#operasi kali
hasil = a * b
print (a, '*',b,'=', hasil)

#operasi bagi
hasil = a / b
print (a, '/',b,'=', hasil)

#operasi eksponen (pangkat)
hasil = a ** b
print (a, '**',b,'=', hasil)

#operasi modulus (sisa pembagian)
hasil = a % b
print (a, '%',b,'=', hasil)

#operasi floor division (membuang bagian desimal dan hanya mengambil angka bulat paling bawah.)
hasil = a // b
print (a, '//',b,'=', hasil)

# prioritas operasi
#1. ()
#2. eksponen **
#2. bagi dan kali,dll * / // % 
#3. tambah dan kurang + - 

x = 3
y = 2
z = 5

# contoh soal prioritas
hasil = x / y + y % z ** x // z
print (x, '/', y, '+', y, '%', z, '**', x, '//', z, '=', hasil)