# Command handler file
# All command handlers for users live here
from project.bot import bot
from project.processor import processor
from project.coordinator import coordinator


@bot.message_handler(commands=["start"])
def start_handler(m):
	coordinator.send_action(m.chat.id)
	response = processor.handle_start(m)
	coordinator.send_text(response)