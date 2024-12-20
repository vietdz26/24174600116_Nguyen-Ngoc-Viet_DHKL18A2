import math
#nhập bán kính và tâm đường tròn 
a = float(input("nhập tọa độ x tâm đường tròn (a): "))
b = float(input("nhập tọa độ y tâm đường tròn (b): "))
r = float(input("nhập vào bán kính của đường tròn (r): "))
#nhập tọa độ điểm m 
x_m = float(input("nhập tọa độ x của điểm m: "))
y_m = float(input("nhập tọa độ y của điểm m: "))
#tính khoảng cách từ m đến đường tròn 
d = math.sqrt((x_m -a ) ** 2 + (y_m -b) ** 2)
#kiểm tra vị trí của điểm m 
if d == r : 
    print("điểm m nằm trên đường tròn ")
elif d < r :
    print("điểm m nằm trong đường tròn ")
else:
    print("điểm m nằm ngoài đường tròn ")
    