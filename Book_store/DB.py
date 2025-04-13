from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

# Bảng Users
class Users(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Boolean, default=False)

# Bảng Books
class Books(db.Model):
    bid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    price = db.Column(db.Float)
    images = db.Column(db.String(255))
    cateid = db.Column(db.Integer, db.ForeignKey('category.cateid'))
    description = db.Column(db.Text)

# Bảng Category
class Category(db.Model):
    cateid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    books = db.relationship('Books', backref='category')

# Bảng Orders
class Orders(db.Model):
    orderid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    order_date = db.Column(db.DateTime)
    total_amount = db.Column(db.Float)
    orderdetails = db.relationship('OrderDetail', backref='orders')

# Bảng OrderDetail
class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.orderid'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.bid'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

    # Tạo liên kết tới bảng Books
    book = db.relationship('Books', backref='orderdetails')
