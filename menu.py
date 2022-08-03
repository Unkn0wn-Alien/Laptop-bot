from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup


def main_menu(update, context, chat_id):
    buttons = [
        [KeyboardButton(text="Mahsulotlar"), KeyboardButton(text="Men haqimda")],
        [KeyboardButton(text="Noutbuklar")]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text="Asosiy menyu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )


def send_my_info(update, context):
    data = context.user_data
    buttons = [
        [InlineKeyboardButton(text="Ma'lumotlarni o'zgartirish", callback_data="edit_data")],
        [InlineKeyboardButton(text="Asosiy menyu", callback_data="main_menu")]
    ]
    msg = update.message.reply_text(
        text="Waiting...",
        reply_markup=ReplyKeyboardRemove()
    )
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id)
    update.message.reply_text(
        text=f"<b>Ism:</b> {data['first_name']}\n"
             f"<b>Familiya:</b> {data['last_name']}\n"
             f"<b>Yosh:</b> {data['age']}\n"
             f"<b>Jinsi:</b> {data['gender']}\n"
             f"<b>Telefon raqami:</b> {data['contact']}\n",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )


def product_info(update, context):
    data = context.user_data
    buttons = [
        [InlineKeyboardButton(text="Apple telefonlari", callback_data="apple_product")],
        [InlineKeyboardButton(text="Samsung telefonlari", callback_data="samsung_product")],
        [InlineKeyboardButton(text="Asosiy menyu", callback_data="main_menu")]
    ]
    msg = update.message.reply_text(
        text="Waiting...",
        reply_markup=ReplyKeyboardRemove()
    )
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id)
    update.message.reply_text(
        text="Mahsulotlar",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
