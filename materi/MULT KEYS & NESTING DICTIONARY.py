import datetime # fungsinya adalah untuk mengambil fungsi tanggal lahir

mahasiswa1 = {
	'nama':'irgi',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
	'nama':'fahrezi',
	'nim':'19022002',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
	'nama':'ohim',
	'nim':'19022003',
	'sks_lulus':100,
	'beasiswa':False,
	'lahir':datetime.datetime(2000,2,29)
}

# membuat dictionary di dalam dictionary
data_mahasiswa = {
	'MAH001':mahasiswa1,
	'MAH002':mahasiswa2,
	'MAH003':mahasiswa3
}

# kita akan membuat agar tampilannya menjadi seperti database
# fungsi dari (:<6) adalah rata kiri  
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

# sekarang kita akan mengeluarkan semua keys dan value dari dictionary data_mahasiswa
for mahasiswa in data_mahasiswa:
	KEY = mahasiswa

	NAMA = data_mahasiswa[KEY]['nama'] #berfungsi untuk mengambil nilai nama dari -
	NIM = data_mahasiswa[KEY]['nim'] #dictionary mahasiswa berdasarkan kunci KEY dan menyimpannya ke dalam variabel NAMA.
	SKS = data_mahasiswa[KEY]['sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['beasiswa']
	LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") # fungsinya adalah ketika di print nanti agar formatnya 12/09/07

	print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")