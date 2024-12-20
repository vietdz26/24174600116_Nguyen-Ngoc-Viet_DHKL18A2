def loai_bo_khoang_trang_thua():
    #nhập chuỗi từ người dùng
    chuoi_nhap = input("nhập vào chuỗi ký tự: ").strip()
    #khởi tạo chuỗi kết quả
    ket_qua = ""
    n = len(chuoi_nhap)
    #duyệt qua từng ký tự bằng chỉ số 
    for i in range(n):
        #thêm ký tự nếu không phải là khoảng trắng hoặc nếu là khoảng trắng nhưng không đứng liền trước khoảng trắng khác
        if chuoi_nhap[i] != "" or (i > 0 and chuoi_nhap[i - 1] != ""):
            kết_qua += chuoi_nhap[i]
    #in chuỗi kết quả 
    print(f"chuỗi sau khi loại bỏ dáu cách thừa: {ket_qua}")
#gọi hàm 
loai_bo_khoang_trang_thua