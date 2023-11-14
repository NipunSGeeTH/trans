from pyrogram import Client, filters
from googletrans import Translator

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_KEY = '1879931223:AAGhQi-yFWyrK9JOT3pRAtwlR8adrxGLmVU'
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=API_KEY)

@app.on_message(filters.private & filters.text)
def translate_text(client, message):
    translator = Translator()
    text = message.text

    # Detect the language of the input text
    detected_language = translator.detect(text).lang

    # Translate the text to English
    translated_text = translator.translate(text, dest='en').text

    # Reply with the translation
    message.reply_text(f"Detected Language: {detected_language}\nTranslated: {translated_text}")

if __name__ == "__main__":
    app.run()
