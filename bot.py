"""import telebot
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='en')

TOKEN = "1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Deep Translate Telegram bot! Send me any text you want to translate and I will do my best to translate it for you.")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        translated_text = translator.translate(message.text)
        bot.send_message(message.chat.id, f"Translation: {translated_text}")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while translating your text. Please try again.")

bot.polling()
"""
import telebot
from telebot import *
from deep_translator import GoogleTranslator
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

translator = GoogleTranslator(source='auto')

TOKEN = "1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU"

bot = telebot.TeleBot(TOKEN)

user_message = ""

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Deep Translate Telegram bot! Send me any text you want to translate and I will do my best to translate it for you.")

@bot.message_handler(func=lambda message: True)
def save_user_message(message):
    global user_message
    user_message = message.text  # Save the user's message to a variable

    # Ask the user to select the target language
    bot.send_message(message.chat.id, "Select the language you want to translate to:", reply_markup=get_language_selection_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ["en", "si"])
def translate_with_selected_language(call):
    global user_message
    # Retrieve the selected target language
    target_language = call.data

    # Translate the user's message to the selected target language
    translated_text = translator.translate(user_message, target=target_language)

    # Send the translated text to the user
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Translation: {translated_text}")

def get_language_selection_keyboard():
    # Create the inline markup keyboard with two buttons
    keyboard = InlineKeyboardMarkup()
    english_button = InlineKeyboardButton(text="English", callback_data="en")
    sinhala_button = InlineKeyboardButton(text="Sinhala", callback_data="si")
    keyboard.add(english_button, sinhala_button)

    return keyboard

bot.polling()  # Start the bot
