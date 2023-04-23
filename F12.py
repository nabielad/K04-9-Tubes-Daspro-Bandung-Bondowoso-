#NIM/Nama : 16522076/Kayla Nasywa V
#F12 - Ayam Berkokok

def EOP(var):
    return var == None

def hitungCandi(candi,celah):
    kondisi = True
    banyak = 0 # jumlah total candi
    i = banyak
    
    while (kondisi) :
        if EOP(candi[i+1]) :
            kondisi = not(kondisi)
        elif(candi[i+1][1] != celah):
            candi[i+1][2] = int(candi[i+1][2])
            candi[i+1][3] = int(candi[i+1][3])
            candi[i+1][4] = int(candi[i+1][4])
            banyak += 1
        i += 1
    return banyak


def ayamBerkokok(candi):
    celah = -1
    N = hitungCandi(candi,celah)
    print("Kukuruyuk.. Kukuruyuk.. \n")
    print("Jumlah Candi: " + N + "\n")

    while N == 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        break
    if N < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        