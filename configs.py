from dotenv import load_dotenv
import os


class Configs:
    def __init__(self):
        load_dotenv()
        self.api_id = os.getenv("API_ID")
        self.api_hash = os.getenv("API_HASH")
        self.bot_token = os.getenv("BOT_TOKEN")
        self.openai_apikey = os.getenv("OPENAI_APIKEY")


configs = Configs()
