my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len (my_list)-1
i = -1
while True:
    i = i + 1
    if i > a:
        break
    else:
        if my_list[i] > 0:
            print (my_list[i])
        elif my_list[i] == 0:
            continue
        else:
            break
