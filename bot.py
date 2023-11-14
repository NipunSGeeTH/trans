import telebot

bot = telebot.TeleBot('1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU')

@bot.message_handler(func=lambda message: '|' in message.text)
def handle_message(message):
    split_message = message.text.split('|')
    bot.send_message(message.chat.id, split_message[1])

bot.polling()
