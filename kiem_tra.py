#bài 2 
import math 
#giải phương trình bậc 2 
a = float(input("nhập a"))
b = float(input("nhập b"))
c = float(input("nhập c"))
delta = float(b*b - 4*a*c)
if delta < 0: 
    print("phương trình vô nghiệm ")
if delta ==0:
    print("phương trình có nghiệm kép ")
    print("x = ", -b / 2 *a)
else:
    print("phương trình bậc 2 có 2 nghiệm phân biệt")
    print("x1 = ",(-b + math.sqrt (delta)/(2 * a)))
    print("x2 = ",(-b + math.sqrt (delta))/(2 * a))
