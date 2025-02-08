


import telebot
from telebot import *
from deep_translator import GoogleTranslator
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import MongoClient




MONGODB_URI = 'your mongodb uri'
DATABASE_NAME = 'Your database name '
COLLECTION_NAME = 'translatebotusers'

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]




# Replace with your Telegram bot token
bot_token = "I1361eQkS-1c"

# Replace with the Telegram channel ID
channel_id = -10


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
    bot.send_photo(message.chat.id, "https://t.me/NsDevSpace/8", caption="Welcome! \nTranslator Bot 💝 Aurora 💖 \n\nSend the part you want to translate as text 💚\n\n 🇱🇰", reply_markup=join_button())
    

    


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
        bot.send_message(user_id, "Please join the channel first ✅.\n\nමුලින්ම මේ චැනල් එකට ජොයින් වෙන්න, \nඊට පස්සෙ Translate කරන්න ඕන Text  එක එවන්න 😊 ", reply_markup=join_button())
bot.polling()  # Start the bot






