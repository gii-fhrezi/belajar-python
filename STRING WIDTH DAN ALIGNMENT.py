# fungsi dari string width dan alignment adalah untuk memberikan lebar dan perataan pada string
nama = 'irgi'
umur = 17
tinggi = 150
sepatu = 41

# string  standard
print (5* '=' + 'standard' + 5* '=')
standard =f"biodata saya adalah {nama}, umur saya {umur} tahun, tinggi saya {tinggi} cm, dan ukuran sepatu saya {sepatu}"
print(standard)

# string multiline dengan format newline (\n)
multiline = f"nama saya adalah {nama}, \numur saya {umur} tahun, \ntinggi saya {tinggi} cm, \nukuran sepatu saya {sepatu}"
print (multiline)

# string multiline dengan format triple quotes (""" """)
print (5* '=' + 'multiline dengan triple quotes' + 5* '=')
multiline = f""" 
nama   = irgi
umur   = 17
tinggi = 150
sepatu = 41
"""
print (multiline)

# mengatur lebar string
datastring = f"""
nama  ={nama:>5}# fungsi dari :>5 adalah untuk mengatur lebar string menjadi 5 karakter dan rata kanan
umur  ={umur:>5}
tinggi={tinggi:>5}
sepatu={sepatu:>5}
"""
print(datastring)