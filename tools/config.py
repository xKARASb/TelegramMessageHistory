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