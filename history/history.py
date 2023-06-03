from pyrogram.types import User, Message, Chat

import json

class HisotryManager:
    def __init__(self, file_name) -> None:
        self.file = file_name
    
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
        return

    def add_text_message(self, chat: Chat, msg: Message) -> None:
        all_data = self.__get_dict()
        all_data["messages"].append(msg.id)
        self.__write_dict(all_data)

        chat_data = self.__get_chat(chat)
        chat_data["messages"].update({msg.id: json.loads(msg.__str__())})
        self.__write_chat(chat=chat, data=chat_data)
    
    def add_deleted_message(self, msg: Message):
        all_data = self.__get_dict()
        all_data["deleted"].append(msg.id)
        self.__write_dict(all_data)
        