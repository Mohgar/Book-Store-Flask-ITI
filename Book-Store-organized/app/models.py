from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()




    __table_args__ = {"extend_existing": True}


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    added_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    appropriate_age = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    def __repr__(self):
        return f"<Book {self.name}>"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", backref="author")
    image = db.Column(db.String(200), nullable=False, default="images/default.jpg")


    __table_args__ = {"extend_existing": True}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()