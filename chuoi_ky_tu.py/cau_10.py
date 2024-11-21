def don_so_sang_ben_trai():
    #nhập chuỗi ký tự từ người dùng
    chuoi = input("nhập vào chuỗi ký tự: ").strip()
    #khởi tạo danh sách để lưu các chữ số và ký tự 
    so = ""
    ky_tu = ""
    #duyệt qua từng ký tự trong chuỗi 
    for ky_tu_hien_tai in chuoi:
        if ky_tu_hien_tai.isdigit(): #nếu ký tự là chữ số 
            so += ky_tu_hien_tai
        else: #nếu ký tự không phải là chữ số , thêm vào phần ký tự 
            ky_tu += ky_tu_hien_tai
    #kết hợp các chữ số và ký tự lại 
    ket_qua = so + ky_tu
    #in kết qủa 
    print("chuỗi mới sau khi dồn số sang bên trái: " , ket_qua)

