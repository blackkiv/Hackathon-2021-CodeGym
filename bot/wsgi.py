from project import app
from project.bot import bot
from config import Config


bot.delete_webhook()
bot.set_webhook(url=Config.webhook_url)
if __name__ == "__main__":
    app.run()