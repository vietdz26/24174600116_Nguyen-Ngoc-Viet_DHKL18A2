#bai9
import math
# chương trình tính cước taxi
def tinh_cuoc_taxi(loai_xe , quang_duong , thoi_gian):
    #khai báo biểu phí cho từng loại xe
    if loai_xe == 4 :
        gia_mo_cua = 11000
        km_mo_cua = 0.8
        gia_duoi_20km = 12100
        gia_tu_21km = 10000
        gioi_han_km = 20
    elif loai_xe == 7:
        gia_mo_cua = 13000
        km_mo_cua = 0.8
        gia_duoi_30km = 14100
        gia_tu_31km = 12000
        gioi_han_km = 30
    else:
        return "loại xe không hợp lệ . vui lòng thử lại "
    #tính cước mở cửa 
    if quang_duong <= km_mo_cua:
        cuoc = gia_mo_cua
    else:
        cuoc = gia_mo_cua
        #tính cước trong giới hạn km 
        if quang_duong <= gioi_han_km :
            cuoc += (quang_duong - km_mo_cua) * (gia_duoi_20km)
            cuoc += (quang_duong - km_mo_cua) * (gia_tu_21km)
    #tính tiền chờ
    if thoi_gian_cho > 5 :
        cuoc += (thoi_gian_cho - 5) * 800
    return(cuoc)
#nhập giữ liệu người dùng 
loai_xe = int(input("nhập loại xe (4 hoặc 7): "))
quang_duong = float(input("nhập quãng đường đi (km) "))
thoi_gian_cho = int(input("nhập thời gian chờ (phút) "))
#tính cước taxi 
cuoc = tinh_cuoc_taxi(loai_xe , quang_duong , thoi_gian_cho)
#in kết quả
print(f"cước taxi cần thanh toán : {cuoc}")
