import json

from pyrogram import Client
from pyrogram import Client, filters

from pyrogram.handlers import MessageHandler, DeletedMessagesHandler

import routers

class HandlerManager:
    def __init__(self, app: Client) -> None:
        self.app: Client = app
        self.add_handlers()

    def add_handlers(self):
        with open("cfg.json", "r") as f:
            chats = json.load(f)["chats"]


        handlers_default = [
            MessageHandler(routers.Commands.add_chat, (filters.command("add", ["/", "!"]) & filters.outgoing)),
            MessageHandler(routers.Commands.remove_chat, (filters.command("remove", ["/", "!"]) & filters.outgoing)),

            MessageHandler(routers.OnMessage.text_message, (filters.text & filters.chat(chats))),
            MessageHandler(routers.OnMessage.sticker, (filters.sticker & filters.chat(chats))),
            MessageHandler(routers.OnMessage.audio, (filters.audio & filters.chat(chats))),
            MessageHandler(routers.OnMessage.photo, (filters.photo & filters.chat(chats))),
            MessageHandler(routers.OnMessage.doc, (filters.document & filters.chat(chats))),
            MessageHandler(routers.OnMessage.animation, (filters.animation & filters.chat(chats))),
            MessageHandler(routers.OnMessage.video, (filters.video & filters.chat(chats))),
            MessageHandler(routers.OnMessage.voice, (filters.voice & filters.chat(chats))),

            DeletedMessagesHandler(routers.OnDelete.delete, filters.chat(chats))
            ]
        
        self.handlers = [ self.app.add_handler(handler) for handler in handlers_default ]

    
    def remove_handlers(self):
        for handler in self.handlers:
            self.app.remove_handler(*handler)
        self.handlers = []

    def update_handlers(self):
        self.remove_handlers()
        self.add_handlers()