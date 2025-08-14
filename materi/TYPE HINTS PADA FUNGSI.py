''' Type hints untuk fungsi '''
#Type hints adalah cara untuk memberi tahu tipe data yang ddigunakan oleh sebuah fungsi


'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("irgi")
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("Ucup")