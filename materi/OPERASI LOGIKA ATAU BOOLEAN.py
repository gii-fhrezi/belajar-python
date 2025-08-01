# operasi logika atau boolean
#operasi yang digunakan untuk membandingkan nilai boolean (True atau False).
# not, and, or, xor

# not (akan menghasilkan kebalikan dari nilai boolean)

a = True
b = False
c = not a

print("==== NOT ====")

print("data a =", a)
print("data b =", b)
print("data c =", c)

# or (akan menghasilkan True jika salah satu operasinya True)
print("\n==== OR ====")
a = False
b = False
c = a or b
print(a, "or", b, "=", c)

a = True
b = False
c = a or b
print(a, "or", b, "=", c)

a = False
b = True
c = a or b
print(a, "or", b, "=", c)

a = True
b = True
c = a or b
print(a, "or", b, "=", c)

# and (akan menghasilkan false jika salah satu operasinya False)
print("\n==== AND ====")
a = False
b = False
c = a and b
print(a, "and", b, "=", c)

a = True
b = False
c = a and b
print(a, "and", b, "=", c)

a = False
b = True
c = a and b
print(a, "and", b, "=", c)

a = True
b = True
c = a and b
print(a, "and", b, "=", c)

# xor (akan menghasilkan True jika salah satu operasinya True)
# xor (akan menghasilkan false jika kedua operasinya sama)
# xor ditandai dengan simbol (^)
print("\n==== XOR ====")
a = False
b = False
c = a ^ b
print(a, "^", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "^", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "^", b, "=", c)

a = True
b = True
c = a ^ b
print(a, "^", b, "=", c)