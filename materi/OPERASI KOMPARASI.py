# operasi komparasi atau perbandingan
# setiap hasil dari operasi komparasi adalah boolean (true dan false)
# >,<,<=,>=,==,!=,is,is not
print ('===OPERASI KOMPARASI===')

a = 4
b = 2

# lebih dari (>)
# memulai mengambil persamaan mulai dari setelah angka di variabel(3,maka akan memulai dari 3.00001)
print ('===lebih dari (>)===')
hasil = a > 3
print (a,'>',3, '=', hasil )
hasil = b > 3
print (b,'>',3, '=', hasil)
hasil = b > 2
print (b, '>',2, '=', hasil)

# kurang dari (<)
print ('===kurang dari (<)===')
hasil = a < 3
print (a,'<',3, '=', hasil )
hasil = b < 3
print (b,'<',3, '=', hasil)
hasil = b < 2
print (b, '<',2, '=', hasil)

# lebih dari sama dengan (>=)
# memulai mengambil persamaan mulai langsung dari angka di variabel(3,maka akan mengambil langsung 3)
print ('===lebih dari sama dengan (>=)===')
hasil = a >= 3
print (a,'>=',3, '=', hasil )
hasil = b >= 3
print (b,'>=',3, '=', hasil)
hasil = b >= 2
print (b, '>=',2, '=', hasil)

# kurang dari sama dengan(<=)
print ('===kurang dari sama dengan(<=)===')
hasil = a <= 3
print (a,'<=',3, '=', hasil )
hasil = b <= 3
print (b,'<=',3, '=', hasil)
hasil = b <= 2
print (b, '<=',2, '=', hasil)

# sama dengan(==)
print ('====sama dengan(==)===')
hasil = a == 4
print (a,'==',4, '=', hasil )
hasil = b == 4
print (b,'==',4, '=', hasil)

# tidak sama dengan(!=)
print ('====tidak sama dengan(!=)===')
hasil = a != 4
print (a,'!=',4, '=', hasil )
hasil = b != 4
print (b,'!=',4, '=', hasil)

# is dan is not digunakan sebagai komparasi object identity (variabel)
# digunakan untuk membandingkan nilai objek (variable)
print ('=== sama dengan(is)===')
x = 4
y = 4
z = 5
hasil = x is y
print ("x =", x)
print ("y =", y)
print ("z =", z)
print('x is y =', hasil)
hasil = x is z
print ('x is z =', hasil)

print ('===tidak sama dengan(is not)===')
x = 4
y = 4
z = 5
hasil = x is not y
print('x is not y =', hasil)
hasil = x is not z
print ('x is not z =', hasil)