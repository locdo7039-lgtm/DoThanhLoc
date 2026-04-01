import random
import math
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# --- Yêu cầu 1: Nhập a, b và tính tổng, hiệu, tích, thương ---
print("--- Bài 1 ---")
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))

print(f"Tổng của a và b là: {a + b}")
print(f"Hiệu của a và b là: {a - b}")
print(f"Tích của a và b là: {a * b}")

if b != 0:
    print(f"Thương của a và b là: {a / b}")
else:
    print("Thương: Không thể thực hiện phép chia cho 0!")

# --- Yêu cầu 2: Lấy các ký tự từ chỉ số 2 đến 4 (llo) ---
print("\n--- Bài 2 ---")
chuoi_1 = "Hello World"
ket_qua_cat = chuoi_1[2:5] 
print(f"Các ký tự từ chỉ số 2 đến 4 của '{chuoi_1}' là: {ket_qua_cat}")

# --- Yêu cầu 3: Xử lý khoảng trắng, hoa/thường và thay thế ký tự ---
print("\n--- Bài 3 ---")
chuoi_2 = " Hello World "
chuoi_chuan = chuoi_2.strip()
print(f"Chuỗi sau khi xóa khoảng trắng: '{chuoi_chuan}'")
print(f"Chuỗi in hoa: {chuoi_chuan.upper()}")
print(f"Chuỗi in thường: {chuoi_chuan.lower()}")
chuoi_thay_the = chuoi_chuan.replace('H', 'J')
print(f"Chuỗi sau khi thay 'H' thành 'J': {chuoi_thay_the}")

# --- Yêu cầu 4, 5, 6, 7, 8, 9 ---
print("\n--- Bài 4 đến 9 ---")
if a > b:
    print("Hello World! (Bài 4)")

print("Bài 5: ", end="")
if a == b:
    print("Yes")
else:
    print("No")

a_test, b_test, c_test, d_test = 5, 5, 3, 5
print("Bài 6: ", end="")
if a_test == b_test:
    print(1)
elif a_test > b_test:
    print(2)
else:
    print(3)

if a_test == b_test and b_test == d_test:
    print("Bài 7: Hello World!")

if a_test == b_test or c_test == d_test:
    print("Bài 8: Hello World!")

max_val = a_test if a_test > b_test else b_test
print(f"Bài 9: Giá trị lớn nhất giữa a_test và b_test là: {max_val}")

# --- Yêu cầu 10 ---
print("\n--- Bài 10 ---")
a_10 = int(input("Nhập số a: "))
b_10 = int(input("Nhập số b: "))
print("Kết quả câu lệnh: ", end="")
print("A") if a_10 > b_10 else print("=") if a_10 == b_10 else print("B")

# --- Yêu cầu 11, 12, 13 ---
print("\n--- Bài 11 ---")
n_11 = int(input("Nhập số phần tử của mảng a: "))
a_arr = [random.randint(1, 100) for _ in range(n_11)]
b_arr = [x for x in a_arr if x % 2 == 0]
print(f"Mảng a: {a_arr}")
print(f"Mảng b (các số chẵn): {b_arr}")

print("\n--- Bài 12 ---")
tong = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(f"Tổng các số < 1000 là bội của 3 hoặc 5: {tong}")

print("\n--- Bài 13 ---")
def tron_mang(mang1, mang2):
    ket_qua = []
    max_len = max(len(mang1), len(mang2))
    for i in range(max_len):
        val1 = mang1[i] if i < len(mang1) else 0
        val2 = mang2[i] if i < len(mang2) else 0
        ket_qua.append(val1 + val2)
    return ket_qua

mang_a_13 = [3, 9, 1, 4]
mang_b_13 = [2, 7, 4, 3, 2, 8]
print(f"Kết quả trộn mảng: {tron_mang(mang_a_13, mang_b_13)}")

# --- Yêu cầu 14: Ma trận ---
print("\n--- Bài 14 ---")
m = int(input("Nhập số dòng m: "))
n = int(input("Nhập số cột n: "))
matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]

print("Mảng 2 chiều đã tạo:")
for row in matrix:
    print(row)

k_row = int(input(f"Nhập dòng k muốn xuất (0 đến {m-1}): "))
print(f"Các phần tử thuộc dòng {k_row}: {matrix[k_row]}")

k_col = int(input(f"Nhập cột k muốn xuất (0 đến {n-1}): "))
col_elements = [row[k_col] for row in matrix]
print(f"Các phần tử thuộc cột {k_col}: {col_elements}")

max_sum_row = max(matrix, key=sum)
print(f"Dòng có tổng lớn nhất: {max_sum_row} (Tổng = {sum(max_sum_row)})")

