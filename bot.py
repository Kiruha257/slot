from pyrogram import Client
from config import API_ID, API_HASH
from handlers.slot import init_slot_handlers
from handlers.commands import init_commands

app = Client("slot_session", api_id=API_ID, api_hash=API_HASH)

# регистрируем обработчики
init_slot_handlers(app)
init_commands(app)

if __name__ == "__main__":
    print("Бот запущен…")
    app.run()