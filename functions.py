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

def newappend(list, item):
    i = 0
    while True:
        if list[i] != None:
            i += 1
        else: #  list[i] == None
            list[i] = item
            break

    return list