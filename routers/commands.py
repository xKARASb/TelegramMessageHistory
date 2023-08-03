from ast import literal_eval

from pyrogram import Client
from pyrogram.types import Message

from tools import config_manager, chats_manager


async def add_chat(client: Client, msg: Message):
    await client.delete_messages(msg.chat.id, msg.id)
    config_manager.add_chat(msg.chat.id)
    chats_manager.add_chat(msg.chat.id)

async def remove_chat(client: Client, msg: Message):
    await client.delete_messages(msg.chat.id, msg.id)
    config_manager.remove_chat(msg.chat.id)

async def set_system_chat(client: Client, msg: Message):
    await msg.reply("This chat set as system chat!")
    await client.delete_messages(msg.chat.id, msg.id)
    config_manager.set_system_chat(msg.chat.id)

async def get_chats(client: Client, msg: Message):
    chats = []
    for x in config_manager.get_chats():
        chat = await client.get_chat(x)
        chats.append(f"{chat.title if chat.title else f'{chat.first_name} {chat.last_name}'}: `{chat.id}`")
    await msg.reply("Chats:\n•" + "\n•".join(chats))

async def get_chat(client: Client, msg: Message):
    chat = chats_manager.get_chat(msg.text.split()[1])
    await msg.reply(f"chat cfg:\n `{chat}`")

async def change_settings(client: Client, msg: Message):
    command, id, *changes = msg.text.split("\\ ")
    data = {}
    for x in changes:
        data.update({literal_eval(x)[0]: literal_eval(x)[1]})
    chats_manager.update_chat(chats_manager.get_chat(int(id)).update_config(**data))
    await msg.reply(f"Current config:\n`{chats_manager.get_chat(int(id))}`")