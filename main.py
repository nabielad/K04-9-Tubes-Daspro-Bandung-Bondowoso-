#file main
# Kelompok 9 /K-04
from module import F01
from module import F02
#from module import F03
#from module import F04
from module import F05
#from module import F06
#from module import F07
from module import F08
from module import F09
from module import F10
#from module import F11
from module import F12
#from module import F15
from module import F16
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

username = None
login = False
save = False
while kondisi :
    masukan = input(">>> ")

    if masukan == 'login' :
        login = F01.login(user,login,username)

    elif masukan == 'logout' :
        login = F02.logout(user,login)
        
        
        
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

    elif masukan == 'ayamberkokok' :
        F12.ayamBerkokok(candi)
        break
        
        
        
    elif masukan == 'exit' :
        F16.exit(save)
        break
#print(F01.login())

f.close()
g.close()
h.close()

