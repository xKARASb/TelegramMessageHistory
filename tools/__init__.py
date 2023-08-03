import os
from dotenv import load_dotenv

from tools.history import HisotryManager
from tools.system import ConfigManager, ChatsManager

load_dotenv()

histoty_manager = HisotryManager(os.getenv("HISTORY_FILE_NAME"))
config_manager = ConfigManager(os.getenv("CONFIG_FILE_NAME"))
chats_manager = ChatsManager()