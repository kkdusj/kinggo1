import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 10871792))

    API_HASH = os.environ.get("API_HASH", "6f3f84d0b392900e09b0aed186470890")
