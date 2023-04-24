# FUNGSI PENGGANTI LEN
def length(list):
    count = 0
    i = 0
    while True:
        if list[i] != None:
            count += 1
        else:   # list[i] == None
            break
        i += 1

    return count

# FUNGSI PENGGANTI APPEND
def newappend(list, item):
    i = 0
    while True:
        if list[i] != None:
            i += 1
        else: #  list[i] == None
            list[i] = item
            break

    return list

# FUNGSI PENGGANTI POP
def newpop(list, item):
    newlist = ["" for i in range(length(list)-1)]
    index = 0   # inisialisasi increment untuk newlist
    for i in range(length(list)):
        if list[i] != item:
            newlist[index] = list[i]
            index += 1
        # else (list[i] == item) maka tidak akan masuk ke dalam list baru

    return newlist
