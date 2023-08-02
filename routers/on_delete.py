from pyrogram import Client
from pyrogram.types import Message

from tools import histoty_manager

async def on_delete(client: Client, msgs: Message):
    histoty_manager.add_deleted_messages(msgs)