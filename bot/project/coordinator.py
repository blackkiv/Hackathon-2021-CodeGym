# Coordinator file. Can also be called "Sender"
# Created to divide processing messages and sending them
from project.bot import bot
from config import Config, join


class Coordinator:
    def __init__(self):
        print("Created: <Coordinator>")

    def send_text(self, args):
        try:
            bot.send_message(**args)
        except Exception as e:
            print(e, args)

    def delete_message(self, args):
        try:
            bot.delete_message(**args)
        except Exception as e:
            print(e, args)

    def send_photo(self, args):
        try:
            bot.send_photo(**args)
        except Exception as e:
            print(e, args)

    def send_document(self, args):
        try:
            bot.send_document(**args)
        except Exception as e:
            print(e, args)

    def send_action(self, chat_id, action="typing"):
        try:
            bot.send_chat_action(chat_id, action)
        except Exception as e:
            print(e)

    def edit_message_text(self, args):
        try:
            bot.edit_message_text(**args)
        except Exception as e:
            print(e, args)

    def send_media_group(self, args):
        try:
            bot.send_media_group(**args)
        except Exception as e:
            print(e, args)

    def answer_callback_query(self, args):
        try:
            bot.answer_callback_query(**args)
        except Exception as e:
            print(e, args)


coordinator = Coordinator()