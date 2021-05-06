from flask import Flask, request
from telebot.types import *
from project.bot import bot
import config

app = Flask(__name__)

from project.model import *

# all handlers import
from project.handlers.command_handler import *
from project.handlers.text_handler import *
from project.handlers.media_handler import *
from project.handlers.callback_handler import *


@app.route("/")
def index():
    return 200

@app.route(f"/{config.Config.secret}", methods=['POST'])
def webhook():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])

    return 'ok', 200