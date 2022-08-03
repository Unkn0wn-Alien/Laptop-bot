from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ReplyKeyboardRemove, ChatAction
from menu import main_menu
from message_handler import message_handler
from inline import inline_handler

TOKEN = "5340443507:AAGyCbG__leiqYld_OHAFoGWZHHbt63i_2o"

steps = {
    "first_name": 1,
    "last_name": 2,
    "age": 3,
    "gender": 4,
    "contact": 5,
    "menu": 6
}


def start_handler(update, context):
    user = update.message.from_user
    update.message.reply_chat_action(action=ChatAction.TYPING)
    if context.user_data.get("first_name"):
        main_menu(update, context, user.id)
    else:
        context.user_data["step"] = steps["first_name"]
        update.message.reply_text(
            text="<b>Ismingizni kiriting:</b>",
            parse_mode="HTML",
            reply_markup=ReplyKeyboardRemove()
        )


def contact_handler(update, context):
    step = context.user_data.get("step", 0)
    user = update.message.from_user
    if step == steps["contact"]:
        context.user_data["contact"] = update.message.contact.phone_number
        context.user_data["step"] = steps["menu"]
        main_menu(update, context, user.id)


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
