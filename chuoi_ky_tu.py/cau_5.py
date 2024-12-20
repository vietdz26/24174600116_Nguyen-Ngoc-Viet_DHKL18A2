def dem_hoa_va_chu_thuong():
    #nhập chuỗi từ người dùng 
    chuoi_nhap = input("nhập vào chuỗi ký tự: ")
    #khởi tạo biến đếm 
    so_chu_hoa = 0 #đếm số chữ cái viết hoa 
    so_chu_thuong = 0 #đếm số chữ cái viết thường 
    #duyệt qua từng ký tự trong chuỗi 
    for ky_tu in chuoi_nhap:
        if ky_tu.isupper(): # kiểm tra nếu là chữ cái viết hoa 
            so_chu_hoa += 1
        elif ky_tu.islower(): #kiểm tra nếu là chữ cái viết thường
            so_chu_thuong +=1 
    #in kết quả 
    print(f"số chữ cái viết hoa: {so_chu_hoa}")
    print(f"số chữ cái viết thường: {so_chu_thuong}")
    