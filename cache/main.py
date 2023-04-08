from pyrogram import Client
from PriyaMusic.config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "PriyaMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="PriyaMusic.handler"),
    )

priyamusic = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(priyamusic,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(esport, overload_quiet_mode=True)

with Client("PriyaMusic", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with priyamusic as app:
    me_priyamusic = app.get_me()
