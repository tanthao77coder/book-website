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
git clone https://github.com/tanthao77coder/book-website.git

Vào thư mục dự án:
cd book-website

Bước 2. Cài đặt Python
Kiểm tra phiên bản Python:
python --version
Nếu chưa cài, tải và cài đặt tại python.org.
Bước 3. Tạo và kích hoạt môi trường ảo
Tạo môi trường ảo:
python -m venv venv
Kích hoạt (tùy HĐH):
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Bước 4. Cài đặt thư viện cần thiết
pip install -r requirements.txt

Bước 5. Cấu hình Database (MySQL)
- Cài đặt MySQL nếu chưa (XAMPP hoặc MySQL Community).
- Tạo database book_store (hoặc tên khác).
- Mở file config.py (hoặc nơi bạn lưu config), kiểm tra MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE.
- Chạy script tạo bảng (setup_database.py hoặc db.create_all()) nếu cần.

Bước 6. Chạy dự án
python app.py
hoặc:
flask run
Sau đó, truy cập ứng dụng tại:
http://127.0.0.1:5000

4. Tác giả
Tác giả: Đào Tấn Thảo

