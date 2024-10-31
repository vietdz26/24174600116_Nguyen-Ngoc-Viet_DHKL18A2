#bai8 
import math
#chương trình phân loại sinh viên theo kết quả điểm học tập 
def phan_loai_sinh_vien(diem):
    if diem == "A":
        return "sinh viên xếp loại xếp sắc"
    elif diem == "B":
        return "sinh viên xếp loại giỏi"
    elif diem == "C":
        return "sinh viên xếp loại khác"
    elif diem == "D":
        return "sinh viên xếp loại trung bình"
    elif diem == "E":
        return "sinh viên xếp loại yếu"
    elif diem == "F":
        return "sinh viên xếp loại kém"
    else:
        return "điểm không hợp lệ. vui lòng thử lại"
#nhập điểm người dùng
diem = input("nhập điểm của sinh viên (A , B , C , E , F): ")
#phân loại sinh viên 
ket_qua = phan_loai_sinh_vien(diem)
#in kết quả
print(ket_qua)
