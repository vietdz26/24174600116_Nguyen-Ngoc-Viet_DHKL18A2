#xử lý 
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#nhân a với n 
for hang in range (len(matrix_a)):
    for cot in range (len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n 
print(matrix_a)
#cộng 
ma_tran_a = [[0,5,8],
             [8,6,9],
             [1,1,2]],
ma_tran_b = [[0,7,1],
             [8,6,5],
             [1,2,2]],
ket_qua = [[0,0,0],
           [0,0,0],
           [0,0,0]]
for h in range (len(ma_tran_a)):
    for c in range (len(ma_tran_a[0])):
        ket_qua[h][c] = ma_tran_a[h][c] + ma_tran_b[h][c]
print(f"nhân hai ma trận: {ket_qua}") 
#trừ 
ma_tran_1 = [[2,4,5,6],
             [3,5,6,1],
             [4,9,0,3],
             [2,2,8,6]],
ma_tran_2 = [[2,4,5,6],
             [5,4,6,1],
             [4,7,0,3],
             [1,2,8,6]],
ket_qua = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
for hang in range (len(ma_tran_1)):
    for cot in range (len(ma_tran_1[0])):
        ket_qua[hang][cot] = ma_tran_1[hang][cot] - ma_tran_2[hang][cot]
for tru_hai_ma_tran in ket_qua: #dùng dấu gạch dưới nếu không cần biến 
    print(f"trừ hai ma trận: {tru_hai_ma_tran}")
#nhân 
matrix_a = [[2,4],
            [2,7]],
matrix_b = [[3,6],
            [2,2]],
ket_qua = [[0,0],
           [0,0]]
for h in range (len(matrix_a)):
    for c in range (len(matrix_a[h])):
        ket_qua[h][c] = matrix_a[h][c] * matrix_b[h][c]
print(f"nhân hai ma trận: {ket_qua}")
#chia
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8 
#chia ma trận a với n 
for hang in range (len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] / n
print("matrix_a ")