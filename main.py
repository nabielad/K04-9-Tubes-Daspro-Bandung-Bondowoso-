#file main
# Kelompok 9 /K-04
from module import F01
#from module import F03
#from module import F04
from module import F05
#from module import F06
#from module import F07
from module import F08
from module import F09
from module import F10
#from module import F11
#from module import F12
#from module import F15
from module import load
from module import argparse


f = open("file_csv/user.csv")
g = open("file_csv/candi.csv")
h = open("file_csv/bahan_bangunan.csv")
#print(F01.login('file_csv/user.csv'))
kondisi = argparse.argument_Parse()
'''
user = []
candi = []
bahan_bangunan = []
'''
user = load.open_csv(f)
candi = load.open_csv(g)
bahan_bangunan = load.open_csv(h)

while kondisi :
    masukan = input(">>> ")

    if(masukan == 'login'):
        print("login")


    elif masukan == 'ubahjin' :
        F05.ubahJin(user)

    elif masukan == 'batchkumpul' :
        F08.batchKumpul(user, bahan_bangunan)

    elif masukan == 'batchbangun' :
        F08.batchBangun(user, bahan_bangunan, candi)

    elif masukan == 'laporanjin' :
        F09.laporanjin(user,candi,bahan_bangunan)

    elif masukan == 'laporancandi' :
        F10.laporancandi(candi)

    elif(masukan == 'exit'):
        break
#print(F01.login())

f.close()
g.close()
h.close()

