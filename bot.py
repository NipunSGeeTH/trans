import telebot
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto')
supported_languages = ['en', 'si', 'fr', 'de', 'it', 'ja', 'pt', 'ru', 'zh-cn']

TOKEN = "1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Deep Translate Telegram bot! Send me any text you want to translate. You can also change the target language using the /language command.")

@bot.message_handler(commands=['language'])
def language(message):
    bot.send_message(message.chat.id, "Available target languages: " + ", ".join(supported_languages))

@bot.message_handler(func=lambda message: True)
def translate(message):
    if message.text.startswith('/language'):
        return

    try:
        # Get the user's target language
        target_language = translator.detect(message.text)
        if target_language not in supported_languages:
            target_language = 'en'

        # Translate the message
        translated_text = translator.translate(message.text, target_language=target_language)
        bot.send_message(message.chat.id, f"Translation ({target_language}): {translated_text}")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while translating your text. Please try again.")

bot.polling()
