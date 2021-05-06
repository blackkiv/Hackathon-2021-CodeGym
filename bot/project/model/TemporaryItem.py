from project import db
from sqlalchemy import Column, Integer, String, ForeignKey


class TemporaryItem(db.Model):

    __tablename__ = "temporary_item"
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String, default="")
    price = db.Column(db.Integer, default=0)
    longitude = db.Column(db.String, default="0.0")
    latitude = db.Column(db.String, default="0.0")

    def __repr__(self):
        return f"<TemporaryItem {self.chat_id}>"