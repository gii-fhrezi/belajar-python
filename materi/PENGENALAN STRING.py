# pengenalan string
# string adalah urutan karakter yang digunakan untuk menyimpan dan memanipulasi teks
# string dapat dibuat menggunakan tanda kutip tunggal (' ') atau tanda kutip ganda (" ")

# 1. cara membuat string
a = 'ini adalah string'
b = "ini juga string"
print ("'halo apa kabar'")
print ('"halo apa kabar"')

#2. menggunakan backslash (\) untuk menghindari karakter khusus
# fungsinya adalah untuk karakter khusus dapat ditampilkan sebagai karakter biasa
print ('mari shalat jum\'at')
print ('g\'day isn\'t it?')
print ("g'day isn't it?")

# untuk memberikan fungsi tab 
print ('kata ini, \t semakin jauhan')
print ('kata ini, \t\t\t semakin jauhan')

# untuk memberikan fungsi backspace
print ('kata ini, \b jadi dekat')

# untuk memberikan fungsi newline
print ('kata ini, \n jadi di bawah') # -> LF (line feed) digunakan di linux dan macOS
print ('kata ini, \r jadi di bawah') #->CR (carriage return) digunakan di windows
print ('kata ini, \r\n jadi di bawah') # -> CRLF (carrriage return line feed) digunakan di windows

# 3. string literal atau raw string
# string literal atau raw string adalah string yang tidak memproses karakter khusus

print (r'ini adalah string literal, karakter khusus seperti \n, \t, \b, tidak akan diproses')

#  string multiline
# string multiline dapat dibuat menggunakan triple quotes (''' ''' atau """ """)
print ('''
       baris pertama
       baris kedua
       ''')


