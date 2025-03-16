from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import login_required
from app.models import Book, Author
from .forms import AddBookForm


main_blueprint = Blueprint("main", __name__, url_prefix="/")

@main_blueprint.route('/', methods=['GET'])
def index():
    books = Book.query.all()

    return render_template('main/index.html', books=books)

@main_blueprint.route('/book/<int:book_id>', methods=['GET'])
@login_required
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    print(book)
    return render_template('main/book_detail.html', book=book)

@main_blueprint.route('/author/<int:author_id>', methods=['GET'])
@login_required
def author_detail(author_id):
    author = Author.query.get_or_404(author_id)
    author_books = Book.query.filter_by(author_id=author_id).all()
    print(author_books)
    return render_template('main/author_detail.html', author=author, books=author_books)

@main_blueprint.route("/add_book", methods=["GET", "POST"])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        if form.validate_on_submit():

            author = Author.query.filter_by(name=form.author_name.data).first()
            if not author:
                author = Author(name=form.author_name.data)
                author.save_to_db()

        new_book = Book(
            name=form.name.data,
            publish_date=form.Publish_date.data,
            price=form.price.data,
            image=form.image.data,
            appropriate_age=form.appropriate_age.data,
            author_id=author.id,
        )
        new_book.save_to_db()
        return redirect(url_for("main.index"))
    return render_template("main/add_book.html", form=form)