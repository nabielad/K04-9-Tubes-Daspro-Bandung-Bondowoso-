#NIM/Nama : 16522076/Kayla Nasywa V
#F16 - Exit

def exit(save):
    meminta_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if meminta_save == 'y' or 'Y' or 'n' or 'N':
        while meminta_save == 'n' or 'N':
            break
        while meminta_save == 'y' or 'Y':
            save = True
            break
    else:
        while meminta_save != 'y' or 'Y' or 'n' or 'N':
            meminta_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
