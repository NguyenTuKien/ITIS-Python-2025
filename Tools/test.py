from sys import stdin
import json

# Nhiệm vụ: Viết hàm đệ quy để "duyệt" toàn bộ cây dữ liệu này và trả về một Tuple chứa 3 thông tin thống kê sau:
# Danh sách tên các Quốc gia (Key) mà có Thủ đô (Value) bắt đầu bằng nguyên âm (u, e, o, a, i - không phân biệt hoa thường). 
# Danh sách phải được sắp xếp theo thứ tự bảng chữ cái.
# Tổng số lượng Quốc gia có tên dài hơn 5 ký tự (tính cả khoảng trắng).
# Tổng số lượng Thủ đô có tên ngắn hơn 6 ký tự.

def travel(data):
    nat = {}
    for key, val in data.items():
        if isinstance(val, dict):
            child = travel(val)
            nat.update(child)
        elif isinstance(val, str):
            nat[key] = val
    return nat


cnt_cap, cnt_nat = 0, 0
world = json.loads(stdin.read())
ls_nat = travel(world)
ls_cap = []
for nat, cap in ls_nat.items():
    if len(nat) > 5 : 
        cnt_nat += 1
    if cap[0] in "aeiouAEIOU":
        ls_cap.append(nat)
    if len(cap) < 6:
        cnt_cap += 1
ans = (ls_cap, cnt_nat, cnt_cap)
print(ans)
