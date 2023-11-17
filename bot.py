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



"""
import telebot
from telebot import *
from deep_translator import GoogleTranslator
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup



TOKEN = "6442898790:AAGPqlo27ohQQG3WNIWoLz3I1361eQkS-1c"

bot = telebot.TeleBot(TOKEN)

user_message = ""

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn_open_website = types.InlineKeyboardButton('Open Website', url='t.me/nipunsgeeth')
    markup.add(btn_open_website)
    bot.send_message(message.chat.id, "Welcome to the Deep Translate Telegram bot! Send me any text you want to translate and I will do my best to translate it for you.",reply_markup=markup)
    
    


@bot.message_handler(func=lambda message: True)
def save_user_message(message):
    global user_message
    user_message = message.text  # Save the user's message to a variable

    # Ask the user to select the target language
    bot.send_message(message.chat.id, "Select the language you want to translate to:", reply_markup=get_language_selection_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ["en", "si","ta","ko","ja","hi"])
def translate_with_selected_language(call):
    global user_message
    # Retrieve the selected target language
    target_language = call.data
    translator = GoogleTranslator(source='auto',  target=target_language)
    # Translate the user's message to the selected target language
    translated_text = translator.translate(user_message)

    # Send the translated text to the user
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Translation: {translated_text}")

def get_language_selection_keyboard():
    # Create the inline markup keyboard with two buttons
    keyboard = InlineKeyboardMarkup()
    english_button = InlineKeyboardButton(text="English", callback_data="en")
    sinhala_button = InlineKeyboardButton(text="Sinhala", callback_data="si")
    tamil_button = InlineKeyboardButton(text="Tamil", callback_data="ta")
    korean_button = InlineKeyboardButton(text="Korean", callback_data="ko")
    japanese_button = InlineKeyboardButton(text="Japanese", callback_data="ja")
    hindi_button = InlineKeyboardButton(text="Hindi", callback_data="hi")
    keyboard.add(english_button, sinhala_button,tamil_button,korean_button,japanese_button,hindi_button)
    return keyboard

bot.polling()  # Start the bot


"""
"""

#all in without mongodb


import telebot
from telebot import *
from deep_translator import GoogleTranslator
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


# Replace with your Telegram bot token
bot_token = "6442898790:AAGPqlo27ohQQG3WNIWoLz3I1361eQkS-1c"

# Replace with the Telegram channel ID
channel_id = -1002123716029


def check_user(user_id):
    # Get the chat member status
    chat_member = bot.get_chat_member(channel_id, user_id)

    # Check if the user is a member
    if chat_member.status == "member":
        return True
    else:
        return False







def get_language_selection_keyboard():
    # Create the inline markup keyboard with two buttons
    keyboard = InlineKeyboardMarkup()
    english_button = InlineKeyboardButton(text="English", callback_data="en")
    sinhala_button = InlineKeyboardButton(text="Sinhala", callback_data="si")
    tamil_button = InlineKeyboardButton(text="Tamil", callback_data="ta")
    korean_button = InlineKeyboardButton(text="Korean", callback_data="ko")
    japanese_button = InlineKeyboardButton(text="Japanese", callback_data="ja")
    hindi_button = InlineKeyboardButton(text="Hindi", callback_data="hi")
    keyboard.add(english_button, sinhala_button, tamil_button, korean_button, japanese_button, hindi_button)
    return keyboard


def send_message(user_id, message):
    # Send the message to the user
    bot.send_message(user_id, message)


# Create a Telegram bot instance
bot = telebot.TeleBot(bot_token)

def join_button():
    markup = types.InlineKeyboardMarkup()
    btn_open_website = types.InlineKeyboardButton('Join Our Main Channel', url='https://t.me/NsDevSpace')
    markup.add(btn_open_website)
    return markup                                              
                                

@bot.message_handler(commands=['start'])
def handle_start(message):
    
    bot.send_photo(message.chat.id, "https://t.me/NsDevSpace/8", caption="Welcome! to Translator Bot Olivia 💚", reply_markup=join_button())
    

    


@bot.message_handler(func=lambda message: True)
def save_user_message(message):
    global user_message
    user_message = message.text  # Save the user's message to a variable
    user_id = message.from_user.id

    if check_user(user_id):
        # Ask the user to select the target language
        bot.send_message(message.chat.id, "Select the language you want to translate to:",
                        reply_markup=get_language_selection_keyboard())

        @bot.callback_query_handler(func=lambda call: call.data in ["en", "si", "ta", "ko", "ja", "hi"])
        def translate_with_selected_language(call):
            global user_message

            # Retrieve the selected target language
            target_language = call.data

            # Create a Google Translator instance with the selected target language
            translator = GoogleTranslator(source='auto', target=target_language)

            # Translate the user's message to the selected target language
            translated_text = translator.translate(user_message)

            # Send the translated text to the user
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Translation: {translated_text}")

    else:
        bot.send_message(user_id, "Please join the channel first.", reply_markup=join_button())
bot.polling()  # Start the bot


"""



