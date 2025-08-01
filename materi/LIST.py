# list adalah kumpulan data yang ditandai dengan []

# list int
angka = [1,2,5,0,9]
print(angka)

# list str
huruf = ['irgi', 'achmad', 'fahrezi']
print(huruf)

#list boolean
boolean = [True, True,False]
print(boolean)

# list campuran
campur = [1,2,'angka', True, 'irgi', False,1,2,3]
print (campur)

#cara alternatif membuat list
data_range = range (0,10,2) # range (start,stop,steps)
print (data_range)
data_list = list (data_range)#
print(data_list)

# membuat list dengan for loop(list comprehension)
list_for = [i for i in range (0,10)]
print(list_for)
# jika ingin melakukan operasi di dalam list
list_for = [i*2 for i in range (0,10)]
print(list_for)

# membuat list dengan for loop dan if
#hanya menampilkan angka genap
list_if = [i for i in range(0,10) if i %2 ==0 ]
print(list_if)
#hanya menampilkan angka ganjil
list_if = [i for i in range(0,10) if i %2 !=0 ]
print(list_if)

