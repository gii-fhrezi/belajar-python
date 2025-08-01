# teknik mengcopy list
a = ['irgi', 'achmad', 'fahrezi', 'aksel','raynand']
b = a.copy()
print(a)
print('\n', b)
# kita coba udah data di salah satu list, apakah semua list akan kena dampaknya
a[0] = 'aksel'
print(a) 
print('\n' , b)

