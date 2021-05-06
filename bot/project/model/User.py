import project.pages as pages

from project import db
from sqlalchemy import Column, Integer, String, ForeignKey


class User(db.Model):

    __tablename__ = "users"
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer(), unique=True)
    page = db.Column(db.String(), default=pages.no_page)

    def __repr__(self):
        return f"<User {self.chat_id}>"