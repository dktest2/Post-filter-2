import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "8321183"))
  API_HASH = os.environ.get("API_HASH", "d9102799310e7038de04d9af2679ed68")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "5928657017:AAHDknS9PQPkxJ_Ua7ks7mLTQgx6U3Uhocg")
  STRINGSESSION = os.environ.get("STRINGSESSION", "1AZWarzgBu4ZJQRIYCkKTKSPLdy3x2YgoVit8hf6zeodZMnkr_z4bvjq-0p4wAW-u3irJaucR_2aT402zWzSpUMVtUHNKcfws_FemmYSxygCL60bLmaZt4t-JkLcZKWJg6gNmHGB0oL9lIsWjQ9EjdU7Ml3_cJVWFbfekyowmBeCDfmX2zPNee2CMPOrnBSVV6KQ6Q8VS-LtR31m15D1eu7AuipHCq7qEf8nnDXCsUj4x2woqSEn1-HUaW_yb5kcCORKvMt47y9k-YvjRT9VEadtFS_UrblmyLFgsolNrPqCjGA8sn6yEyMdizx19ukO16MvQlLuU-SSUsoFvDeu5zvFOtHK3R7A=")
  OWNER_ID = int(os.environ.get("OWNER_ID", "399726799"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001745238544"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://vxagnqmn:gKw_gOqVE39Ys7cPQiPvXygnhg4QTUwS@berry.db.elephantsql.com/vxagnqmn")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 600))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ded_eye")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "links_search_bot")
