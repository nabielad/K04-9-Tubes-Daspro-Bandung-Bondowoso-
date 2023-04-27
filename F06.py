import variables as var
from random import randint

def bangun():
    pasir = randint(1, 5)
    batu = randint(1, 5)
    air = randint(1, 5)
    if pasir > int(var.bahan[1][2]) or batu > int(var.bahan[2][2]) or air > int(var.bahan[3][2]):
        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!")
    else:
        var.bahan[1][2] = str(int(var.bahan[1][2]) - pasir)
        var.bahan[2][2] = str(int(var.bahan[2][2]) - batu)
        var.bahan[3][2] = str(int(var.bahan[3][2]) - air)

        idx = 1
        while var.candi[idx] != None:
            idx += 1
        
        var.candi[idx] = [str(idx),
                          str(var.current_user[0]),
                          str(pasir),
                          str(batu),
                          str(air)]

        var.jumlah_candi += 1

        sisa_candi = 0 if var.jumlah_candi > 100 else (100 - var.jumlah_candi)

        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: " + str(sisa_candi) + ".")