#bài 8 
import math
#nhập giá trị x 
x = float(input("nhập giá trị x: "))
#kiểm tra điều kiện của x 
#if x > 0:
#phép tính 
log_4_x = math.log(x, 4)
log_2_x = math.log(2, x)
#tính toán 
dap_an = log_4_x + log_2_x
dap_an = round(dap_an, 2)
#kết quả
print("giá trị của biểu thức là:", dap_an)
#else
print("giá trị x phải lớn hơn 0")
