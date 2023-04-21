# F10 - Ambil Laporan Candi
# Nama/Nim : Andrew/ 16522040

def EOP(var):
    return var == None

def hitungCandi(candi,celah):
    kondisi = True
    banyak = 0 # jumlah totl jin
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

def hitungBahanCandi(candi, jenisBahan, N, celah):
    jumlah = 0
    indeksBahan = 0
    if(jenisBahan == 'pasir'):
        indeksBahan = 2
    elif(jenisBahan == 'batu'):
        indeksBahan = 3
    else:
        indeksBahan = 4
    
    i = 1
    while(not(EOP(candi[i]))):
        if(candi[i][1] != celah):
            jumlah += int(candi[i][indeksBahan])
        i += 1
    return jumlah
    
def hargaCandi(candi, jenisHarga, celah):
    idCandi = '-'
    harga = 0
    if(jenisHarga == 'Termurah'):
        harga = 5*10000 + 5 *15000 +5*7500
    
    i = 1
    while(not(EOP(candi[i]))):
        if(candi[i][1] != celah):
            pasir = candi[i][2]
            batu = candi[i][3]
            air = candi[i][4]
            hargaTemp = pasir*10000 + batu*15000 + air*7500
            if(jenisHarga == 'Termahal' and hargaTemp > harga):
                harga = hargaTemp
                idCandi = candi[i][0]
            elif(jenisHarga == 'Termurah' and hargaTemp < harga):
                harga = hargaTemp
                idCandi = candi[i][0]
        i += 1
    print(idCandi,end="")
    if(idCandi != '-'):
        print("(Rp "+str(harga)+")")
    print()                
    return

def laporancandi(candi):
    celah = '-1' # celah bermaksud saat candi di hapus dari data ada celah anatar candi di data
    N = hitungCandi(candi,celah) #jumlah Candi total
    print("> Total Candi: ", N)
    print("> Total Pasir yangg digunakan: ", hitungBahanCandi(candi,'pasir',N,celah))
    print("> Total Batu yangg digunakan: ", hitungBahanCandi(candi,'batu',N,celah))
    print("> Total Air yangg digunakan: ", hitungBahanCandi(candi,'air',N,celah))

    print("> ID Candi Termahal: ",end="")
    print(hargaCandi(candi,"Termahal",celah))
    print("> ID Candi Termurah: ",end="")
    print(hargaCandi(candi,"Termurah",celah))

    return