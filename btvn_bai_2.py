#bai2
import math
#nhập tọa độ điểm M và tâm I, bán kính R từ bàn phím 
x = float(input("nhập tọa độ x của điểm M: "))
y = float(input("nhập tọa độ y của điểm M: "))
a = float(input("nhập tọa độ a của tâm I: " ))
b = float(input("nhập tọa độ b của tâm I: "))
R = float(input("nhập bán kính R của hình tròn: "))
#tính khoảng cách giữa M và I
distance = math.sqrt((x - a)**2 + (y - b)**2)
#kiểm tra nếu khoảng casch nhỏ hơn hoặc bằng bán kính R
if distance <=R:
    print("điểm M nằm trong hoặc trên hình tròn:{true}")
 
else:
    print("điểm M nằm ngoài hình tròn:{false}")
