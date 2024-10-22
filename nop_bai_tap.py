#bai 1
import math
#nhập bán kính và chiều cao từ bàn phím 
r = float(input("nhap ban kinh (r): "))
h = float(input("nhap chieu cao (h): "))
#điều kiện 
if r > 0 and h > 0: 
 pi = 3.14
#tính diện tích xung quanh , diện tích toàn phần và thể tích
dien_tich_xung_quanh = 2 * pi * r * h 
dien_tich_toan_phan = 2 * pi *r * (r + h )
the_tich = 2 * pi * r * h 
#làm tròn kết quả đến hai chữ số thập phân 
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)
#kết quả
print(f"dien_tich_xung_quanh: {dien_tich_xung_quanh}")
print(f"dien_tich_toan_phan: {dien_tich_toan_phan}")
print(f"the_tich: {the_tich}")
#else:
print("r va h phai lon hon 0 ")
