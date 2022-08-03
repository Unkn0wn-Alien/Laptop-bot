from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from menu import main_menu
from notebooks_main import inline_handler_notebooks


def inline_handler(update, context):
    query = update.callback_query
    data_sp = str(query.data).split("_")
    if data_sp[1] == "product":
        inline_handler_product(update, context)
    if data_sp[0] == "notebooks":
        inline_handler_notebooks(update, context)
    if query.data == "edit_data":
        buttons = [
            [
                InlineKeyboardButton(text="Ism", callback_data="edit_first_name"),
                InlineKeyboardButton(text="Familiya", callback_data="edit_last_name"),
            ],
            [
                InlineKeyboardButton(text="Yosh", callback_data="edit_age"),
                InlineKeyboardButton(text="Jinsi", callback_data="edit_gender"),
            ],
            [
                InlineKeyboardButton(text="Telefon raqami", callback_data="edit_contact")
            ]
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif query.data == "edit_first_name":
        query.message.edit_text("<b>Ismingizni kiriting:</b>", parse_mode="HTML")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 1

    elif query.data == "edit_last_name":
        query.message.edit_text("<b>Familiyangizni kiriting:</b>", parse_mode="HTML")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 2

    elif query.data == "edit_age":
        query.message.edit_text("<b>Yoshingizni kiriting:</b>", parse_mode="HTML")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 3

    elif query.data == "edit_gender":
        buttons = [
            [KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text(text="<b>Jinsingizni tanlang:</b>", parse_mode="HTML",
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
                                                                  one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 4

    elif query.data == "edit_contact":
        buttons = [
            [KeyboardButton(text="<b>Jo'natish</b>", parse_mod="HTML", request_contact=True)]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text(text="<b>Kontaktingizni jo'nating yoki qo'lda tering</b>",
                                 parse_mode="HTML",
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
                                                                  one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 5

    elif query.data == "main_menu":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        main_menu(update, context, query.message.chat_id)


def inline_handler_product(update, context):
    query = update.callback_query
    if query.data == "apple_product":
        buttons = [
            [InlineKeyboardButton(text="iPhone 13 Pro Max", callback_data="iphone_product_13_pro_max"),
             InlineKeyboardButton(text="iPhoone XS", callback_data="iphone_product_xs")],
            [InlineKeyboardButton(text="Asosiy menyu", callback_data="main_menu")]
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "samsung_product":
        buttons = [
            [InlineKeyboardButton(text="Samsung A22", callback_data="samsung_product_a22"),
             InlineKeyboardButton(text="Samsung Galaxy S10", callback_data="samsung_product_galaxy_s10")],
            [InlineKeyboardButton(text="Asosiy menyu", callback_data="main_menu")]
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "iphone_product_13_pro_max":
        query.message.reply_photo(
            photo="https://yandex.uz/images/search?text=iphone%2013%20promax&from=tabbar&pos=2&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FMq9fL3TDc9w%2Fmaxresdefault.jpg&rpt=simage",
            caption="iPhone 13 Pro Max"
        )
        query.message.reply_text(
            text="Korpus: zanglamas po‘lat, Ceramic Shield hamda Gorilla Glass shishasi"
                 "O‘lchamlari: 160.8 x 78.1 x 7.65mm"
                 "Og‘irligi: 240g"
                 "Himoya: IP68 standarti - suv va changdan himoya"
                 "Ranglar: Graphite, Gold, Silver, Sierra Blue"
        )
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    if query.data == "iphone_product_xs":
        query.message.reply_photo(
            photo="https://yandex.uz/images/search?text=iphone%20xs&from=tabbar&pos=3&img_url=https%3A%2F%2Fpochinil.ru%2Fwp-content%2Fuploads%2F2019%2F10%2Faifon-xs-max.png&rpt=simage",
            caption="iPhone XS"
        )
        query.message.reply_text(
            text="Kafolat: 1 oy"
                 "SIM-karta turi va soni: Dual Sim (nano-Sim, dual stand by)"
                 "Operatsion sistema versiyasi: iOS 12"
                 "Anons qilingan sanasi: September, 2018"
                 "Face ID Datchigi: Mavjud"
                 "O‘lchami: O‘lchami"
        )
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    if query.data == "samsung_product_a22":
        query.message.reply_photo(
            photo="https://yandex.uz/images/search?text=samsung%20a22&from=tabbar&pos=6&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEzluhn9VcAAhfAI.jpg&rpt=simage",
            caption="Samsung A22"
        )
        query.message.reply_text(
            text="Xususiyatlari: Fingerprint (side-mounted), accelerometer, gyro, compass, Virtual proximity sensing"
                 "Rangi: Black"
                 "Vazni: 186 g"
                 "SIM-karta turi va soni: Single SIM (Nano-SIM) or Dual SIM (Nano-SIM, dual stand-by)"
                 "O‘lchami: 159.3 x 73.6 x 8.4 mm"
                 "Operatsion sistema versiyasi: Android 11, One UI Core 3.1"
                 "Barmoq izi: Mavjud"
        )
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    if query.data == "samsung_product_galaxy_s10":
        query.message.reply_photo(
            photo="https://yandex.uz/images/search?text=samsung%20s10&from=tabbar&pos=3&img_url=https%3A%2F%2Fsun9-54.userapi.com%2Fimpf%2F7D5RrPe6ul-Gp2nM0VdepkQQPPTdRejCcv2cYQ%2F1F5SXkBeoyw.jpg%3Fsize%3D604x604%26quality%3D96%26sign%3Dc092c90de6c43fa9fec52720797b74d2&rpt=simage",
            caption="Samsung S10"
        )
        query.message.reply_text(
            text="Protsessor tezligi: 2,7 GGs, 2,3 GGs, 1,9 GGs"
                 "O'lchami (asosiy displey): 163.5mm (6.4)"
                 "Texnologiyasi (asosiy displey): Dynamic AMOLED"
        )
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    if query.data == "main_menu":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        main_menu(update, context, query.message.chat_id)
