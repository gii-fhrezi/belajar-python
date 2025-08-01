# memuat gabungan area rentang dari angka
# soal 1
print ("====SOAL 1====")
# +++++3------10++++++
inputuser = float(input("masukkan angka yg bernilai kurang dari 3 atau lebih dari 10: "))
# memeriksa angka kurang dari 3
kurang3 = (inputuser < 3)
print ("angka kurang dari 3 =", kurang3)

# memeriksa angka lebih dari 10
lebih10 = (inputuser > 10)
print ('angka lebih dari 10 =', lebih10)

#memeriksa apakah angka kurang dari 3 atau lebih dari 10
hasil = kurang3 or lebih10
print("angka kurang dari 3 atau lebih besar dari 10 =", hasil)


# soal 2
print ("====SOAL 2====")
# -----3++++++10----------
inputuser = float(input("masukkan angka yg bernilai lebih dari 3 dan kurang dari 10: "))
# memeriksa angka lebih dari 3
lebih3 = (inputuser > 3)
print ("angka lebih dari 3 =", lebih3)

# memeriksa angka kurang dari 10
kurang10 = (inputuser < 10)
print ('angka kurang dari 10 =', kurang10)

#memeriksa apakah angka lebih dari 3 atau kurang dari 10
hasil = lebih3 and kurang10
print("angka lebih dari 3 dan kurang besar dari 10 =", hasil)

print ("====SOAL 3====")
# soal 3
# -----0++++++5------8+++++11--------
inputuser = float(input("masukkan angka yg bernilai \n lebih dari 0 \n dan kurrang dari 5 \n atau lebih dari 8 \n dan kurang dari 11: "))
lebih0 = (inputuser > 0)
print ("angka lebih dari 0= ", lebih0)
kurang5 = (inputuser < 5)
print ("angka kurang dari 5= ", kurang5)
lebih8 = (inputuser > 8)
print ("angka lebih dari 8= ", lebih8)
kurang11 = (inputuser < 11)
print ("angka kurang dari 11= ", kurang11)
# memeriksa apakah angka kurang dari 5 atau lebih dari 0 atau lebih dari 8 atau kurang dari 11
hasil = kurang5 or lebih0 and lebih8 and kurang11
print("angka kurang dari 5 atau lebih dari 0 atau lebih dari 8 atau kurang dari 11 =", hasil)