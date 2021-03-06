from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from session_manager import SessionManager
from io import BytesIO
import os
import assistant
import voice

import logging

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger('TelegramBot')

URL_HEROKU_TELEGRAM = os.environ.get('BOT_TELEGRAM_HEROKU_URL')
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    assistant.validate_session(update.effective_chat.id)
    response_text = assistant.send_message(SessionManager.getInstance().getSession(update.effective_chat.id), '')
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

def message(update, context):
    assistant.validate_session(update.effective_chat.id)

    response_text = assistant.send_message(SessionManager.getInstance().getSession(update.effective_chat.id), update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

def receive_voice(update, context):
    assistant.validate_session(update.effective_chat.id)

    audio_file = BytesIO(update.message.voice.get_file().download_as_bytearray())
    text = voice.convert_voice(audio_file)
    response_text = assistant.send_message(SessionManager.getInstance().getSession(update.effective_chat.id), text)
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=voice.convert_text(response_text))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text, message)
dispatcher.add_handler(message_handler)

voice_handler = MessageHandler(Filters.voice, receive_voice)
dispatcher.add_handler(voice_handler)

# updater.start_polling()

updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)

updater.bot.setWebhook(URL_HEROKU_TELEGRAM + TOKEN)

updater.idle()