import telebot
from telebot import *
from deep_translator import GoogleTranslator
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import MongoClient




MONGODB_URI = 'mongodb+srv://sangeethnipun385:poabZUl7nevXZPQ7@cluster0.jyiupuu.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'Cluster0'
COLLECTION_NAME = 'translatebotusers'

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]




# Replace with your Telegram bot token
bot_token = "6442898790:AAGPqlo27ohQQG3WNIWoLz3I1361eQkS-1c"

# Replace with the Telegram channel ID
channel_id = -1002123716029


def check_user(user_id):
    # Get the chat member status
    chat_member = bot.get_chat_member(channel_id, user_id)

    # Check if the user is a member
    if chat_member.status == "member":
        return True
    else:
        return False







def get_language_selection_keyboard():
    # Create the inline markup keyboard with two buttons
    keyboard = InlineKeyboardMarkup()
    english_button = InlineKeyboardButton(text="English", callback_data="en")
    sinhala_button = InlineKeyboardButton(text="Sinhala", callback_data="si")
    tamil_button = InlineKeyboardButton(text="Tamil", callback_data="ta")
    korean_button = InlineKeyboardButton(text="Korean", callback_data="ko")
    japanese_button = InlineKeyboardButton(text="Japanese", callback_data="ja")
    hindi_button = InlineKeyboardButton(text="Hindi", callback_data="hi")
    keyboard.add(english_button, sinhala_button, tamil_button, korean_button, japanese_button, hindi_button)
    return keyboard


def send_message(user_id, message):
    # Send the message to the user
    bot.send_message(user_id, message)


# Create a Telegram bot instance
bot = telebot.TeleBot(bot_token)

def join_button():
    markup = types.InlineKeyboardMarkup()
    btn_open_website = types.InlineKeyboardButton('Join Our Main Channel', url='https://t.me/NsDevSpace')
    markup.add(btn_open_website)
    return markup                                              
                                

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Save user's ID, username, first name, and last name in the MongoDB database
    user_id = message.chat.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    user_data = {"user_id": user_id, "user_name": user_name, "user_first_name": user_first_name, "user_last_name": user_last_name}
    if not collection.find_one({"user_id": user_id}):
        collection.insert_one(user_data)
    bot.send_photo(message.chat.id, "https://t.me/NsDevSpace/8", caption="Welcome! to Translator Bot Olivia 💚", reply_markup=join_button())
    

    


@bot.message_handler(func=lambda message: True)
def save_user_message(message):
    global user_message
    user_message = message.text  # Save the user's message to a variable
    user_id = message.from_user.id

    if check_user(user_id):
        # Ask the user to select the target language
        bot.send_message(message.chat.id, "Select the language you want to translate to:",
                        reply_markup=get_language_selection_keyboard())

        @bot.callback_query_handler(func=lambda call: call.data in ["en", "si", "ta", "ko", "ja", "hi"])
        def translate_with_selected_language(call):
            global user_message

            # Retrieve the selected target language
            target_language = call.data

            # Create a Google Translator instance with the selected target language
            translator = GoogleTranslator(source='auto', target=target_language)

            # Translate the user's message to the selected target language
            translated_text = translator.translate(user_message)

            # Send the translated text to the user
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Translation: {translated_text}")

    else:
        bot.send_message(user_id, "Please join the channel first.", reply_markup=join_button())
bot.polling()  # Start the bot






