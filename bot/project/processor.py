# Processor file
# Created to divide processing messages and sending them
import project.pages as pages
import project.messages as m
import project.keyboards as k

from project.dbmanager import dbmanager
from project.coordinator import coordinator
from project.API import api
from config import Config
from project.bot import bot
from project.model.GeoEncodingRequest import GeoEncodingRequest
from project.model.AddProductRequest import AddProductRequest


class Processor:

    def __init__(self):
        print("Created: <Processor>")

    def return_back(self, message):
        
        page = dbmanager.get_user(message.chat.id).page

        if page == pages.enter_item_title:
            return self.handle_start(message)

        elif page == pages.enter_item_price:
            return self.handle_add_item_click(message)

        elif page == pages.enter_item_location:
            return self.handle_item_title_enter(message, True)

        elif page == pages.confirm_product:
            return self.handle_item_price_enter(message, True)

        elif page == pages.search:
            return self.handle_start(message)


    def handle_start(self, message):
        if dbmanager.is_new_user(message.chat.id):
            dbmanager.add_user(message.chat.id, pages.main)

        dbmanager.update_page(message.chat.id, pages.main)

        return {
            "chat_id": message.chat.id,
            "parse_mode": "HTML",
            "text": m.hello,
            "reply_markup": k.main
        }

    def handle_add_item_click(self, message):

        dbmanager.update_page(message.chat.id, pages.enter_item_title)
        dbmanager.delete_pending_temporary_item(message.chat.id)
        dbmanager.add_temporary_item(message.chat.id)

        return {
            "chat_id": message.chat.id,
            "parse_mode": "HTML",
            "text": m.enter_product_name,
            "reply_markup": k.return_back
        }

    def handle_item_title_enter(self, message, from_return=False):

        if not from_return:
            title = message.text.replace("<", "").replace(">", "").replace("/", "")
        else :
            title = dbmanager.get_temporary_item(message.chat.id).title

        dbmanager.update_page(message.chat.id, pages.enter_item_price)
        dbmanager.update_temporary_item_title(message.chat.id, title)

        return {
            "chat_id": message.chat.id,
            "parse_mode": "HTML",
            "text": m.enter_product_price,
            "reply_markup": k.return_back
        }

    def handle_item_price_enter(self, message, from_return=False):

        if from_return:

            dbmanager.update_page(message.chat.id, pages.enter_item_location)

            return {
                "chat_id": message.chat.id,
                "parse_mode": "HTML",
                "text": m.enter_product_shop_location,
                "reply_markup": k.return_back
            }
        else :
            price = 0.0

            try:
                price = abs(int(float(message.text) * 100) / 100)

                dbmanager.update_page(message.chat.id, pages.enter_item_location)
                dbmanager.update_temporary_item_price(message.chat.id, price)

                return {
                    "chat_id": message.chat.id,
                    "parse_mode": "HTML",
                    "text": m.enter_product_shop_location,
                    "reply_markup": k.return_back
                }

            except ValueError as e:
                return {
                    "chat_id": message.chat.id,
                    "parse_mode": "HTML",
                    "text": m.enter_error,
                    "reply_markup": k.return_back
                }

    def handle_item_location(self, message):
        longitude = message.location.longitude
        latitude = message.location.latitude

        response = api.get_geo(GeoEncodingRequest(latitude, longitude))

        if response.status_code == 200:
            address = response.json()["address"]

            dbmanager.update_temporary_item_location(message.chat.id, longitude, latitude)
            dbmanager.update_page(message.chat.id, pages.confirm_product)
        
            item = dbmanager.get_temporary_item(message.chat.id)

            return {
                "chat_id": message.chat.id,
                "parse_mode": "HTML",
                "text": m.product_preview.format(
                    title=item.title,
                    price=item.price,
                    address=address
                ),
                "reply_markup": k.confirm
            }

        else:
            return {
                "chat_id": message.chat.id,
                "parse_mode": "HTML",
                "text": m.location_error
            }

    def handle_confirm(self, message):
        
        dbmanager.update_page(message.chat.id, pages.main)
        item = dbmanager.get_temporary_item(message.chat.id)

        api.send_product(AddProductRequest(
            item.title,
            item.price,
            item.latitude,
            item.longitude
        ))

        return {
            "chat_id": message.chat.id,
            "parse_mode": "HTML",
            "text": m.added_product_thank,
            "reply_markup": k.main
        }

    def handle_search_click(self, message):

        dbmanager.update_page(message.chat.id, pages.search)

        return {
            "chat_id": message.chat.id,
            "text": m.search_enter_title,
            "reply_markup": k.return_back
        }

    def handle_search(self, message):

        search_response = api.search_product(message.text).json()

        message_text = [f"<b>{index+1}. {item['name']}</b> за {item['price']} ₴\nДе: {item['address']}" for index, item in enumerate(search_response)]

        if message_text == []:

            return {
                "chat_id": message.chat.id,
                "text": m.search_no_items,
                "reply_markup": k.return_back
            }
        else: 
            return {
                "chat_id": message.chat.id,
                "text": "\n\n".join(message_text),
                "reply_markup": k.return_back
            }



processor = Processor()