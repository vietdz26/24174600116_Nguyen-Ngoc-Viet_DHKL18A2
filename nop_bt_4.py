#bai 4
#nhập thời gian 
t = float(input("nhap thoi gian: "))
#điều kiện thời gian 
#if t > 0 :
#chi tiết bóng đèn 
hieu_dien_the = 220
cuong_do_dong_dien = 2,7
cong_suat = 7000
#phép tính
cong_suat = t *hieu_dien_the*cuong_do_dong_dien/3600*1000
#tính 
tien_phai_trai = cong_suat*7000
#in kết quả
print("tien phai tra la: ", tien_phai_trai)
#else:
print("thoi gian su dung phai lon hon 0")
