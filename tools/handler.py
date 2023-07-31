from pyrogram import Client, filters

from pyrogram.handlers import MessageHandler, DeletedMessagesHandler

import routers
from tools.filters import chats


class HandlerManager:
    def __init__(self, app: Client) -> None:
        self.app: Client = app
        self.add_handlers()

    def add_handlers(self):

        handlers_default = (
            MessageHandler(routers.Commands.add_chat, (filters.command("add", ["/", "!"]) & filters.outgoing)),
            MessageHandler(routers.Commands.remove_chat, (filters.command("remove", ["/", "!"]) & filters.outgoing & chats)),

            MessageHandler(routers.OnMessage.text_message, (filters.text & chats)),
            MessageHandler(routers.OnMessage.sticker, (filters.sticker & chats)),
            MessageHandler(routers.OnMessage.audio, (filters.audio & chats)),
            MessageHandler(routers.OnMessage.photo, (filters.photo & chats)),
            MessageHandler(routers.OnMessage.doc, (filters.document & chats)),
            MessageHandler(routers.OnMessage.animation, (filters.animation & chats)),
            MessageHandler(routers.OnMessage.video, (filters.video & chats)),
            MessageHandler(routers.OnMessage.voice, (filters.voice & chats)), 

            DeletedMessagesHandler(routers.OnDelete.delete),
            )
        
        self.handlers = [ self.app.add_handler(handler) for handler in handlers_default ]
    
    def remove_handlers(self):
        for handler in self.handlers:
            self.app.remove_handler(*handler)
        self.handlers = []

