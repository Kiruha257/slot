from pyrogram import filters

def init_commands(app):

    @app.on_message(filters.me & filters.command("start"))
    async def start_command(client, message):
        await message.reply("Слот-бот активен 🎰")

    @app.on_message(filters.me & filters.command("getid"))
    async def getid(client, message):
        await message.reply(f"Chat ID: {message.chat.id}")

    @app.on_message(filters.me & filters.command("thread"))
    async def thread_info(client, message):
        await message.reply(f"ID текущей темы: `{message.message_thread_id}`")

    @app.on_message(filters.me & filters.command("info"))
    async def info(client, message):
        await message.reply(
            f"**Информация о чате:**\n"
            f"Название: {message.chat.title}\n"
            f"ID: `{message.chat.id}`\n"
            f"Тип: {message.chat.type}"
        )