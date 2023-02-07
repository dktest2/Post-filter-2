import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "8321183"))
  API_HASH = os.environ.get("API_HASH", "d9102799310e7038de04d9af2679ed68")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "5928657017:AAHDknS9PQPkxJ_Ua7ks7mLTQgx6U3Uhocg")
  STRINGSESSION = os.environ.get("STRINGSESSION", "1BVtsOK4BuxRmEEyDH8mU6jcIMONqWZIN7O3Z0IGO0oEgy1toJYF3PxjlhMRu-JfQBI4Ga6vccLvOmndQug2SmjP_nBb3sJ4sZcX8eteHP0QMkxYgKYknB7iuuS4ipJfz0uM0bWz60Go-clRTOaJfWRxwpvBWmHRfeIEsarvyfZtRQQmK9URdG9RX85PKf7rNFbdkoBuStgLljv2TNOJo_40rxT69UaydiiDtGDoHUrgKOQGRcnlJXL7IR27_mGMnIsCNbRxoFAG__k1Run8Qg1ONFDJCspyd4dlZG1FMCSrJc6EE3ZfjdJxT4HanW9eALlXG240UdAV8wJLQXgpCCyDj_Mynv34=")
  OWNER_ID = int(os.environ.get("OWNER_ID", "399726799"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001896983424"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://vxagnqmn:gKw_gOqVE39Ys7cPQiPvXygnhg4QTUwS@berry.db.elephantsql.com/vxagnqmn")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 600))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ded_eye")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "links_search_bot")
