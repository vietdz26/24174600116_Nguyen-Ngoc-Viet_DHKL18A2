def tach_ho_ten():
    #nhập họ tên từ người đùng
    ho_ten_day_du = input("nhập vào họ tên đầy đủ: ").strip()
    #tách họ tên thành danh sách các từ
    danh_sach_ten = ho_ten_day_du.strip()
    #lấy họ và tên 
    ho = danh_sach_ten[0] #họ là từ đầu tiên 
    ten = danh_sach_ten[-1] #tên là từ cuối cùng
    #in kết quả
    print(f"Họ: {ho} , Tên: {ten}")
#gọi hàm 
tach_ho_ten