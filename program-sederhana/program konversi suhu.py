# latihan konversi satuan temperature

# konversi satuan celcius
print ("KONVERSI SATUAN TEMPERATURE CELCIUS")

celcius = float(input("masukkan suhu dalam celcius = "))
print ("suhu adalah", celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print ("suhu adalah", reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print ("suhu adalah", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print ("suhu adalah", kelvin, "kelvin")

# KONVERSI SATUAN FAHRENHEIT
#  UNTUK KONVERSI SATUAN FAHRENHEIT KE KELVIN
# DILAKUKAN DENGAN MENGKONVERSI F KE SATUAN CELCIUS,BARU DIUBAH KE KELVIN
print ("KONVERSI SATUAN FAHRENHEIT KE KELVIN")
fahrenheit_1 = float (input("masukkan suhu dalam fahrenheit = "))

celcius_1 = 5/9 * (fahrenheit_1 - 32)
print ("suhu adalah", celcius_1, "celcius")

reamur_1 = 4/9 * (fahrenheit_1 - 32)
print ("suhu adalah", reamur_1, "reamur")

kelvin_1 = celcius_1 + 273
print ("suhu adalah", kelvin_1, "kelvin")

# KONVERSI SATUAN KELVIN
print ("KONVERSI SATUAN KELVIN")
kelvin_2 = float (input("masukkan suhu dalam kelvin ="))

celcius_2 = kelvin_2 - 273
print ("suhu adalah", celcius_2, "celcius")

reamur_2 = 4/5 * (kelvin_2 - 273)
print ("suhu adalah", reamur_2, "reamur")

fahrenheit_2 = ((9/5) * celcius_2) + 32 
print ("suhu adalah", fahrenheit_2, "fahrenheit")

# KONVERSI SATUAN REAMUR
print ("KONVERSI SATUAN REAMUR")

reamur_3 = float(input("masukkan suhu dalam reamur ="))
print ("suhu adalah", reamur_3, "reamur")

celcius_4 = (5/4) * reamur_3
print ("suhu adalah", celcius_4, "celcius")

fahrenheit_3 = ((9/4) * reamur_3) + 32
print ("suhu adalah", fahrenheit_3, "fahrenheit")

kelvin_3 = ((5/4) * reamur_3) + 273
print ("suhu adalah", kelvin_3, "kelvin")
