def kiem_tra_xau():
    #nhập vào hai chuỗi str_1 và str_2
    str_1 = input("nhập vào chuỗi str_1: ")
    str_2 = input("nhập vào chuỗi str_2: ")
    #kiểm tra xem str_2 có nằm trong str_1
    if str_2 in str_1:
        print(f"chuỗi '{str_2}' có nằm trong '{str_1}' . ")
    else:
        print(f"chuỗi '{str_2}' không nằm trong '{str_1}' . ")
    #kiểm tra xem str_1 có nằm trong str_2
    if str_1 in str_2: 
        print(f"chuỗi '{str_1}' nằm trong '{str_2}' . ")
    else:
        print(f"chuỗi '{str_1}' không nằm trong '{str_2}' . ")
        