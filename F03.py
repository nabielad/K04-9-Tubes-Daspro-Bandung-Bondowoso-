import variables as var

def summonjin():
    if jin_penuh(var.users):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")

        while True:
            pilih_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            if pilih_jin == '1':
                role = "jin_pengumpul"
                break
            elif pilih_jin == '2':
                role = "jin_pembangun"
                break
            else:
                print("Tidak ada jenis jin bernomor " + pilih_jin + "!")

        while True:
            username_taken = False
            username = input("Masukkan username jin:")
            for idx in range(1, 101):
                if var.users[idx] == None:
                    continue
                if username == var.users[idx][0]:
                    username_taken = True
            if username_taken:
                print("Username " + username + " sudah diambil!")
            else:
                break        

        while True:
            password = input("Masukkan password jin:")
            if len(password) < 5 or len(password) > 25:
                print("Password panjangnya harus 5-25 karakter!")
            else:
                var.users = isi_jin(var.users, username, password, role)
                print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
                print("Jin " + username + " berhasil dipanggil!")
                break

def jin_penuh(user_arr):
    penuh = True 
    for idx in range(1, 101):
        if user_arr[idx] == None:
            penuh = False
    return penuh

def isi_jin(user_arr, username, password, role):
    idx = 1
    while user_arr[idx] != None:
        idx += 1
    user_arr[idx] = [username, password, role]
    return user_arr
