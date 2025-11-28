import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота от @BotFather
bot = telebot.TeleBot('8360152375:AAHRrO2JfJnKolIBQNXZK-FJJZZflYKH-q0')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('Подсказка')
    button2 = types.KeyboardButton('Создать плейлист')
    button3 = types.KeyboardButton('Найти плейлист')

    # Первый ряд - две кнопки
    markup.row(button2, button3)
    # Второй ряд - одна кнопка
    markup.row(button1)

    bot.send_message(
        message.chat.id,
        'Привет! Добро пожаловать в TBBT, нажми "Подсказка" чтобы научиться пользоваться ботом!',
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == 'Подсказка')
def help_message(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Правила', callback_data='rules')
    btn2 = types.InlineKeyboardButton('Создание плейлиста', callback_data='create_help')
    btn3 = types.InlineKeyboardButton('Добавление треков', callback_data='add_tracks')
    btn4 = types.InlineKeyboardButton('Жанры', callback_data='genres')
    btn5 = types.InlineKeyboardButton('Система оценивания', callback_data='rating')
    btn6 = types.InlineKeyboardButton('Коментарии (soon)', callback_data='comments')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)

    bot.send_message(
        message.chat.id,
        'Выбери раздел, о котором ты хочешь узнать:',
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'rules':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, '📋 **Правила:**\n\nЗдесь будут правила использования бота...',
                         parse_mode='Markdown')

    elif call.data == 'create_help':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, '🎵 **Создание плейлиста:**\n\nИнструкция по созданию плейлиста...',
                         parse_mode='Markdown')

    elif call.data == 'add_tracks':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, '➕ **Добавление треков:**\n\nКак добавлять треки в плейлист...',
                         parse_mode='Markdown')

    elif call.data == 'genres':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, '🎸 **Жанры:**\n\nИнформация о доступных жанрах музыки...',
                         parse_mode='Markdown')

    elif call.data == 'rating':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, '⭐ **Система оценивания:**\n\nОписание системы оценок...',
                         parse_mode='Markdown')

    elif call.data == 'comments':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, '💬 **Комментарии:**\n\nЭта функция скоро появится!',
                         parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == 'Создать плейлист')
def create_playlist(message):
    bot.send_message(
        message.chat.id,
        'Создание плейлиста...\nЗдесь будет функционал создания плейлиста!'
    )


@bot.message_handler(func=lambda message: message.text == 'Найти плейлист')
def find_playlist(message):
    bot.send_message(
        message.chat.id,
        'Поиск плейлиста...\nЗдесь будет функционал поиска плейлиста!'
    )

# Запуск бота
print('Бот запущен...')
bot.polling(none_stop=True)
