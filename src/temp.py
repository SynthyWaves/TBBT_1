import telebot
from telebot import types

bot = telebot.TeleBot('ВАШ_ТОКЕН_ЗДЕСЬ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Нажми сюда!')
    markup.add(button)
    bot.send_message(message.chat.id, 'Hello World!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Нажми сюда!':
        bot.send_message(message.chat.id, 'Кнопка была нажата! 🎉')

bot.polling(non_stop=True, interval=0)

import telebot
from telebot import types
bot = telebot.TeleBot('8360152375:AAHRrO2JfJnKolIBQNXZK-FJJZZflYKH-q0')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Нажми сюда!', callback_data='button_pressed')
    markup.add(button)
    bot.send_message(message.chat.id, 'Hello World!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'button_pressed':
        bot.answer_callback_query(call.id, 'Вы нажали на кнопку!')
        bot.send_message(call.message.chat.id, 'Кнопка была нажата! 🎉')

print('Бот запущен...')
bot.polling(none_stop=True)