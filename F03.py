# NIM/Nama   : 16522022/Nabiel Aufi Danendra
# F03 - Summon Jin

from functions import *
def summonjin(dataUser):

    # KAMUS LOKAL
    # nomor : integer
    # tipe_jin, username_jin, password_jin : string

    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    print()

    # validasi nomor jenis jin
    while True:
        nomor = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if nomor == 1:
            tipe_jin = "jin_pengumpul"
            print()
            print("Memilih jin Pengumpul.")
            break
        elif nomor == 2:
            tipe_jin = "jin_pembangun"
            print()
            print("Memilih jin Pembangun.")
            break
        else:
            print()
            print(f"Tidak ada jenis jin yang bernomor {nomor}!")
            print()
    print()

    # validasi username jin
    while True:
        username_jin = input("Masukkan username jin: ")
        for i in range(length(dataUser)):
            if dataUser[i][0] == username_jin:
                print(f"Username {username_jin} sudah diambil!")
            else:
                break
        break
    
    # validasi password jin
    while True:
        password_jin = input("Masukkan password jin: ")
        if len(password_jin) < 5 or len(password_jin) > 25:
            print("Password panjangnya harus 5-25 karakter!")
        else:
            break

    # menambahkan jin baru ke array
    jin_baru = [username_jin, password_jin, tipe_jin]

    dataUser = newappend(dataUser, jin_baru)

    print("Mengumpulkan sesajen. . .")
    print("Menyerahkan sesajen. . .")
    print("Membacakan mantra. . .")

    print(f"Jin {username_jin} berhasil dipanggil!")