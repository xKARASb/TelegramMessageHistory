import logging
import os

from dotenv import load_dotenv

from pyrogram import Client

from tools.handler import HandlerManager

load_dotenv()

logging.basicConfig(level=logging.INFO, filename="app.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

api_id = os.getenv("ID")
api_hash = os.getenv("HASH")

app = Client('xkarasb', api_id, api_hash)
app.handler_manager = HandlerManager(app)

app.run()