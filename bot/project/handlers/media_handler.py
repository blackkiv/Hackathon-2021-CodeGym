# Media handler file
# All media handlers for users live here
import project.pages as pages

from project.bot import bot
from project.processor import processor
from project.dbmanager import dbmanager
from project.coordinator import coordinator


@bot.message_handler(
	content_types=["location"],
	func=lambda m: dbmanager.user_on_page(m.chat.id, pages.enter_item_location)
)
def enter_item_location_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.handle_item_location(m)
	coordinator.send_text(response)