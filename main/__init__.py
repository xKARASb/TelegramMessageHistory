import os

from dotenv import load_dotenv

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, DeletedMessagesHandler 

from main import handlers 


load_dotenv()

api_id = os.getenv("ID")
api_hash = os.getenv("HASH")

app = Client('xkarasb', api_id, api_hash)

#Delete message handlers
app.add_handler(MessageHandler(handlers.on_text_message, filters.text))
app.add_handler(MessageHandler(handlers.on_sticker, filters.sticker))
app.add_handler(MessageHandler(handlers.on_audio, filters.audio))
app.add_handler(MessageHandler(handlers.on_photo, filters.photo))
app.add_handler(MessageHandler(handlers.on_doc, filters.document))
app.add_handler(MessageHandler(handlers.on_animation, filters.animation))
app.add_handler(MessageHandler(handlers.on_video, filters.video))
app.add_handler(MessageHandler(handlers.on_voice, filters.voice))

#Delete message handlers
app.add_handler(DeletedMessagesHandler(handlers.on_delete))

app.run()