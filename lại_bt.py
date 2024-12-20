#bài 1
n = int(input("nhập vào số nguyên dương n : "))
for i in range(n):
    if i % 2 != 0:
        print(i)





#bài 3
#khởi tạo hai số đầu tiên trong dãy fibonacci
a = 0
 
# in ra 50 số đầu tiên trong dãy fibonacci 
for _ in range(50):
    print(a)
    tong_ab = a + b 
    a = b 
    b = tong_ab

     




    


#bài 4
#nhập vào một số từ người dùng 
number = int(input("nhâjp một số: "))
#hàm kiểm tra số nguyên tố
def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(int(n ** 0.5) + 1):
        if n % i == 0 :
            return False
    return True
#kiểm tra và in kết quả
if so_nguyen_to(number):
    print(f"{number} là số nguyên tố")
else:
    print(f"{number} không phải  là số nguyên tố")










#BÀI 6 
# nhập vào một số từ người dùng 
number = int(input("nhập một số: "))
#hàm kiểm tra số chính phương 
def so_chinh(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n 
#kiểm tra và in kết quả
if so_chinh(number):
    print(f"(number là số chính phương)")
else:
    print(f"{number} không phải là số chính phương")










#bài 7
#nhập vào số n tưf người dùng 
n = int(input("nhập số n: "))
#hàm kiểm ta số nguyên tố
def so_nguyen_to(number):
    if number <= 1:
        return False
    for i in range(int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
#tìm tất cả các số nguyên tố nhỏ hơn n 
for i in range(n):
    if so_nguyen_to(i):
        so_nguyen_to(i)
#in ra các số nguyên tố
print(f"các số nguyên tố nhỏ hơn n là số nguyên tố")











#bài 9
#nhập vào số n từ người đùng
n = int(input("nhập số n: "))
#hàm kiểm tra số chính phương 
def so_chinh_phuong(number):
    if number < 0:
        return False
    root = int(number ** 0.5)
    return root * root == number
#tìm tất cả các số chính phương hơn hơn n 
for i in range (n):
    if so_chinh_phuong(i):
        so_chinh_phuong(i)
#in ra các số chính phương 
print (f"các số chính phương nhỏ hơn n là ")









#bài 10
#nhập vào hai số từ người dùng 
a = int(input("nhập số thứ nhất: "))
b = int(input("nhập số thứ hai: "))
#hàm tìm ước chung lớn nhất 
def uoc_chung_lon_nhat(x , y):
    while y != 0:
        x , y = y , x % y 
    return x 
#tính ước chung lớn nhất của hai 
ucln = uoc_chung_lon_nhat(a , b)
#in ra kết quả
print(f"ước chung lớn nhất của {a} , {b} là : {ucln}")











#bài 11
#nhập vào hai số từ người dùng 
a = int(input("nhập số thứ nhất: "))
b = int(input("nhập số thứ hai: "))
#hàm tìm ước chung lớn nhất
def uoc_chung_lon_nhat(x , y):
    while y != 0:
        x, y = y , x % y 
    return x
#hàm tính bội chung nhỏ nhất 
def boi_chung_nho_nhat(x , y):
    return (x * y) // uoc_chung_lon_nhat(x, y)
#tính bội chung nhỏ nhất của hai số 
bcnn = boi_chung_nho_nhat(a, b)
#in ra kết quả
print(f"bội chung nhỏ nhất của {a} , {b} là {bcnn}")















#bài 5 
#tìm hàm số hoàn hảo 
def so_hoan_hao(n):
    #kiểm tra nếu n <= 1 thì không phải là số hoàn hảo 
    if n <= 1:
        return False
    #tìm tất cả ước số của n và tính tổng các ước số
    tong_cac_uoc_so_thuc_cua_n = 0 
    for i in range(1, n):
        if n % i == 0:
            tong_cac_uoc_so_thuc_cua_n += i
    #kiểm tra nếu tổng các uoức bằng n 
    return tong_cac_uoc_so_thuc_cua_n == n 
#nhập số từ người dùng
number = int(input("nhập một số: "))
#kiểm tra và in kết quả
if so_hoan_hao(number):
    print(f"{number} là số hoàn hảo")
else:
    print(f"{number} là số không hoàn hảo ")
    
  




    





#bài 2 
#nhập giá trị n 
n = int(input("nhập giá trị n: "))
#tính S1 
S1 = 0
for i in range(1, n+1):
    S1 += i
#tính S2
S2 = 1 
for i in range (1 , n):
    S2 *= i 
#tính S3
S3 = 0 
for k in range(1 , n+1):
    S3 += ((-1) ** (k-1)) / k 
#tính S4
S4 = 0 
for k in range (n +1):
    S4 += k / (k + 2)
#in kết quả
print("S1= ", S1)
print("S2= ", S2)
print("S3 =", S3)
print("S4= ", S4)













#bài 8 
#nhập vào số n 
n = int(input("nhập vào n: "))
#duyệt qua tất cả các số từ 2 đến n -1 để kiểm tra số hoàn hảo 
print(f"các số hoàn hảo nhỏ hơn {n}: ")
for i in range(2 , n):
    tong_cong = 1 #bắt đầu tổng từ 1 vì 1 là ước của tất cả các số 
#tính tổng các ước của i 
for j in range(2, int(i **0.5)+1 ):
    if i % j == 0:
        tong_cong +=j 
        if j != i // j: #kiểm tra nếu tổng các ước bằng chính số đó
            tong_cong += i // j 
        #kiểm tra nếu tổng các ước bằng chính số đó
        if tong_cong == i:
            print(i)














#bài 12
#nhập vào tử số và mẫu số 
tu_so = int(input("nhập vào tu so: "))
mau_so = int(input("nhập vào mẫu số: "))
#kiểm tra mẫu số có phải là 0 hay không 
if mau_so == 0:
    print("mẫu số không thể bằng 0! ")
else:
    #tính ước chung lớn nhất bằng thuật toán euclid
    a ,b = tu_so , mau_so
    while b != 0:
        a ,b = b , a % b
    #tối giản phân số 
    tu_so //= a 
    mau_so //= a 
    #in kết quả phân số đã tối giản 
    print(f"phân số đã tối giản là: {tu_so} / {mau_so} ")


















#bài 15
#chuyển từ cơ số 10 sang cơ số 2
n = int(input("nhập hệ số thâjp phân: "))
if n == 0:
    print("số nhị phân là: 0 ")
else:
    #in trực tiếp các bit nhị phân từ phải sang trái 
    while n > 0:
        print(n % 2 , end="")
        n //= 2 
    print() #xuống dòng sau khi in xong 
#chuyển từ cơ số 2 sang cơ số 10 
b = int("nhập số nhị phân; ")
thap_phan = 0 
for i in range(b):
    thap_phan = thap_phan * 2 + int(b[i])
    print(f"số thập phân là {thap_phan}")













#bài 14
#nhập số dòng 
n = int(input("nhập số dòng: "))
#hàm 
for line in range(n):
    #in khoảng cách để căn giữa
    print("(n - line - 1) , end= ")
    c = 1
    for i in range(line + 1):
        print(c , end="")
        c = int(c * (line - i) / (i + 1))
        print()
        


















#bài 13
#nhập vào một số 
n = int(input("nhập một số: "))
#in"1"đầu tiên 
print("1" , end="")
#kiểm tra các thừa số từ 2 đến n 
for i in range(2 ,n + 1 ):
    while n % i == 0:
        print(f" * {i}" , end="")
        n //=i
#kết thúc 
print()















