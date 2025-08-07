# copy dictionary

teman_teman = {
	"nama":'irgi',
    'lengkap':'irgi achmad fahrezi',
    'asal':'sinambek',
    'kelamin':'pria'
}
# cara mengcopy yg benar, agar ketika kita mengubah value dari salah satu dict, tidak mengubah value -
# dari dictionary yang dicopy juga
friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["nama"]="irgi achmad"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

print('POP DICTIONARY')
#pop() adalah fungsi bawaan Python yang digunakan untuk menghapus data dari dictionary berdasarkan kunci (key).
# pop dictionary (berdasarkan key)
# pop dictionary adalah menghapus keys dictionary
dataaksel = friends.pop("asal")
print(f"data aksel = {dataaksel}\n")
print(f"friends = {friends}\n")
# maka keys asal akan dipindahkan ke dataaksel

# popitem dictionary (yang terakhir ajah)
# menghapus keys yg terakhir saja
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")