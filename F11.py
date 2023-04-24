# NIM/Nama   : 16522022/Nabiel Aufi Danendra
# F11 - Hancurkan Candi

from functions import *
def hancurkancandi(dataCandi):

    # KAMUS LOKAL
    # found : bool
    # id, index : int
    # dataCandi : matrix of integer and string
    # confirm : string

    id = int(input("Masukkan ID candi: "))
    print()

    # searching ID candi dalam dataCandi
    found = False       # inisialisasi state ketemu
    for i in range(length(dataCandi)):
        if id == dataCandi[i][0]:
            index = i
            found = True
            break

    # konfirmasi penghancuran candi
    if found:
        confirm = input(f"Apakah Anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        
        if confirm == "Y" or confirm == "y":
            dataCandi = newpop(dataCandi, dataCandi[index])

        print("Candi telah berhasil dihancurkan")
    else: # not found
        print("Tidak ada candi dengan ID tersebut.")