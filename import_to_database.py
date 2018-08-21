import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)


def main():
    db.create_all()
    print("I've just create tables :)")
    file = open("books.csv")
    reader = csv.reader(file)

    for i, isbn, title, author, year in enumerate(reader):
        book = Books(isbn=isbn, title=title, author=author, year=year)
        db.session.add(book)
        print(i, "-th", isbn, title, author, year)
        db.session.commit()
    print("I'm committing")
    print("Ok")

if __name__ == "__main__":
    with app.app_context():
        main()
