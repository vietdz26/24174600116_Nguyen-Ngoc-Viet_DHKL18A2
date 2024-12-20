import math 
#nhập vào hai số m và n 
m = float(input("nhập vào số m: "))
n = float(input("nhập vào số n: "))
#tính tổng 
total = m + n 
#kiểm tra điều kiện 
if total > 100:
    print(f"tổng của {m} và {n} là total , lớn hơn 100 chương trình dừng")
else:
    print(f"tổng của {m} và {n} là total , nhỏ hơn 100 chương trình tính tiếp ")
    