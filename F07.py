import variables as var
from random import randint

def kumpul():
    pasir = randint(1, 5)
    batu = randint(1, 5)
    air = randint(1, 5)

    var.bahan[1][2] = str(int(var.bahan[1][2]) + pasir)
    var.bahan[2][2] = str(int(var.bahan[2][2]) + batu)
    var.bahan[3][2] = str(int(var.bahan[3][2]) + air)

    print("Jin menemukan " + str(pasir) + " pasir, " + str(batu) + " batu, dan " + str(air) + " air.")