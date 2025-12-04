import telebot
from telebot import types
bot = telebot.TeleBot('8360152375:AAHRrO2JfJnKolIBQNXZK-FJJZZflYKH-q0')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Нажми сюда', callback_data='Button_1')
    markup.add(button)
    bot.send_message(message.chat.id, 'Hello World!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'Button_1')
def handle_first_click(call):
    bot.answer_callback_query(call.id, 'Отлично!')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('А теперь сюда!')
    markup.add(button)
    bot.send_message(call.message.chat.id, 'Теперь нажми кнопку в меню!', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'А теперь сюда!')
def handle_second_click(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Спасибо', callback_data='Button_2')
    markup.add(button)
    bot.send_message(message.chat.id, 'Молодец!', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data == 'Button_2')
    def handle_thanks(call):
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Ну все, хорош...')

print('Бот запущен...')
bot.polling(none_stop=True)
