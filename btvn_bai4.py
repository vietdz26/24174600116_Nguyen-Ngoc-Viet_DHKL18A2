#bai4
def kiem_tra_tam_giac(a , b , c):
    #kiểm tra điều kiện tam giác
    if a + b > c and a + c > b and b + c > a:
        #kiểm tra loại tam giác
        if a == b == c:
            return "tam giác đều"
        elif a==b or a==c or b==c:
            if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
                return "tam giác vuông cân"
            return "tam giác cân"
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "tam giác vuông"
        else:
            return "tam giác thường" 
    else:
        return "không phải là bộ ba cạnh của tam giác" 
#nhập vào các cạnh a, b, c từ bàn phím
a = float(input("nhập cạnh a: "))
b = float(input("nhập cạnh b: "))
c = float(input("nhập cạnh c "))
#gọi hàm và in kết quả
result = kiem_tra_tam_giac(a, b, c)
print(result)