# membuat segitiga
kode = 0
while True:
    kode += 1
    print('=' * kode)
    if kode > 10:
        break

# hanya print bagian genapnya saja
for  i in range(0,11, 2):
    print('=' * i )

# membuat ketupat
for  i in range(0,11, 2):
    print('=' * i )
kode = 11
while True:
    kode -= 1
    if kode % 2 == 0:
        continue
    print(kode * '=')
    if kode < 2:
        break