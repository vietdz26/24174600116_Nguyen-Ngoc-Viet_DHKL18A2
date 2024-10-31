#hàm để tính loại điểm
def xep_loai (diem_trung_binh):
    if diem_trung_binh >=9:
        return "A"
    elif diem_trung_binh >=7:
        return "B"
    elif diem_trung_binh >=5:
        return "C"
    else:
        return "D"
#nhập điểm từng người dùng
diem_chuyen_can = float(input("nhập điểm chuyên cần:"))
diem_giua_ki = float(input("nhập điểm giữa kì:"))
diem_cuoi_ki = float(input("nhập điểm cuối kì:"))
#tính điểm trung bình
diem_trung_binh = (diem_chuyen_can + diem_giua_ki + diem_cuoi_ki)/3
#xếp loại
loai_diem = xep_loai(diem_trung_binh)
#in kết quả
print(f"điểm trung bình: {diem_trung_binh:.2f}")
print(f"xếp loại: {loai_diem}")