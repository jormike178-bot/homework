import telebot

bot = telebot.TeleBot('8294305929:AAHd8_K15fV33u6E2klTJsjSXJHgCQ0fu1w')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'привет')


@bot.message_handler(commands=['help!'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Помогите')

bot.polling(none_stop=True)