# operator bitwise, operasi biner
# Operasi bitwise digunakan untuk melakukan operasi pada level bit dari bilangan bulat.
# or, and, xor, not, left shift, right shift
a = 9
b = 5

#bitwise or (|)
c = a | b 
print ("\n====== OR ======")
print("nilai =", a, ", binary = ", format(a, '08b'))
print ("nilai =", b, ", binary = ", format(b, '08b'))
print ('===================(|)')
print ("nilai =",c,", binary = ", format(c, '08b'))

#bitwise and (&)
c = a & b 
print ("\n====== AND ======")
print("nilai =", a, ", binary = ", format(a, '08b'))
print ("nilai =", b, ", binary = ", format(b, '08b'))
print ('===================()')
print ("nilai =",c,", binary = ", format(c, '08b'))

#bitwise xor (^)
c = a ^ b 
print ("\n====== XOR ======")
print("nilai =", a, ", binary = ", format(a, '08b'))
print ("nilai =", b, ", binary = ", format(b, '08b'))
print ('===================(^)')
print ("nilai =",c,", binary = ", format(c, '08b'))

#bitwise not (~)
c = ~a
print ("\n====== NOT ======")
print("nilai =", a, ", binary = ", format(a, '08b'))
print ("nilai =", b, ", binary = ", format(b, '08b'))
print ('===================(~)')
print ("nilai =",c,", binary = ", format(c, '08b'))
print ('===================(^)')
d = 0b0000001001
e = 0b1111111111
print ('nilai =',e^d,' , binary = ', format(e^d, '08b'))

#bitwise left shift (<<)
c = a << b 
print ("\n====== << ======")
print("nilai =", a, ", binary = ", format(a, '08b'))
print ("nilai =", b, ", binary = ", format(b, '08b'))
print ('===================(<<)')
print ("nilai =",c,", binary = ", format(c, '08b'))

#bitwise right shift (>>)
c = a >> b
print ("\n======  >>  ======")
print("nilai =", a, ", binary = ", format(a, '08b'))
print ("nilai =", b, ", binary = ", format(b, '08b'))
print ('===================(>>)')
print ("nilai =",c,", binary = ", format(c, '08b'))