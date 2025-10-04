from telebot import types

def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Отправить номер телефона📞", request_contact=True)
    kb.add(btn)
    return kb

