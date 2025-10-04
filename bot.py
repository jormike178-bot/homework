import telebot
import buttons
import db
from tgHw.dz17.db import register

bot = telebot.TeleBot('7587537078:AAH3JxwjB5rKFp3Oe5WIyqkkyoTReXnEnt4')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.text
    if db.check_user(user_id):
        bot.send_message(user_id, f'Добро пожаловать, {user_name}!',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Привет, как тебя зовут?',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, f'Приятно познакомиться, {user_name}!\nОтправьте свой номер телефона📞:',
                     reply_markup=buttons.num_button())
    bot.register_next_step_handler(message, get_num, user_name)

def get_num(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, 'Вы зарегистрированы!', register(user_id, user_name, phone_number))
        start(message)
    else:
        bot.send_message(user_id, 'Пожалуйста, используйте кнопку для отправки номера')
        bot.register_next_step_handler(message, get_num, user_name)

bot.polling(non_stop=True)