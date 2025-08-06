# looping dictionary

teman_teman = {
	'awal':'irgi',
	'tengah':'achmad',
	'akhir':'fahrezi'
}

# looping first try (yang keluar hanya key nya saja, dan valuenya tidak keluar)

for teman in teman_teman:
	print(teman)

# operator untuk mengambil item / iterables
# untuk mengambil keys nya saja
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
	print(teman_teman.get(key))

# untuk mengambil values nya saja
values = teman_teman.values()
print(values)

for value in teman_teman.values():
	print(value)

# untuk mengambil key dan value nya
items = teman_teman.items()
print(items)

for item in teman_teman.items():
	print(item)

# cara lain untuk mengambil key dan valuenya
for key,value in teman_teman.items():
	print(f"key = {key}, value = {value}")