from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove


remove_keyboard = ReplyKeyboardRemove()

main_buttons = {
	"search_item": "Знайти продукт",
	"add_item": "Додати продукт",
}
main = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
main.add(*main_buttons.values())

return_back_buttons = {
	"return_back": "Повернутися"
}
return_back = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
return_back.add(*return_back_buttons.values())

confirm_buttons = {
	"okay": "Все вірно!",
	"return_back": "Повернутися"
}
confirm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
confirm.add(*confirm_buttons.values())