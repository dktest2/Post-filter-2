import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28685915"))
  API_HASH = os.environ.get("API_HASH", "f9ae4c2b687c9cc726338af37b11af88")
  BOT_TOKEN = os.getenv("BOT_TOKEN", "5811468754:AAGbEH9638DOLJSG0o50fVlSJUYfsWcSIjA")
  STRINGSESSION = os.environ.get("STRINGSESSION","1BVtsOMUBuwc2pKUl2ybdzcIFvFmqsmsjkPjKpLaeNYTlxcKp-3OKY6mniXmDxWnbTimpB9wp6LjTfrlfl2yz95TRyLfRCKcDvKz1wcKrklbwmOn48X1TlkA7pdd7bgTaV5fd6dKnQh050-BdqD1qmjeizmWnZZW_ydAJt-VbGROTNyxLXH3xr-lWomkN0KYvpcBT1jj2AymtgfcjpekofQ9KbNODN1fiC_V-IWMN6y6LikP4UWsckxNRAXOn-l_Po1HbrtEtW10J8rIFn-R1UlIi7Aaplpo0ZGekCLplEbncqIvRe_pbJ60qpKMmkC1IEQ_yJwRAvqY_YgYMJMgof8MbHuY8rf8=")
  OWNER_ID = int(os.environ.get("OWNER_ID", "5492208921"))
  DATABASE_CHANNELS = os.environ.get("DATABASE_CHANNELS", ["-1001769986368"])
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://iioysmdb:TQGx_Y24RYLN7KpjRRuQS0eyyHIK6VIy@mel.db.elephantsql.com/iioysmdb")
  DELETE_DELAY = int(os.environ.get("DELETE_DELAY", 120))
  SUBSCRIPTION_TIME = int(os.getenv("SUBSCRIPTION_TIME", "31"))
  FORCESUB_CHANNEL = os.getenv("FORCESUB_CHANNEL", -100)
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ask_admin001")
