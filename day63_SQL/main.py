from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


def add_book(title, author, rating):
    """Add or Update and existing book"""
    # CREATE RECORD
    # Check if a book with the same title already exists
    with app.app_context():
        existing_book = Book.query.filter_by(title=title).first()

        if existing_book:
            # Update the existing record
            existing_book.author = author.strip().title()
            existing_book.rating = round(float(rating), 1)
            db.session.commit()
        else:
            # Create a new record
            new_book = Book(title=title.strip().title(), author=author.strip().title(), rating=round(float(rating), 1))
            db.session.add(new_book)
            db.session.commit()


# Use the Flask app context
with app.app_context():
    # Create the database and tables
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_book(request.form['title'], request.form['author'], request.form['rating'])
        return redirect('/')
    return render_template('add.html')


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    with app.app_context():
        book = Book.query.filter_by(id=id).first()
        if request.method == 'POST':
            book.rating = round(float(request.form["new_rating"]), 1)
            db.session.commit()
            return redirect('/')

    return render_template('update.html', book=book)


@app.route("/delete/<int:id>")
def delete(id):
    with app.app_context():
        book = Book.query.filter_by(id=id).first()
        # if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect('/')

    # return render_template('delete.html', book=book)


if __name__ == "__main__":
    app.run(debug=True)
