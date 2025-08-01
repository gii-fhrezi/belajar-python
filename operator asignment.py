"""operator asignment adalah operator yang digunakan untuk memberikan nilai pada variabel
operator asignment terdiri dari operator penugasan dasar (=) dan operator penugasan gabungan seperti 
+=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>="""

a = 5 # adalah assignment
print("nilai a =", a)

a += 1 # sama dengan a = a + 1
print('nilai a += 1, nilai a sekarang =', a)

a -= 2 # sama dengan a = a - 2
print('nilai a -= 2, nilai a sekarang =', a)

a *= 5 # sama dengan a = a * 5
print('nilai a *= 5, nilai a sekarang =', a)

a /= 2 #artinya a = a / 2
print ('nilai a /= 2, nilai a sekarang =', a)

#operator f;oor division
a = 10
print("\nnilai a =", a)
a //=3 #artinya a = a // 3
print ('nilai a //= 3, nilai a sekarang =', a)

a %= 2 #artinya a = a % 2
print ('nilai a %= 2, nilai a sekarang =', a)

#operator pangkat
a = 5
print("\nnilai a =", a)
a **=2 #artinya a = a ** 2
print ('nilai a **= 2, nilai a sekarang =', a)

#operator bitwise
# and
print("\n====== AND ======")
a = True
print("\nnilai a =", a)
a &= False
print('nilai a &= false, nilai a sekarang =', a)
a = False
print("\nnilai a =", a)
a &= False
print('nilai a &= false, nilai a sekarang =', a)

# or
print("\n====== OR ======")
a = True
print("\nnilai a =", a)
a |= False
print('nilai a |= false, nilai a sekarang =', a)
a = False
print("\nnilai a =", a)
a |= False
print('nilai a |= false, nilai a sekarang =', a)

# xor
print("\n====== XOR ======")
a = True
print("\nnilai a =", a)
a ^= False
print('nilai a ^= false, nilai a sekarang =', a)
a = True
print("\nnilai a =", a)
a ^= True
print('nilai a ^= true, nilai a sekarang =', a)

# operator left shift
print("\n====== RIGHT SHIFT ======")
a = 0b0100
print('\nnilai a =', format(a, '04b'))
a >>= 2 #artinya a = a >> 2
print('\nnilai a >>= 2','nilai a menjadi', format(a, '04b'))

print("\n====== LEFT SHIFT ======")
a <<= 1 #artinya a = a << 1
print('\nnilai a <<= 1','nilai a menjadi', format(a, '04b'))



 