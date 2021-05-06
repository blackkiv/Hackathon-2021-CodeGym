from project.model.Users import Users
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
        return Users.query.filter_by(chat_id=chat_id).first() == None

    def get_user(self, chat_id: int) -> Users:
        return Users.query.filter_by(chat_id=chat_id).first()

    def user_on_page(self, chat_id: int, page: str) -> bool:
        user = Users.query.filter_by(chat_id=chat_id, page=page).first()
        return bool(user)

    @commitable
    def add_user(self, chat_id: int, page: str) -> Users:
        new_user = Users(
            chat_id=chat_id,
            page=page
        )

        db.session.add(new_user)

db.create_all()

dbmanager = DBManager()