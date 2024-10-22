import math
# nhập bán kính và chiều cao nhập từ bàn phím
r = float(input("nhập bán kính (r):"))
h = float(input("nhập chiều cao (h):"))
# điều kiện
if r > 0 and h > 0:
 pi = 3.14
# tính diện tích xung quanh , diện tích tòan phần và thể tích 
dien_tich_xung_quanh = 2* pi * r *h
dien_tích_toan_phan = 2* pi * r * (r+h)
the_tich = pi * r * 2 * h
# làm tròn kết quả đến hai chữ số thập phân 
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tích_toan_phan =round(dien_tích_toan_phan, 2)
the_tich = round(the_tich, 2)
# in kết quả 
print(f"diện tích xung quanh: {dien_tich_xung_quanh}")
print(f"diện tích toàn phần: {dien_tích_toan_phan}")
print(f"thể tích: {the_tich}") 
#else : 
print("r va h phai lon hon 0 ")



#bài 8 
import math 
x = input("nhập giá trị x: ")
x = float(x)
f_x = math.log(x , 4) + math.log(2 , x)
print (f"giá trị cần tìm f(x) = {f_x:.2f}")




#bài 2 
#tu so = -x + (x**2 + 4)**(1/2)
#mau so = (x**4 + 1)**(1/7)
#f_x = (-x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7))
print(f"giá trị của f(x) = {f_x:.2f}")




#bài 4 
t = float(input("nhap thoi gian su dung bong den"))
hieu_dien_the = 220
cuong_do_dong_dien = 2.7 
P = t *hieu_dien_the * cuong_do_dong_dien/3600 * 1000
tien_phai_tra = cong_suat*7000 
print(f"tien dien phai tra: {tien_phai_tra}")


