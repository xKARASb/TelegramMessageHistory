import os

from tools.history import HisotryManager
from tools.config import ConfigManager

histoty_manager = HisotryManager(os.getenv("HISTORY_FILE_NAME"))
config_manager = ConfigManager(os.getenv("CONFIG_FILE_NAME"))
