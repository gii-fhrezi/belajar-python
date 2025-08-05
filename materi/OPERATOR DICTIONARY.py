# operator dictionary

data_dict = {
	"nama":"irgi",
	"umur":17,
	"asal":"sinambek"
}

# panjang dictionary
# fungsinya adalah untuk mengecek panjang dari dictionary tersebut 
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek apakah key(data) ada di dalam list atau tidak
KEY = "nama"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["nama"]) # operator ini langsung error jika key(value) tidak ada
print(data_dict.get("nama"))# bedanya dengan yg atas adalah jika tidak ada key maka tidak eror dan akan mengeprint`None`.

print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan 

# mengupdate data / menambahkan data
data_dict["nama"] = "fahrezi"
print(data_dict)
data_dict["bulan"] = "september"# jika key yg akan diubah tidak ada, maka akan langsung ditambahkan ke dalam dict
print(data_dict)

data_dict.update({"nama":"irgi"})
print(data_dict)
data_dict.update({"hobi":"tidur"}) # jika key tidak ada maka akan otomatis ditambahkan
print(data_dict)

# mendelete data pada dictionary
del data_dict["hobi"]
print(data_dict)