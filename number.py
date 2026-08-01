import sys

# Nhận dữ liệu nhập từ người dùng
lst = input("Nhập số điện thoại: ").strip()
ls_len = len(lst)
ls_ex = []  # Danh sách kết quả

# Kiểm tra điều kiện đầu vào
if ls_len == 0:
    print("Lỗi: Vui lòng không để trống!")
    sys.exit()
elif ls_len < 10:
    print("Lỗi: Số điện thoại chưa đủ độ dài (tối thiểu 10 số)!")
    sys.exit()

# Bảng ánh xạ mã hóa cho từng chữ số (Dictionary)
encoding_map = {
    "0": "100 1000",
    "1": "100 1100",
    "2": "100 1010",
    "3": "111 0110",
    "4": "100 11011",
    "5": "101 01101",
    "6": "111 11111",
    "7": "1111 10001",
    "8": "1111 111101",
    "9": "1111 111001",
}

# Chuyển đổi từng chữ số
for num in lst:
    if num in encoding_map:
        ls_ex.append(encoding_map[num])

print(f"Số điện thoại sau khi mã hóa: {ls_ex}")
