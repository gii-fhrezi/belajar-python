print("*=== kalkulator sederhana ===*")
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")

pilihan =input("masukkan pilihan (1/2/3/4)= ")

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if pilihan == "1":
    hasil = angka1 + angka2
    print("hasil penjumlahan=", hasil)
elif pilihan == "2":
    hasil = angka1 - angka2
    print("hasil pengurangan= ", hasil)
elif pilihan == "3":
    hasil = angka1 * angka2
    print("hasil perkalian=", hasil)
elif pilihan == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil pembagian:", hasil)
    else:
        print("Error: Tidak bisa dibagi dengan nol!")
else:
    print("Pilihan tidak valid.")



