import os
import json

from pyrogram import Client
from pyrogram.types import Message

from history import manager

#GETTING MESSAGE
async def on_text_message(client, msg: Message):
    manager.add_text_message(msg.chat, msg)

async def on_sticker(client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    extend = msg.sticker.file_name.split(".")[1]
    await client.download_media(msg, f"../static/stickers/{msg.sticker.file_unique_id}.{extend}")

async def on_audio(client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    await client.download_media(msg, f"../static/audios/{msg.audio.file_name}")
    

async def on_photo(client: Client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    await client.download_media(msg, f"../static/photos/{msg.photo.file_unique_id}.png")

async def on_doc(client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    await client.download_media(msg, f"../static/docs/{msg.document.file_name}")
    
async def on_animation(client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    await client.download_media(msg, f"../static/animations/{msg.animation.file_name}")
    
async def on_video(client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    await client.download_media(msg, f"../static/videos/{msg.video.file_name}")

async def on_voice(client, msg: Message):
    manager.add_text_message(msg.chat, msg)
    await client.download_media(msg, f"../static/voices/{msg.voice.file_unique_id}.ogg")

#ON EDIT MESSAGES
async def on_edit(client, msg: Message):
    pass

#ON DELET MESSAGES
async def on_delete(client, msg: Message):
    manager.add_deleted_message(msg)