from pyrogram import Client
from pyrogram.types import Message

from tools import histoty_manager

async def on_edit(client: Client, msg: Message):
    histoty_manager.add_edited_message(msg)
