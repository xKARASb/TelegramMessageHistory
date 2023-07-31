from pyrogram import Client
from pyrogram.types import Message

from tools import histoty_manager

async def on_delete(client: Client, msg: Message):
    print(msg)

    #FIX IT
    histoty_manager.add_deleted_message(msg)