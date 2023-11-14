import telebot
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='en')

TOKEN = "1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Deep Translate Telegram bot! Send me any text you want to translate to English or specify a language code along with the text if you want to translate it to a different language.")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        if " | " in message.text:
            text, language_code = message.text.split(" | ", 1)
            translated_text = translator.translate(text, target=language_code.strip())
        else:
            translated_text = translator.translate(message.text)

        bot.send_message(message.chat.id, f"Translation: {translated_text}")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while translating your text. Please try again.")

bot.polling()
