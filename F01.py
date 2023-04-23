#NIM/Nama : 16522076/Kayla Nasywa V
#F01 - Login

def login(user,login,username):
    while login and not(username):
        print("Login gagal!")
        print("Anda telah login dengan username " + username + ", silakan lakukan logout sebelum melakukan login kembali.")

    username = input("Username: ")
    password = input("Password: ")

    i = 0
    while user[i] != None and i < 102:
        if user[i][0] == username and user[i][1] == password:
            print("Selamat datang, " + username + "!")
            print("Masukkan command " + "help" +" untuk daftar command yang dapat kamu panggil.")
            return True
        elif user[i][0] == username and user[i][1] != password:
            print("Password salah!")
            return False
        elif user[i][0] != username and user[i][1] == password:
            print("Username tidak terdaftar!")
            return False
        i = i+1



