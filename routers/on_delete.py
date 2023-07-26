from pyrogram import Client
from pyrogram.types import Message

from history import manager

async def on_delete(client: Client, msg: Message):
    manager.add_deleted_message(msg)