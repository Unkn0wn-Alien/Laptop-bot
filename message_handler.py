from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
import registration
from menu import send_my_info, product_info
from notebooks_main import message_handler_notebooks

def message_handler(update, context):
    message = update.message.text
    step = context.user_data.get("step", 0)

    if step == 1:
        registration.get_first_name(update, context)
    elif step == 2:
        registration.get_last_name(update, context)
    elif step == 3:
        registration.get_age(update, context)
    elif step == 4:
        registration.get_gender(update, context)
    elif step == 5:
        registration.get_text_contact(update, context)
    elif step == 6:
        if message == "Men haqimda":
            send_my_info(update, context)
        elif message == "Mahsulotlar":
            product_info(update, context)
        elif message == "Noutbuklar":
            message_handler_notebooks(update, context)
