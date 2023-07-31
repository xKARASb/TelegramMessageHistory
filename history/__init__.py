import os

from history.history import HisotryManager

manager = HisotryManager(os.getenv("HISTORY_FILE_NAME"))