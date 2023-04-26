import variables as var

def logout():
    if var.logged_in:
        var.current_user = ("", "", "")
        var.logged_in = False
    else:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        