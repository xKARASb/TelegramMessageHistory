from pyrogram.types import Message
from pyrogram.filters import create

from tools import config_manager

async def added_chats_filter(_, __, m: Message):
    return m.chat.id in config_manager.get_chats()

chats = create(added_chats_filter)