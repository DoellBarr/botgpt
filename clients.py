from pyrogram import Client
from configs import configs


bot = Client(
    name="openai_bot",
    api_id=configs.api_id,
    api_hash=configs.api_hash,
    bot_token=configs.bot_token,
    in_memory=True
)
