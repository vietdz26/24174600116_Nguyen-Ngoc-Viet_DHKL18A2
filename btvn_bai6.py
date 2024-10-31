#bai6
import math
#chương trình hiển thị menu thể loại phim
def hien_thi_menu():
    print("chào mừng bạn đến với rạp chiếu phim")
    print("vui lòng chọn thể loại phim bạn muốn xem:")
    print("1. phim tình cảm")
    print("2. phim kinh dị")
    print("3. phim hoạt hình")
    print("4. phim khoa học viễn tưởng")
def chon_the_loai():
    lua_chon = input("nhập lựa chọn của bạn từ 1 đến 4:")
    if lua_chon == "1" :
        print("bạn dã chọn phim tình cảm")
    elif lua_chon =="2" :
        print("bạn đã chọn phim kinh dị")
    elif lua_chon =="3":
        print("bạn đã chọn phim hoạt hình")
    elif lua_chon =="4":
        print("bạn đã chọn phim khoa học viễn tưởng")
#gọi hàm để chạy chương trình
chon_the_loai()