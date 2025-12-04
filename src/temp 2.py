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