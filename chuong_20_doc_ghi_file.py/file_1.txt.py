#Đọc ghi file

#C:\Users\luong\Desktop\24174600069_Luong_Thanh_Tung_DHKL18A2\24174600069_Luong_Thanh_Tung_DHKL18A2\file_a.txt
#file_a.txt
#folder_upload\file_a.txt
open_file= open(file="file_a.txt", mode="r")
#r: chỉ đọc file từ đầu đến cuối, nếu tệp tin không tồn tại sẽ 
#r+: đọc và ghi tệp tin từ dòng đầu đến cuối, nếu tệp tin ko tồn tại
#w: mở và ghi tệp tin (ghi đè), nếu tệp tin không tồn tại, tạo tệp tin mới
#w+: đọc và ghi tệp tin(ghi đè), nếu tệp tin không tồn tại, tạo tệp tin mới
#a: mở và ghi vào cuối tệp tin, nếu tệp tin không tồn tại báo lỗi
#a+: đọc và ghi tệp tin, nếu tệp tin không tồn tại báo lỗi
print(open_file.readline(),end="")
print(open_file.readline(),end="")
print(open_file.readline(),end="")
open_file.close()

write_file = open(file="file_a.txt", mode="w")
write_file.write("chuoi thong tin moi")


