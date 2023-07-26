import json

from pyrogram import Client
from pyrogram.types import Message

async def add_chat(client: Client, msg: Message):
    await client.delete_messages(msg.chat.id, msg.id)
    with open("cfg.json") as f:
        data = json.load(f)
    data["chats"].append(msg.chat.id)
    with open("cfg.json", "w") as f:
        json.dump(data, f)
    client.handler_manager.update_handlers()

async def remove_chat(client: Client, msg: Message):
    await client.delete_messages(msg.chat.id, msg.id)
    with open("cfg.json") as f:
        data = json.load(f)
    data["chats"].pop(data["chats"].index(msg.chat.id))
    with open("cfg.json", "w") as f:
        json.dump(data, f)
    client.handler_manager.update_handlers()