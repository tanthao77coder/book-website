BookStore - Web Bán Sách
BookStore là dự án web bán sách mini được phát triển bằng Flask (Python), cho phép người dùng duyệt qua danh sách sách, thêm vào giỏ hàng, xem chi tiết, đăng nhập/đăng ký, và quản trị (admin).

1. Công nghệ sử dụng:
- Python 3.x
- Flask (Framework web)
- MySQL (Quản lý dữ liệu)
- Bootstrap 5 (Giao diện)
- Jinja2 (Template engine mặc định của Flask)

2. Chức năng chính
Trang chủ:
- Hiển thị danh sách sách, banner.
- Đăng nhập/Đăng ký/Đăng xuất.
- Chi tiết sách:
- Hiển thị thông tin sách, mô tả, ảnh, danh mục.
- Cho phép thêm vào giỏ hàng.

Giỏ hàng:
- Thêm, xóa, xem tổng tiền.
- Xem nhanh nội dung giỏ hàng.

Quản trị (dành cho admin):
- Thêm, sửa, xóa sách và danh mục.
- Quản lý người dùng (nếu có).

3. Hướng dẫn cài đặt
Bước 1. Clone dự án
Trên máy tính, mở terminal (hoặc Git Bash), chạy:
bash
Sao chép
Chỉnh sửa
git clone https://github.com/<tên-tài-khoản-git>/<tên-repo-bookstore>.git
Vào thư mục dự án:

bash
Sao chép
Chỉnh sửa
cd bookstore
Bước 2. Cài đặt Python
Đảm bảo đã cài Python 3.x:

Kiểm tra phiên bản:

bash
Sao chép
Chỉnh sửa
python --version
Nếu chưa, tải và cài từ python.org.

Bước 3. Tạo và kích hoạt môi trường ảo (venv)
bash
Sao chép
Chỉnh sửa
# Tạo venv
python -m venv venv

# Kích hoạt môi trường ảo
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
Bước 4. Cài đặt thư viện cần thiết
Trong thư mục dự án đã clone:

bash
Sao chép
Chỉnh sửa
pip install -r requirements.txt
Lưu ý: Nếu bạn chưa có file requirements.txt, có thể tự tạo nhanh bằng lệnh:

bash
Sao chép
Chỉnh sửa
pip freeze > requirements.txt
Bước 5. Cấu hình Database (MySQL)
Cài đặt MySQL nếu chưa (XAMPP hoặc MySQL Community).

Tạo database book_store (hoặc tên khác).

Kiểm tra/mở file config.py (hoặc nơi bạn lưu config DB), chỉnh MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE phù hợp.

Bước 6. Khởi tạo bảng (nếu cần)
Nếu bạn chưa tạo bảng, hãy chạy script setup DB (ví dụ setup_database.py) hoặc chạy lệnh db.create_all() trong code (nếu có).

Ví dụ:

bash
Sao chép
Chỉnh sửa
python setup_database.py
Hoặc truy cập MySQL và tạo các bảng (books, category, users) thủ công.

Bước 7. Chạy dự án
bash
Sao chép
Chỉnh sửa
python app.py
hoặc:

bash
Sao chép
Chỉnh sửa
flask run
Truy cập trình duyệt tại:
http://127.0.0.1:5000

4. Cấu trúc thư mục (gợi ý)
bash
Sao chép
Chỉnh sửa
bookstore/
├── app.py
├── config.py
├── DB.py
├── requirements.txt
├── static/
│   ├── ...
├── templates/
│   ├── home.html
│   ├── detail.html
│   ├── cart.html
│   ├── ...
└── ...
5. Tác giả & Đóng góp
Tác giả: Đào Văn Thơm (thay tên bạn)

Đóng góp: Mọi ý kiến, PR, issue được hoan nghênh.
