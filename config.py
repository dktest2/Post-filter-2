import os

class Config(object):
  API_ID = int(os.environ.get("API_ID"))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.getenv("BOT_TOKEN")
  STRINGSESSION = os.environ.get("STRINGSESSION")
  OWNER_ID = int(os.environ.get("OWNER_ID"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001769986368"])
  DATABASE_URL = os.environ.get("DATABASE_URL")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 120))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
  BOT_USERNAME = os.environ.get("BOT_USERNAME")