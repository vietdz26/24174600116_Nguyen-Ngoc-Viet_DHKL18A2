#bài 2 
#nhập x 
x = float(input("nhập giá trị của x: "))
#kiểm tra điều kiện của x 
#if x > 0: 
#phép tính 
tu_so = -x + (x**2 + 4)**(1/2)
mau_so = (x**4 + 1)**(1/7)
f_x = tu_so / mau_so
#tính 
ket_qua = round(f_x, 2)
#in kết quả 
print(f"giá trị của f(x) = {f_x:.2f}")
#else:
print("giá trị x phải lớn hơn 0 để thực hiện phép tính:")
