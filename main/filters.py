import json

from pyrogram.types import Message
from pyrogram.filters import create



async def added_chats_filter(_, __, m: Message):  
    with open("cfg.json", "r") as f:
        chats = json.load(f)["chats"]
    return m.chat.id in chats

chats = create(added_chats_filter)