def tich_cot(col_idx):
    return math.prod(row[col_idx] for row in matrix)

min_prod_col_idx = min(range(n), key=tich_cot)
print(f"Cột có tích nhỏ nhất là cột {min_prod_col_idx} (Tích = {tich_cot(min_prod_col_idx)})")

print("Các phần tử thuộc dòng chẵn, cột lẻ:")
for i in range(m):
    for j in range(n):
        if i % 2 == 0 and j % 2 != 0:
            print(f"A[{i}][{j}] = {matrix[i][j]}", end=" | ")
print()

pt_chan_dong_le = [matrix[i][j] for i in range(m) if i % 2 != 0 for j in range(n) if matrix[i][j] % 2 == 0]
if pt_chan_dong_le:
    print(f"TBC các phần tử chẵn thuộc dòng lẻ: {sum(pt_chan_dong_le) / len(pt_chan_dong_le)}")
else:
    print("Không có phần tử chẵn nào nằm trên dòng lẻ.")

pt_bien = []
for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            pt_bien.append(matrix[i][j])
if pt_bien:
    print(f"TBC các phần tử biên: {sum(pt_bien) / len(pt_bien)}")

# --- Yêu cầu 15: Sinh viên ---
print("\n--- Bài 15 ---")
class SinhVien:
    def __init__(self, ma_sv, ten, nam_sinh, diem_tb):
        self.ma_sv = str(ma_sv)[:10]
        self.ten = str(ten)[:20]
        self.nam_sinh = int(nam_sinh)
        self.diem_tb = float(diem_tb)

danh_sach_sv = [
    SinhVien("02DH0001", "Phan Thi Lan", 2004, 7.5),
    SinhVien("01CD0002", "Nguyen Van A", 2007, 4.0),
    SinhVien("03DH0003", "Phan Van B", 2003, 8.0),
    SinhVien("04DH0004", "Le Thi Lan", 2006, 5.5)
]

print(f"Số SV đủ điều kiện lên lớp: {sum(1 for sv in danh_sach_sv if sv.diem_tb >= 5)}")

nam_hien_tai = datetime.date.today().year
print("Các sinh viên đủ 20 tuổi:")
for sv in danh_sach_sv:
    if (nam_hien_tai - sv.nam_sinh) >= 20:
        print(f"- {sv.ten}")

print(f"Số SV hệ đại học: {sum(1 for sv in danh_sach_sv if len(sv.ma_sv) >= 4 and sv.ma_sv[2:4] == 'DH')}")
print(f"Số SV tên Lan: {sum(1 for sv in danh_sach_sv if sv.ten.split()[-1].upper() == 'LAN')}")
print(f"Số SV họ Phan: {sum(1 for sv in danh_sach_sv if sv.ten.split()[0].upper() == 'PHAN')}")

# --- BÀI TẬP VỀ NHÀ ---
print("\n--- Bài Tập Về Nhà ---")

# File I/O
with open("du_lieu.txt", "w", encoding="utf-8") as file:
    file.write("Dữ liệu thử nghiệm xử lý I/O\n")
    file.write("Dòng thứ hai trong file.")

with open("du_lieu.txt", "r", encoding="utf-8") as file:
    print("Nội dung file du_lieu.txt:\n", file.read())

# Pandas & Matplotlib
data = {
    'Môn học': ['CSDL', 'Hệ Điều Hành', 'Trí Tuệ Nhân Tạo', 'Xác Suất'],
    'Điểm Số': [8.5, 7.0, 9.0, 6.5]
}
df = pd.DataFrame(data)
print("\nBảng điểm Pandas:\n", df)

plt.bar(df['Môn học'], df['Điểm Số'], color='coral')
plt.title('Điểm số các môn chuyên ngành')
plt.xlabel('Môn học')
plt.ylabel('Điểm')
plt.ylim(0, 10)
# Lưu biểu đồ thành file ảnh thay vì mở cửa sổ (để chạy được trên GitHub Actions)
plt.savefig('bieu_do.png')
print("=> Đã lưu biểu đồ thành file ảnh bieu_do.png")

# Chạy thử hàm Trộn mảng Min
def tron_mang_min(a, b):
    ket_qua = []
    min_len = min(len(a), len(b))
    for i in range(min_len):
        ket_qua.append(min(a[i], b[i]))
    if len(a) > len(b):
        ket_qua.extend(a[min_len:])
    else:
        ket_qua.extend(b[min_len:])
    return ket_qua

print(f"\nKết quả trộn mảng Min: {tron_mang_min([3, 9, 1, 4], [2, 7, 4, 3, 2, 8])}")
print("\nCHƯƠNG TRÌNH KẾT THÚC THÀNH CÔNG!")
