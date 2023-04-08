import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("Internal"):
    load_dotenv("Internal")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "ᴘʀɪʏᴀ ᴍᴜsɪᴄ")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "ᴘʀɪʏᴀ ᴍᴜsɪᴄ")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "PriyaUpdates")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "PriyaUpdates")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5509475839").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/a855ceaa3910d17a3174a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
IMG = getenv("IMG", "https://telegra.ph//file/a855ceaa3910d17a3174a.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph//file/a855ceaa3910d17a3174a.jpg")
