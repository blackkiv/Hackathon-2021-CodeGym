# Processor file
# Created to divide processing messages and sending them
from project.dbmanager import dbmanager
from project.pages import Pages
from project.coordinator import coordinator
from config import Config
from project.bot import bot
import project.messages as m
import project.keyboards as k

from telebot.types import InputMediaPhoto, InlineKeyboardMarkup


class Processor:

    def __init__(self):
        print("Created: <Processor>")

processor = Processor()