import os
import json
import logging

from pyrogram.types import Message, Chat


class HisotryManager:
    def __init__(self, file_name) -> None:
        self.file = os.getcwd() + f"\\{file_name}"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                data = { "messages": [], "history": {}, "deleted": [] }
                json.dump(data, f)
    
    def __get_dict(self) -> dict:
        with open(self.file) as f:
            data = json.load(f)
        return data
    
    def __write_dict(self, data: dict) -> None:
        with open(self.file, "w") as f:
            json.dump(data, f, ensure_ascii=False)
        return
    
    def __get_chat(self, chat: Chat) -> dict:
        with open(self.file) as f:
            data = json.load(f)["history"]
        title = chat.title if chat.title else f"{chat.first_name} {chat.last_name}"
        data[str(chat.id)] =\
            data.get(str(chat.id), {"title": title, "messages": {}})
        return data[str(chat.id)]

    def __write_chat(self, chat, data: dict) -> None:
        all_data = self.__get_dict()

        data["title"] = chat.title if chat.title else f"{chat.first_name} {chat.last_name}"
        all_data["history"][str(chat.id)] = data
        with open(self.file, "w") as f:
            json.dump(all_data, f, ensure_ascii=False)

    def add_message(self, msg: Message) -> None:
        data = self.__get_dict()
        data["messages"].append(msg.id)
        self.__write_dict(data)

        chat_data = self.__get_chat(msg.chat)
        chat_data["messages"].update({msg.id: json.loads(msg.__str__())})
        self.__write_chat(chat=msg.chat, data=chat_data)
    
    def add_edited_message(self, msg: Message) -> None:
        data = self.__get_chat(msg.chat)
        data["messages"][str(msg.id)]["edited"] = data["messages"][str(msg.id)].get("edited", [])
        data["messages"][str(msg.id)]["edited"].append(json.loads(msg.__str__())) 
        self.__write_chat(chat=msg.chat, data=data)
    
    def add_deleted_messages(self, msgs: list[Message]):
        data = self.__get_dict()
        for msg in msgs:
            if msg.id in data["messages"]:
                data["deleted"].append(msg.id)
        self.__write_dict(data)
    
    def get_deleted_messages(self) -> list[Message]:
        return self.__get_dict()["deleted"]
    