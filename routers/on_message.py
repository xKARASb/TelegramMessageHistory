import os

from pyrogram import Client
from pyrogram.types import Message

from tools import histoty_manager

path = os.path.join(os.getcwd(), "static")

async def on_text_message(client, msg: Message):
    histoty_manager.add_message(msg)

async def on_sticker(client, msg: Message):
    histoty_manager.add_message(msg)
    extend = msg.sticker.file_name.split(".")[1]
    await client.download_media(msg, f"{path}/stickers/{msg.sticker.file_unique_id}.{extend}")

async def on_audio(client, msg: Message):
    histoty_manager.add_message(msg)
    await client.download_media(msg, f"{path}/audios/{msg.audio.file_name}")
    

async def on_photo(client: Client, msg: Message):
    histoty_manager.add_message(msg)
    await client.download_media(msg, f"{path}/photos/{msg.photo.file_unique_id}.png")

async def on_doc(client, msg: Message):
    histoty_manager.add_message(msg)
    await client.download_media(msg, f"{path}/docs/{msg.document.file_name}")
    
async def on_animation(client, msg: Message):
    histoty_manager.add_message(msg)
    await client.download_media(msg, f"{path}/animations/{msg.animation.file_name}")
    
async def on_video(client, msg: Message):
    histoty_manager.add_message(msg)
    await client.download_media(msg, f"{path}/videos/{msg.video.file_name}")

async def on_voice(client, msg: Message):
    histoty_manager.add_message(msg)
    await client.download_media(msg, f"{path}/voices/{msg.voice.file_unique_id}.ogg")
