import os
import json


class ConfigManager:
    def __init__(self, file_name) -> None:
        self.file = os.getcwd() + f"\\{file_name}"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                data = { "chats": [] }
                json.dump(data, f)

    def __get_dict(self) -> dict:
        with open(self.file) as f:
            data = json.load(f)
        return data
    
    def __write_dict(self, data: dict) -> None:
        with open(self.file, "w") as f:
            json.dump(data, f, ensure_ascii=False)

    def get_chats(self) -> list:
        return self.__get_dict()["chats"]
    
    def add_chat(self, id: int) -> None:
        data = self.__get_dict()
        if not id in data["chats"]:
            data["chats"].append(id)
            self.__write_dict(data)
    
    def remove_chat(self, id: int) -> None:
        data = self.__get_dict()
        chats = data["chats"]
        chats.pop(chats.index(id))
        self.__write_dict(data)
    
    def set_system_chat(self, id: int) -> None:
        data = self.__get_dict()
        data.update({"system_chat": id})
        self.__write_dict(data)
    
    def get_system_chat(self) -> int:
        return self.__get_dict().get("system_chat", 0)

class ChatConfig:
    id: int
    sticker: bool
    audio: bool
    photo: bool
    document: bool
    animation: bool
    video: bool
    voice: bool

    def __init__(self, **kwargs) -> None:
        self.__dict__ = {"sticker": True, "audio": True, "photo": True, "document": True, "animation": True, "video": True, "voice": True}
        self.__dict__.update(kwargs)

    def get_allowed(self) -> list[str]:
        return [x for x in self.__dict__ if self.__dict__[x] and isinstance(self.__dict__[x], bool)]

    def update_config(self, **kwargs):
        self.__dict__.update(kwargs)
        return self

    def __repr__(self) -> str:
        return f'Id: {self.id}\nConfig:\n•sticker: {self.sticker},\n•audio: {self.audio},\n•photo: {self.photo},\n•document: {self.document},\n•animation: {self.animation},\n•video: {self.video},\n•voice: {self.voice}'

class ChatsManager:
    def __init__(self) -> None:
        if not os.path.exists(os.path.join(os.getcwd(), "chats")): os.makedirs("chats")
        self.path = os.path.join(os.getcwd(), "chats")

    def __chat_file(self, id: int, mode: str = "r"):
        return open(self.path + f"/{id}.json", mode)

    def add_chat(self, id: int) -> None:
        with self.__chat_file(id, "w") as f:
            json.dump(ChatConfig(id=id).__dict__, f)
    
    def update_chat(self, chat: ChatConfig) -> None:
        with self.__chat_file(chat.id, "w") as f:
            json.dump(chat.__dict__, f)

    def get_chat(self, id: int) -> ChatConfig | None:
        if os.path.isfile(self.path + f"/{id}.json"):
            with self.__chat_file(id) as f:
                return ChatConfig(**json.load(f))
        return None
        