#bai7
import math
#chương trình giải hệ phương trình bậc nhất hai ẩn 
def giai_he_phuong_trinh():
    #nhập các hệ số từ bàn phím
    a1 = float(input("nhập a1: "))
    b1 = float(input("nhập b1: "))
    c1 = float(input("nhập c1: "))
    a2 = float(input("nhập a2: "))
    b2 = float(input("nhập b2: "))
    c2 = float(input("nhập c2: "))
    #tính định thức
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - c2 * c1
    #xét trường hợp 
    if D ==0 :
        if Dx ==0 and Dy ==0 :
            print("hệ phương trình có vô số nghiệm")
        else:
            print("hệ phương trình vô nghiệm")
    else:
        x = Dx / D
        y = Dy / D
        print("nghiệm của hệ phương trình là: ")
        print("x =", x)
        print("y =", y)
#gọi hàm để chạy chương trình
giai_he_phuong_trinh()