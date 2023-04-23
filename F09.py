#F09 - Ambil Laporan 
# Nama/Nim : Andrew/ 16522040

def EOP(var):
    return var == None

def jumlahJin(peran, array,N):
    jlhPengumpul = 0
    jlhPembangun = 0
    for i in range(N):
        if(not(EOP(array[i]))):
            if(array[i+3][2] == 'Pengumpul'):
                jlhPengumpul += 1
            else:# role = 'pembangun'
                jlhPembangun += 1
        else:
            break
    if(peran == 'Pengumpul'):
        return jlhPengumpul
    else:#peran = pembangun
        return jlhPembangun
    
def hitungLenUser(array):
    kondisi = True
    banyak = 0 # jumlah totl jin
    i = banyak
    while (kondisi) :
        if EOP(array[i+3]) :
            kondisi = not(kondisi)
        elif(array[i+3][2] == 'Pengumpul' or array[i+3][2] == 'Pembangun'):
            banyak += 1
        i += 1
    return banyak

def printOutbahan(bahan_bangunan,bahan):
    n = 0
    if(not(EOP(bahan_bangunan[1]) and not(EOP(bahan_bangunan[2])) and not(EOP(bahan_bangunan[3])))):
        if(bahan == 'pasir'):
            n = int(bahan_bangunan[1][2])
        elif(bahan == 'batu'):
            n = int(bahan_bangunan[2][2])
        else:#bahan = air
            n = int(bahan_bangunan[3][2])
    return n

def cariIndeks(array, kata, indeksbeda):
    for k in range(0,len(array)):
        if(kata[indeksbeda] == array[k]):
            return k

    
def userTerpilih(indekskata1, indekskata2, kata1, kata2, type):
    if type == 'Terajin' :
        if(indekskata1 > indekskata2):
            return kata2
        else:
            return kata1
    elif type == 'Termalas' :
        if(indekskata1 > indekskata2):
            return kata1
        else:
            return kata2
    
def bandingKata(kata1, kata2, type):
    i = 0
    j = 0
    dataHurufKapital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dataHurufKecil = 'abcdefghijklmnopqrstuvwxyz'
    while(j < len(kata2)-1 and i < len(kata1)-1 and kata1[i] == kata2[j]):
        i += 1
        j += 1
    if i == 0 :
        indeksKata1 = cariIndeks(dataHurufKapital, kata1, i)
        indeksKata2 = cariIndeks(dataHurufKapital, kata2, j)
        return userTerpilih(indeksKata1,indeksKata2,kata1, kata2, type)

    elif(i == len(kata1)-1 or j == len(kata2)-1):
        if(type == 'Terajin'):
            if(len(kata1) > len(kata2)):
                return kata2
            else:
                return kata1
        else:# type = jin termalas
            if(len(kata1) > len(kata2)):
                return kata1
            else:
                return kata2          
    elif i > 0 or j > 0 :
        indeksKata1 = cariIndeks(dataHurufKecil, kata1,i)
        indeksKata2 = cariIndeks(dataHurufKecil, kata2,j)
        return userTerpilih(indeksKata1,indeksKata2,kata1, kata2, type)

def JinPopuler(Jenispopuler,arrayUser, arrayUserCandi):
    usernameJin = '-'
    jumlah = 0
    if(Jenispopuler == 'Termalas'):
        jumlah = 9999
    jumlahTemp = 0
    i = 3 # indeks mulai dari 3 dari data user
    j = 1 # indeks mulai dari 1 dari data candi
    if(Jenispopuler == 'Terajin'):
        while(not(EOP(arrayUser[i]))):
            username = arrayUser[i][0]
            while(not(EOP(arrayUserCandi[j]))):
                if(arrayUserCandi[j][1] == username):
                    jumlahTemp += 1
                j += 1
            if(usernameJin == '-' and jumlahTemp >= 1 and username != '-1'):
                usernameJin = username
            elif(jumlahTemp > jumlah and username != '-1'):
                jumlah = jumlahTemp
                usernameJin = username
            elif(jumlahTemp == jumlah and jumlah != 0 and username != '-1'):
                usernameJin = bandingKata(usernameJin,username,'Terajin')
            jumlahTemp = 0
            j = 0
            i += 1
    elif(Jenispopuler == 'Termalas'):
        while(not(EOP(arrayUser[i]))):
            username = arrayUser[i][0]
            while(not(EOP(arrayUserCandi[j]))):
                if(arrayUserCandi[j][1] == username):
                    jumlahTemp += 1
                j += 1
            if(usernameJin == '-' and jumlahTemp >= 1 and username != '-1'):
                usernameJin = username
            elif(jumlahTemp < jumlah and username != '-1'):
                jumlah = jumlahTemp
                usernameJin = username
            elif(jumlahTemp == jumlah and jumlah != 0 and username != '-1'):
                usernameJin = bandingKata(usernameJin,username,'Termalas')
            jumlahTemp = 0    
            j = 0
            i += 1  
    
    return usernameJin
        
    
def laporanjin(user, candi, bahan_bangunan): # arrray1 = user ,array2 = bahan, array 3= candi
    # laporan bagian data user

    N = hitungLenUser(user)
    print("> Total Jin: ",N)
    N = 103
    nPengumpul = jumlahJin('Pengumpul',user,N)
    nPembangun = jumlahJin('Pembangun',user,N)
    print("> Total JIn Pengumpul: ",nPengumpul)
    print("> Total JIn Pembangun: ",nPembangun)

    # laporan bagian data candi 
    print("> Jin Terajin: ", JinPopuler("Terajin",user,candi))
    print("> Jin Termalas: ", JinPopuler("Termalas",user,candi))

    #laporan bagina data bahan_bangunan
    print("> Jumlah Pasir: ", printOutbahan(bahan_bangunan,"pasir"))
    print("> Jumlah Batu: ", printOutbahan(bahan_bangunan,"batu"))
    print("> Jumlah Air: ", printOutbahan(bahan_bangunan,"air"))
    return
