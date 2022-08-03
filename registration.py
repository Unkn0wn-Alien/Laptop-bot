import re
from telegram import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from menu import main_menu, send_my_info


def get_first_name(update, context):
    message = update.message.text
    context.user_data["first_name"] = message
    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        context.user_data["step"] = 6
    else:
        context.user_data["step"] = 2
        update.message.reply_text(
            text="<b>Familiyangizni kiriting:</b>",
            parse_mode="HTML",
            reply_markup=ReplyKeyboardRemove()
        )


def get_last_name(update, context):
    message = update.message.text
    context.user_data["last_name"] = message
    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        context.user_data["step"] = 6
        send_my_info(update, context)
    else:
        context.user_data["step"] = 3
        update.message.reply_text(
            text="<b>Yoshingizni kiriting:</b>",
            parse_mode="HTML",
            reply_markup=ReplyKeyboardRemove()
        )


def get_age(update, context):
    message = update.message.text
    if re.search("^[0-9]+$", message):
        context.user_data["age"] = message
        if context.user_data.get("edit_step"):
            context.user_data["edit_step"] = False
            context.user_data["step"] = 6
            send_my_info(update, context)
        else:
            context.user_data["step"] = 4
            buttons = [
                [KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")]
            ]
            update.message.reply_text(
                text="<b>Jinsingizni tanlang:</b>",
                parse_mode="HTML",
                reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
            )
    else:
        update.message.reply_text(
            text="<b>Iltimos to'g'ri qiymat kiriting!</b>",
            parse_mode="HTML"
        )


def get_gender(update, context):
    message = update.message.text
    if re.search("^(Erkak|Ayol)$", message):
        context.user_data["gender"] = message
        if context.user_data.get("edit_step"):
            context.user_data["edit_step"] = False
            context.user_data["step"] = 6
            send_my_info(update, context)
        else:
            context.user_data["step"] = 5
            buttons = [
                [KeyboardButton(text="Jo'natish", request_contact=True)]
            ]
            update.message.reply_text(
                text="<b>Kontaktingizni jo'nating yoki qo'lda tering</b>",
                parse_mode="HTML",
                reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
            )
    else:
        update.messagereply_text(
            text="<b>Iltimos to'g'ri qiymat kiriting!</b>",
            parse_mod="HTML"
        )


def get_text_contact(update, context):
    message = update.message.text
    context.user_data["contact"] = message
    context.user_data["step"] = 6
    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        send_my_info(update, context)
    else:
        main_menu(update, context, message.from_user.id)
