import variables as var

def login():
    if var.logged_in:
        print("Login gagal!\nAnda telah login dengan username " + var.current_user[0] + ", silahkan lakukan “logout”")
    else:
        input_username = input("Username: ")
        input_password = input("Password: ")

        for idx in range(1,102):
            if idx == 101:
                print("\nUsername tidak terdaftar!")
            if var.users[idx] == None:
                continue
            if input_username == var.users[idx][0]:
                if input_password == var.users[idx][1]:
                    var.current_user = (var.users[idx][0],
                                        var.users[idx][1],
                                        var.users[idx][2])
                    var.logged_in = True
                    print("\nSelamat datang, " + var.current_user[0] + "!")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    break
                else:
                    print("\nPassword salah!")
                    break
