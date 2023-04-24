# NIM/Nama      : 16522022/Nabiel Aufi Danendra
# F04 - Hilangkan Jin

from functions import *
def hapusjin(dataUser, dataCandi):

    # KAMUS LOKAL
    # dataUser, dataCandi : matrix of string and integer
    # username_jin, confirm : string
    # found : bool
    # index : int

    username_jin = input("Masukkan username jin: ")
    print()

    # searching username_jin pada dataUser
    found = False
    for i in range(length(dataUser)):
        if username_jin == dataUser[i][0]:
            index = i
            found = True
            break

    # penghapusan jin dari dataUser
    if found:
        confirm = input(f"Apakah Anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)? ")
        
        if confirm == "Y" or confirm == "y":
            dataUser = newpop(dataUser, dataUser[index])

            # penghapusan candi-candi yang dibuat oleh jin
            for i in range(length(dataCandi)):
                if username_jin == dataCandi[i][1]:
                    dataCandi = newpop(dataCandi, dataCandi[i])

        print("Jin telah berhasil dihapus dari alam gaib.")
    else: # not found
        print("Tidak ada jin dengan username tersebut.")