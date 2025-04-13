from flask import Flask
from config import Config
from DB import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Đã tạo các bảng vào database thành công!")
