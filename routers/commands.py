from pyrogram import Client
from pyrogram.types import Message

from tools import config_manager

async def add_chat(client: Client, msg: Message):
    await client.delete_messages(msg.chat.id, msg.id)
    config_manager.add_chat(msg.chat.id)

async def remove_chat(client: Client, msg: Message):
    await client.delete_messages(msg.chat.id, msg.id)
    config_manager.remove_chat(msg.chat.id)