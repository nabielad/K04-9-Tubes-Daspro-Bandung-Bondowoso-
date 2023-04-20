# NIM/Nama   : 16522022/Nabiel Aufi Danendra
# F15 - Help

def help(role):
    print("===================== HELP =====================")
    
    if role == "bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. save")
        print("   Untuk menyimpan data")
        print("3. summonjin")
        print("   Untuk memanggil jin")
        print("4. hapusjin")
        print("   Untuk menghapus jin")
        print("5. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("6. batchkumpul")
        print("   Untuk membuat jin pengumpul mengumpulkan bahan")
        print("7. batchbangun")
        print("   Untuk membuat jin pembangun membangun candi")
        print("8. laporanjin")
        print("   Untuk mengetahui kinerja dari para jin")
        print("9. laporancandi")
        print("   Untuk mengetahui progress pembangunan candi")
        print("10. exit")
        print("   Untuk keluar dari permainan")
    
    elif role == "roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. save")
        print("   Untuk menyimpan data")
        print("3. hancurkancandi")
        print("   Untuk menghancurkan candi")
        print("4. ayamberkokok")
        print("   Untuk menyelesaikan permainan dan menentukan pemenang")
        print("5. exit")
        print("   Untuk keluar dari permainan")

    elif role == "jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. exit")
        print("   Untuk keluar dari permainan")
    
    elif role == "jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan bahan-bahan bangunan")
        print("3. exit")
        print("   Untuk keluar dari permainan")
    
    else:   # role == ""
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
