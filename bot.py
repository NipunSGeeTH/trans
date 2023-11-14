import telebot
from googletrans import Translator

translator = Translator()

TOKEN = "1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Google Translate Telegram bot! Send me any text you want to translate and I will do my best to translate it for you.")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        source_language = message.chat.language_code
        translated_text = translator.translate(message.text, dest="en").text
        bot.send_message(message.chat.id, f"Translation from {source_language} to English: {translated_text}")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while translating your text. Please try again.")

bot.polling()
