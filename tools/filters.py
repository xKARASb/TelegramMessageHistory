from pyrogram.types import Message
from pyrogram.filters import create

from tools import chats_manager, config_manager

async def added_chats_filter(_, __, m: Message):
    chat = chats_manager.get_chat(m.chat.id)
    if chat:
        if m.text: return True
        return str(m.media.value).lower() in chat.get_allowed()

async def settings_filter(_, __, m: Message):
    return m.chat.id == config_manager.get_system_chat()

chats = create(added_chats_filter)
system_chat = create(settings_filter)