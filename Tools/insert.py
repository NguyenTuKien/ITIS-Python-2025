import os
import csv

# 1. Tạo thư mục chứa data (giống cấu trúc bài làm của bạn)
# Nó sẽ tạo folder "Data" và "Smart_building" ngay tại nơi bạn chạy script này
base_dir = os.path.join(os.getcwd(), 'Data', 'Smart_building')
os.makedirs(base_dir, exist_ok=True)

print(f"Đang tạo dữ liệu tại: {base_dir}")

# Header chuẩn
header = ['Time', 'DeviceType', 'Consumption', 'State']

# --- DANH SÁCH 10 FILE TEST ---

# 1. tang1_M01.csv (Chuẩn)
data_1 = [
    header,
    ['08:00', 'Light', '10', 'Normal'],
    ['09:00', 'AC', '50', 'Normal'],
    ['10:00', 'Fan', '5', 'Normal']
]

# 2. tang1_M02.csv (FILE RỖNG -> Bad File)
data_2 = [] 

# 3. tang1_M03.csv (Có dòng lỗi Maintenance, Spike -> Test lọc dữ liệu)
data_3 = [
    header,
    ['08:00', 'Server', '100', 'Normal'],
    ['09:00', 'Server', '500', 'Spike'],      # Bỏ qua
    ['10:00', 'Fan', '5', 'Maintenance']      # Bỏ qua
]

# 4. tang2_M01.csv (Chuẩn - Tầng 2)
data_4 = [
    header,
    ['08:00', 'AC', '60', 'Normal'],
    ['13:00', 'AC', '60', 'Normal']
]

# 5. tang2_M02.csv (FILE RỖNG -> Bad File)
data_5 = []

# 6. tang2_M03.csv (Có số âm -> Test điều kiện > 0)
data_6 = [
    header,
    ['08:00', 'Light', '20', 'Normal'],
    ['09:00', 'Light', '-50', 'Normal'],      # Bỏ qua
    ['10:00', 'Light', '0', 'Normal']         # Bỏ qua (đề bài >0)
]

# 7. tang3_M01.csv (Chuẩn - Tầng 3)
data_7 = [
    header,
    ['07:00', 'Pump', '30', 'Normal']
]

# 8. tang3_M02.csv (Toàn bộ là Maintenance -> File OK nhưng tổng điện = 0)
data_8 = [
    header,
    ['07:00', 'Elevator', '50', 'Maintenance'],
    ['08:00', 'Elevator', '50', 'Maintenance']
]

# 9. tangG_M01.csv (Tầng G - Thiết bị tiêu thụ lớn để test Max Device)
data_9 = [
    header,
    ['08:00', 'Server', '200', 'Normal'],
    ['09:00', 'Server', '200', 'Normal']
]

# 10. tangG_M02.csv (FILE RỖNG -> Bad File)
data_10 = []

# --- HÀM GHI FILE ---
files_to_create = {
    'tang1_M01.csv': data_1,
    'tang1_M02.csv': data_2,
    'tang1_M03.csv': data_3,
    'tang2_M01.csv': data_4,
    'tang2_M02.csv': data_5,
    'tang2_M03.csv': data_6,
    'tang3_M01.csv': data_7,
    'tang3_M02.csv': data_8,
    'tangG_M01.csv': data_9,
    'tangG_M02.csv': data_10,
}

for filename, content in files_to_create.items():
    file_path = os.path.join(base_dir, filename)
    
    # Nếu content rỗng -> Tạo file rỗng (0 byte)
    if not content:
        with open(file_path, 'w') as f:
            pass # Không ghi gì cả
    else:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(content)

print("Xong! Đã tạo 10 file CSV (3 file rỗng, 7 file có nội dung).")