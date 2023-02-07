import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "8321183"))
  API_HASH = os.environ.get("API_HASH", "d9102799310e7038de04d9af2679ed68")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "5928657017:AAHDknS9PQPkxJ_Ua7ks7mLTQgx6U3Uhocg")
  STRINGSESSION = os.environ.get("STRINGSESSION", "1BVtsOKkBuzRaySMz6D7Gw1XU11O1KjfolOKV-IfR1Dzv2BCvy8cg6ij8EqCQrqY6Ca-anKa3y7whE3QawRgq12E5829iJe7pFYvLkvctD406IsPT-vUIQFptH_z7pceYHLJo_INF_-ZQ05qQfTxytag7ytx-9TBVpLOXwHLR-4USppowQOOoT_781CQEH_ZlYIR40JVQq44Nq9uhs540Teitl9I5BcrFvxvbhlgE_G15TxGdX2g9KGLsgcny9kkHzMnXZelcN12occ3m7ty7Zc66_-bz2fiM60u_P3C-pLqwSaDTX44shCjawcwOb0vMrd-zxffpyBshEiMioRLcMVDkKaHp6M4=")
  OWNER_ID = int(os.environ.get("OWNER_ID", "399726799"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001896983424"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://vxagnqmn:gKw_gOqVE39Ys7cPQiPvXygnhg4QTUwS@berry.db.elephantsql.com/vxagnqmn")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 600))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ded_eye")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "links_search_bot")
