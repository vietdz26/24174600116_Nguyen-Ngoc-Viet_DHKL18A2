def dem_so_tu():
    #nhập chuỗi từ người dùng
    input_string = input("hôm nay  trời mưa ").strip()
    #tách chuỗi thành danh sách các từ , loại bỏ khỏang trắng thừa 
    words = input_string.split()
    #đếm số từ 
    so_tu = len(words)
    #in kết qủa 
    print(f"số từ trong chuỗi vừa nhập là : {so_tu}")


