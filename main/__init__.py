import json
import os

from dotenv import load_dotenv

from pyrogram import Client

from main.handler import HandlerManager


load_dotenv()

api_id = os.getenv("ID")
api_hash = os.getenv("HASH")
history_file_name = os.getenv("HISTORY_FILE_NAME")

if not os.path.exists(os.getcwd() + f"\\{history_file_name}"):
    with open(history_file_name, "w") as f:
        data = { "messages": [], "history": {}, "deleted": [] }
        json.dump(data, f)

if not os.path.exists(os.getcwd() + f"\\cfg.json"):
    with open("cfg.json", "w") as f:
        data = { "chats": [] }
        json.dump(data, f)

app = Client('xkarasb', api_id, api_hash)
app.handler_manager = HandlerManager(app)

app.run()