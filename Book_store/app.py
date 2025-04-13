from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from DB import db, Users, Category, Books

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

##############################
#          ROUTES           #
##############################

# ---------- Trang chủ ----------
@app.route('/')
def home():
    books = Books.query.all()
    return render_template('home.html', books=books)

# ---------- Đăng nhập ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Admin cứng
        if username == 'admin' and password == '123456':
            session['user'] = 'admin'
            session['role'] = 'admin'
            return redirect(url_for('admin'))

        # Kiểm tra user thường
        user = Users.query.filter_by(username=username, password=password).first()
        if user:
            session['user'] = user.username
            session['role'] = 'user'
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Sai tên đăng nhập hoặc mật khẩu!')

    return render_template('login.html')

# ---------- Đăng ký ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return render_template('register.html', error='Mật khẩu không khớp!')

        existing_user = Users.query.filter_by(username=fullname).first()
        if existing_user:
            return render_template('register.html', error='Tên đăng nhập đã tồn tại!')

        new_user = Users(username=fullname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')

# ---------- Đăng xuất ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    return redirect(url_for('home'))

# ---------- Trang admin ----------
@app.route('/admin')
def admin():
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    categories = Category.query.all()
    books = Books.query.all()
    return render_template('admin.html',
                           user=session['user'],
                           categories=categories,
                           books=books)

# ---------- Thêm danh mục ----------
@app.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        db.session.add(Category(name=name, description=description))
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('add_category.html')

# ---------- Thêm sách ----------
@app.route('/book/add', methods=['GET', 'POST'])
def add_book():
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    categories = Category.query.all()
    if request.method == 'POST':
        book = Books(
            title=request.form['title'],
            author=request.form['author'],
            price=request.form['price'],
            images=request.form['images'],
            cateid=request.form['cateid'],
            description=request.form['description']
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('add_book.html', categories=categories)

# ---------- Sửa danh mục ----------
@app.route('/category/edit/<int:cateid>', methods=['GET', 'POST'])
def edit_category(cateid):
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    category = Category.query.get_or_404(cateid)
    if request.method == 'POST':
        category.name = request.form['name']
        category.description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('edit_category.html', category=category)

# ---------- Sửa sách ----------
@app.route('/book/edit/<int:bid>', methods=['GET', 'POST'])
def edit_book(bid):
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    book = Books.query.get_or_404(bid)
    categories = Category.query.all()

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.price = request.form['price']
        book.images = request.form['images']
        book.cateid = request.form['cateid']
        book.description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('edit_book.html', book=book, categories=categories)

# ---------- chi tiết sách ----------
@app.route('/book/<int:bid>')
def book_detail(bid):
    # Tìm sách theo id
    book = Books.query.get_or_404(bid)
    return render_template('detail.html', book=book)


# ---------- Xóa danh mục  ----------
@app.route('/category/delete/<int:cateid>')
def delete_category(cateid):
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    category = Category.query.get_or_404(cateid)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin'))

# ---------- Xóa sách  ----------
@app.route('/book/delete/<int:bid>')
def delete_book(bid):
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    book = Books.query.get_or_404(bid)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('admin'))

# ---------- Xóa user----------
# @app.route('/user/delete/<int:uid>')
# def delete_user(uid):
#     if 'user' not in session or session.get('role') != 'admin':
#         return redirect(url_for('login'))

#     user = Users.query.get_or_404(uid)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
