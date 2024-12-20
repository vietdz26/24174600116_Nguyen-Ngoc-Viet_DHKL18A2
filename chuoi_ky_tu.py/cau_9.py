def kiem_tra_nhi_phan():
    #nhập chuỗi nhị phân từ người đùng
    chuoi_nhi_phan = input("nhập vào chuỗi ký tự nhị phân; ").strip()
    #kiểm tra xem chuỗi chỉ chứ '0' và '1'
    if all (bit in '01' for bit in chuoi_nhi_phan):
        #chuyển chuỗi nhị phân sang chuỗi thập phân 
        so_thap_phan = int(chuoi_nhi_phan , 2)
        print(f"{chuoi_nhi_phan} là số nhị phân , chuyển sang thập phân: {so_thap_phan}")
    else:
        print("chuỗi nhập vào không phải là số nhị phân hợp lệ")
