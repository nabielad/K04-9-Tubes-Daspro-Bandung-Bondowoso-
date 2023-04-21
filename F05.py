#F05 - Ubah Tipe Jin
#Nama/NIM : Andrew/16522040

def EOP(var):
    return var == None

def bisa(pilihan, roleIndeks, roleGanti,user):
    if(pilihan == 'Y' or pilihan == 'y'):
        user[roleIndeks][2] = roleGanti
        print("JIn telah berhasil diubah")
    elif(pilihan == 'N' or pilihan == 'n'):
        print("Jin tetap")
    return

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

def ubahJin(user):
    namaJin = input("Masukkan username jin : " )
    a = -1
    N = hitungLenUser(user)
    for i in range(N):
        if(namaJin ==user[i][0]):
            a = i
    if(a == -1):
        print("Tidak ada jin dengan username tersebut.")
    else:#a != -1
        if(user[a][2] == 'Pengumpul'):
            roleGanti = 'Pembangun'
            pilihan = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun”(Y/N)? ")
            bisa(pilihan, a, roleGanti,user)
        else: #role[a] = Pembangun
            roleGanti = 'Pengumpul'            
            pilihan = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul”(Y/N)? ")
            bisa(pilihan, a, roleGanti,user)
    return
