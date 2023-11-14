import telebot
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto')

TOKEN = "1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU"

bot = telebot.TeleBot(TOKEN)

def generate_language_selection_markup():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('English'))
    markup.add(telebot.types.KeyboardButton('Sinhala'))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Deep Translate Telegram bot! Please select your preferred translation language:", reply_markup=generate_language_selection_markup())

@bot.message_handler(func=lambda message: True)
def handle_language_selection(message):
    selected_language = message.text.lower()

    if selected_language == 'English':
        target_language = 'en'
    elif selected_language == 'Sinhala':
        target_language = 'si'
    else:
        bot.send_message(message.chat.id, "Invalid language selection. Please choose either 'English' or 'Sinhala'.")
        return

    # Set the target language for future translations
    translator.target = target_language

    bot.send_message(message.chat.id, f"Your preferred translation language has been set to {target_language}. Send me any text you want to translate and I will do my best to translate it for you.")

    # Reset the keyboard to default
    bot.send_message(message.chat.id, "Please select your preferred translation language:", reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        translated_text = translator.translate(message.text)
        bot.send_message(message.chat.id, f"Translation: {translated_text}")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while translating your text. Please try again.")

bot.polling()
