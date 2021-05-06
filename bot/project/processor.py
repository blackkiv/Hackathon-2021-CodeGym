# Processor file
# Created to divide processing messages and sending them
import project.pages as pages
from project.dbmanager import dbmanager
from project.coordinator import coordinator
from config import Config
from project.bot import bot
import project.messages as m
import project.keyboards as k

class Processor:

    def __init__(self):
        print("Created: <Processor>")

    def handle_start(self, message):
        response = {
            "chat_id": message.chat.id,
            "parse_mode": "HTML"
        }


        if dbmanager.is_new_user(message.chat.id):
            dbmanager.add_user(message.chat.id, pages.main)

        response["text"] = m.hello
        response["reply_markup"] = k.main

        # dbmanager.update_page(message.chat.id, pages.main)

        return response

processor = Processor()