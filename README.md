# python-number-phone

[![PyPI](https://img.shields.io/pypi/v/python-number-phone.svg)](#) [![Build Status](https://img.shields.io/github/actions/workflow/status/KhoaDang2011/python-number-phone/ci.yml)](#) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Mô tả ngắn: Thư viện Python để phân tích, xác thực và định dạng số điện thoại quốc tế và nội địa một cách đơn giản và nhất quán.

## Tính năng
- Phân tích (parse) số điện thoại từ chuỗi (hỗ trợ mã quốc gia).
- Xác thực số điện thoại theo chuẩn cơ bản (độ dài, ký tự).
- Định dạng số điện thoại theo các kiểu: E.164, quốc tế, nội địa.
- Hỗ trợ nhiều mã vùng/quốc gia (có thể mở rộng dữ liệu vùng).

## Yêu cầu
- Python 3.8+
- (Tùy chọn) pytest để chạy test

## Cài đặt
Cách đơn giản nhất (nếu đã publish lên PyPI):
```bash
pip install python-number-phone
```

Cài đặt từ mã nguồn:
```bash
git clone https://github.com/KhoaDang2011/python-number-phone.git
cd python-number-phone
pip install .
```

## Sử dụng nhanh
Lưu ý: tên module trong ví dụ dưới đây là `number_phone` — điều chỉnh theo tên module/tệp thực tế trong repo nếu khác.

Ví dụ cơ bản:
```python
from number_phone import parse, is_valid, format_number, PhoneNumber

# phân tích chuỗi thành đối tượng PhoneNumber
pn = parse("+84123456789")
print(pn.country)           # 'VN' hoặc mã quốc gia tương ứng
print(pn.national_number)   # '123456789'

# kiểm tra hợp lệ
print(is_valid("+84123456789"))  # True / False

# định dạng
print(format_number(pn, fmt="E164"))         # +84123456789
print(format_number(pn, fmt="INTERNATIONAL"))# +84 123 456 789
print(format_number(pn, fmt="NATIONAL"))     # 0123 456 789
```

API tham khảo (ví dụ, điều chỉnh theo implementation):
- parse(number_str: str, default_region: str | None = None) -> PhoneNumber
- is_valid(number_str: str, region: str | None = None) -> bool
- format_number(phone: PhoneNumber | str, fmt: Literal["E164","INTERNATIONAL","NATIONAL"]) -> str
- class PhoneNumber:
  - attributes: country (str), country_code (int), national_number (str), raw_input (str)

## Ví dụ phức tạp hơn
Xử lý danh sách số và lọc hợp lệ:
```python
from number_phone import parse, is_valid, format_number

phones = ["+84123456789", "0123456789", "12345"]
valid_formatted = []

for p in phones:
    if is_valid(p, region="VN"):
        obj = parse(p, default_region="VN")
        valid_formatted.append(format_number(obj, fmt="E164"))

print(valid_formatted)
```

## Chạy test
Sử dụng pytest (nếu có test tích hợp):
```bash
pip install -r requirements-dev.txt
pytest
```

## Đóng góp
Rất hoan nghênh PR và issue:
- Mở issue để mô tả lỗi hoặc đề xuất tính năng.
- Tạo branch riêng theo nhánh chính: `feature/<mô-tả>` hoặc `fix/<mô-tả>`.
- Viết test cho thay đổi nếu cần.
- Gửi PR mô tả rõ thay đổi và lý do.

## Lộ trình (TODO)
- Hỗ trợ dữ liệu vùng chi tiết hơn (validation theo từng quốc gia).
- Tích hợp với thư viện chuẩn (nếu cần) để nâng cao độ chính xác.
- Internationalization cho thông báo lỗi.

## License
MIT — xem file LICENSE để biết chi tiết.

## Liên hệ
Tác giả: KhoaDang2011  
Repo: https://github.com/KhoaDang2011/python-number-phone

Nếu bạn muốn, mình có thể:
- Điều chỉnh README theo API thực tế của repo (nêu tên module / các hàm chính).
- Tạo file README.md trực tiếp trong repo cho bạn (cần quyền hoặc xác nhận owner/repo để thực hiện).
```
