import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

CHAT_ID = int(os.getenv("CHAT_ID"))

topics_raw = os.getenv("SLOT_TOPICS", "")
SLOT_TOPICS = {int(t.strip()) for t in topics_raw.split(",") if t.strip()}

WIN_VALUES = {64, 43, 22, 1}