def dem_ky_tu():
    #nhập chuỗi từ người dùng 
    chuoi_nhap = input("nhập vào chuỗi ký tự: ")
    #khởi tạo biến đếm 
    so_chu = 0 #đếm số ký tự là chữ
    so_so = 0 #đến số ký tự là số 
    so_ky_tu_dac_biet = 0 #đếm ký tự đặc biệt 
    #duyệt từng ký tự trong chuỗi 
    for ky_tu in chuoi_nhap:
        if ky_tu.isalpha(): #kiểm tra nếu là chữ cái 
            so_chu += 1
        elif ky_tu.isdigit(): #kiểm tra nếu là số 
            so_so += 1 
        else: #nếu không phải chữ cũng không phải số, là ký tự đặc biệt
            so_ky_tu_dac_biet += 1
    #in kết quả 
    print(f"số ký tự là chữ: {so_chu}")
    print(f"số ký tự là số: {so_so}")
    print(f"số ký tự đặc biệt: {so_ky_tu_dac_biet}")
