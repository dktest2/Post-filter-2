import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "8321183"))
  API_HASH = os.environ.get("API_HASH", "d9102799310e7038de04d9af2679ed68")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "5928657017:AAHDknS9PQPkxJ_Ua7ks7mLTQgx6U3Uhocg")
  STRINGSESSION = os.environ.get("STRINGSESSION", "1BVtsOLwBuyARpm69kZG2xCZCr2MDJHewD1G1V62hXN8i-MyVTShm_upu5Q_LMZi8f8cHWYLtPWhHR2e6bkP80RyBkIsYHMjqaUOegvLqxjSHu36NGlFubmcLNzxURkOQnih0aNXLJhXNCdBqSOLpoKtfUoTWIdCKJpzpZ_VMdLr9RD5izBFu0D8YUSddVKeD2_Z1HGr_BRj-PntgpDWKZeU62-iMjVqZTIP0IoVHucSmzbx6jZFgqQu05yZi201bw6Cinoszynd1Ez8c7p6IrKOSoM5-27nUzi6XhtFDcpfxxIq_Nxc-fEw-LqLJtB3C7L9Vdi1mQTAcEEs5W-T3LPj97OXwTF4=")
  OWNER_ID = int(os.environ.get("OWNER_ID", "399726799"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001896983424"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://vxagnqmn:gKw_gOqVE39Ys7cPQiPvXygnhg4QTUwS@berry.db.elephantsql.com/vxagnqmn")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 600))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ded_eye")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "links_search_bot")
