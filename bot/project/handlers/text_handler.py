# Text handler file
# All text handlers for users live here
import project.pages as pages
import project.keyboards as k

from project.bot import bot
from project.processor import processor
from project.coordinator import coordinator
from project.dbmanager import dbmanager


@bot.message_handler(
	content_types=["text"], 
	func=lambda m: m.text == k.return_back_buttons["return_back"]
)
def return_back_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.return_back(m)
	coordinator.send_text(response)

@bot.message_handler(
	content_types=["text"], 
	func=lambda m: (dbmanager.user_on_page(m.chat.id, pages.main) and m.text == k.main_buttons["add_item"])
)
def add_item_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.handle_add_item_click(m)
	coordinator.send_text(response)

@bot.message_handler(
	content_types=["text"], 
	func=lambda m: (dbmanager.user_on_page(m.chat.id, pages.enter_item_title))
)
def update_item_title_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.handle_item_title_enter(m)
	coordinator.send_text(response)

@bot.message_handler(
	content_types=["text"], 
	func=lambda m: (dbmanager.user_on_page(m.chat.id, pages.enter_item_price))
)
def update_item_price_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.handle_item_price_enter(m)
	coordinator.send_text(response)

@bot.message_handler(
	content_types=["text"], 
	func=lambda m: (dbmanager.user_on_page(m.chat.id, pages.confirm_product) and m.text == k.confirm_buttons["okay"])
)
def confirm_item_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.handle_confirm(m)
	coordinator.send_text(response)