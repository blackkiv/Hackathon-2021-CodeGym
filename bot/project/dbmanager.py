from project.model.User import User
from project.model.TemporaryItem import TemporaryItem
from project import db
from time import time as current_time


class DBManager:

    def __init__(self):
        print("Created: <DBManager>")

    def commitable(function):
        def func_wrapper(*arguments, **kwargs):
            res = function(*arguments, **kwargs)
            db.session.commit()

            return res

        return func_wrapper

    def is_new_user(self, chat_id: int) -> bool:
        return User.query.filter_by(chat_id=chat_id).first() == None

    def get_user(self, chat_id: int) -> User:
        return User.query.filter_by(chat_id=chat_id).first()

    def get_temporary_item(self, chat_id: int) -> TemporaryItem:
        return TemporaryItem.query.filter_by(chat_id=chat_id).first()

    def user_on_page(self, chat_id: int, page: str) -> bool:
        user = User.query.filter_by(chat_id=chat_id, page=page).first()
        return bool(user)

    @commitable
    def add_user(self, chat_id: int, page: str) -> User:
        new_user = User(
            chat_id=chat_id,
            page=page
        )

        db.session.add(new_user)

    @commitable
    def update_page(self, chat_id: int, page: str):
        user = self.get_user(chat_id)
        user.page = page

    @commitable
    def add_temporary_item(self, chat_id: int):
        temporary_item = TemporaryItem(chat_id=chat_id)
        db.session.add(temporary_item)

    @commitable
    def delete_pending_temporary_item(self, chat_id: int):
        temporary_item = TemporaryItem.query.filter_by(chat_id=chat_id).first()
        if temporary_item != None:
            db.session.delete(temporary_item)

    @commitable
    def update_temporary_item_title(self, chat_id: int, title: str):
        temporary = self.get_temporary_item(chat_id)
        temporary.title = title

    @commitable
    def update_temporary_item_price(self, chat_id: int, price: int):
        temporary = self.get_temporary_item(chat_id)
        temporary.price = price

    @commitable
    def update_temporary_item_location(self, chat_id: int, longitude: float, latitude: float):
        temporary = self.get_temporary_item(chat_id)
        temporary.latitude = latitude
        temporary.longitude = longitude

db.create_all()
dbmanager = DBManager()