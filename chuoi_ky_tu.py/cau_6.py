def kiem_tr_so_am():
    #nhập chuỗi từ người dùng 
    chuoi = input("nhập vào chuỗi ký tự: ").strip()
    #kiểm tra nếu chuỗi bắt đầu bằng dấu '-' và phần còn lại là số 
    if chuoi.startswith('-') and chuoi[1:].isdigit():
        print("đây là một số âm ")
    else:
        print("đây không phải là số âm ")
        