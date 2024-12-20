def kiem_tra_so_thap_phan():
    #nhập chuỗi từ người dùng
    chuoi = input("nhập vào chuỗi ký tự: ").strip()
    #kiểm tra nếu chuỗi là số thập phân hợp lệ 
    if chuoi.count('.') == 1 and chuoi.replace('.' , '').replace('.' , '').isdigit() and chuoi[1:].replace('.' , '').isdigit():
        print("đay là một số thập phân ")
    else:
        print("đây không phải là số thập phân")
        
