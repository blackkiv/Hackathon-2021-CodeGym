from telebot.types import ReplyKeyboardMarkup


main_buttons = {
	"search_item": "Знайти продукт",
	"add_item": "Додати продукт",
}
main = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
main.add(*main_buttons.values())