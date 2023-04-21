#F08 - Batch Kumpul/Bangun
#Nama/NIM : Andrew/16522040
import random

def EOP(var):
    return var == None

def jumlahJin(peran,user):
    jlhPengumpul = 0
    jlhPembangun = 0
    i = 0
    while(not(EOP(user[i+3]))):
        if(user[i+3][0] != '-1'):
            if(user[i+3][2] == 'Pengumpul'):
                jlhPengumpul += 1
            else:# role = 'pembangun'
                jlhPembangun += 1
        i += 1

    if(peran == 'Pengumpul'):
        return jlhPengumpul
    else:#peran = pembangun
        return jlhPembangun

def inputBahan(pasir,batu,air,tipe,bahan_bangunan):
    integerBahan(bahan_bangunan)
    if(tipe == 'Pengumpul'):
        bahan_bangunan[1][2] += pasir
        bahan_bangunan[2][2] += batu
        bahan_bangunan[3][2] += air
    else:#tipe Pembangun
        bahan_bangunan[1][2] -= pasir
        bahan_bangunan[2][2] -= batu
        bahan_bangunan[3][2] -= air
    return

def berhasilBangun(pasir,batu,air,jlhPembangun,bahan_bangunan,candi,user, candiTemp):
    integerBahan(bahan_bangunan)
    if(pasir <= bahan_bangunan[1][2] and batu <= bahan_bangunan[2][2] and air <= bahan_bangunan[3][2]):
        print("Jin berhasil membangun total "+str(jlhPembangun)+" candi.")
        inputBahan(pasir, batu, air,'Pembangun',bahan_bangunan)
        inputCandi(103,user,candi,candiTemp)
        print(candiTemp)
        resetCandiTemp(candiTemp,user)

    else:#bahan kurang
        print("Bangun gagal. Kurang",end=" ")
        if(pasir > bahan_bangunan[1][2]):
            print(str(pasir - bahan_bangunan[1][2])+" pasir",end=" ")
        if(batu > bahan_bangunan[2][2]):
            print(str(batu - bahan_bangunan[2][2])+" batu",end=" ")
        if(air > bahan_bangunan[3][2]):
            print(str(air - bahan_bangunan[3][2])+" air",end=" ")       
        print(".")
        resetCandiTemp(candiTemp,user)
    return

def randomBahan(bahan):
    pasir = 0
    batu = 0
    air = 0
    if(bahan == 'pasir'):
        pasir = random.randint(0,5)
        return pasir
    elif(bahan == "batu"):
        batu = random.randint(0,5)
        return batu
    elif(bahan == 'air'):
        air = random.randint(0,5)
        return air

def batchKumpul(user, bahan_bangunan):
    jlhPengumpul = jumlahJin('Pengumpul',user)
    pasir = 0
    batu = 0
    air = 0
    
    if(jlhPengumpul == 0):
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:#ada jin pengumpul
        for i in range(jlhPengumpul):
            pasirTemp = randomBahan("pasir",)
            pasir += pasirTemp
            batuTemp = randomBahan('batu')
            batu += batuTemp
            airTemp = randomBahan('air')
            air += airTemp

        print("Mengerahkan "+str(jlhPengumpul)+" jin untuk mengumpulkan bahan.")
        print("Jin menemukan total "+str(pasir)+" pasir, "+str(batu)+" batu, "+str(air)+" air.")
        inputBahan(pasir,batu,air,'Pengumpul',bahan_bangunan)
    return

def batchBangun(user, bahan_bangunan,candi):
    jlhPembangun = jumlahJin('Pembangun',user)
    candiTemp = [[0 for i in range(3)] for j in range(jumlahJin('Pembangun',user)+1)]
    pasir = 0
    batu = 0
    air = 0
    if(jlhPembangun == 0):
        print("Kumpul gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:#ada jin pembangun
        for i in range(jlhPembangun):
            pasirTemp = randomBahan("pasir")
            pasir += pasirTemp
            batuTemp = randomBahan('batu')
            batu += batuTemp
            airTemp = randomBahan('air')
            air += airTemp
            bangunCandiTemp(pasirTemp, batuTemp, airTemp,candiTemp)
        print("Mengerahkan "+str(jlhPembangun)+" jin untuk membangun candi")
        print("dengan total bahan "+str(pasir)+" pasir, "+str(batu)+" batu, "+str(air)+" air.")
        berhasilBangun(pasir,batu,air,jlhPembangun,bahan_bangunan,candi,user,candiTemp)

def hitungLenUser(array):
    kondisi = True
    banyak = 0 # jumlah totl jin
    i = banyak
    while (kondisi) :
        if EOP(array[i+3]) :
            kondisi = not(kondisi)
        elif(array[i+3][2] == 'Pengumpul' or array[i+3][2] == 'Pembangun') and (array[i+3][0] != '-1'):
            banyak += 1
        i += 1
    return banyak


def bangunCandiTemp(pasir, batu, air,candiTemp): # bangun candi saat belum ditentukan apakah bahan cukup
    i = 0
    while(candiTemp[i][0] != 0 and candiTemp[i][1] != 0 and candiTemp[i][2] != 0):
        i += 1
    #Setelah ada baris matriks kosong
    
    candiTemp[i][0] = pasir
    candiTemp[i][1] = batu
    candiTemp[i][2] = air
    return

def inputCandi(jumlahTotalUser, user, candi,candiTemp):
    k = 0
    for i in range(2,jumlahTotalUser):
        if(EOP(user[i])):
            break
        elif(user[i][2] == 'Pembangun'):
            j = 1
            id = 1
            arrayTemp = [0 for i in range(5)]
            while((not(EOP(candi[j]))) and candi[j][1] != '-1' and j < 103):
                id += 1
                j += 1
            
            if j < 103 :
                if(EOP(candi[j])):
                    arrayTemp[0] = id
                    arrayTemp[1] = user[i][0]
                    arrayTemp[2] = candiTemp[k][0]
                    arrayTemp[3] = candiTemp[k][1]
                    arrayTemp[4] = candiTemp[k][2]
                    candi[j] = arrayTemp
                elif(candi[j][1] == '-1'):
                    candi[j][1] = user[i][0]
                    candi[j][2] = candiTemp[k][0]
                    candi[j][3] = candiTemp[k][1]
                    candi[j][4] = candiTemp[k][2]                    

            k += 1
        
    return 

def integerBahan(bahan_bangunan):
    bahan_bangunan[1][2] = int(bahan_bangunan[1][2])
    bahan_bangunan[2][2] = int(bahan_bangunan[2][2])
    bahan_bangunan[3][2] = int(bahan_bangunan[3][2])
    return

def resetCandiTemp(candiTemp,user):
    for i in range(0, jumlahJin("Pembangun",user)+1):
        for j in range(0,3):
            candiTemp[i][j] = 0
    return

