from pyrogram import filters
from config import CHAT_ID, SLOT_TOPICS, WIN_VALUES

def init_slot_handlers(app):

    @app.on_message(filters.chat(CHAT_ID) & filters.dice)
    async def slot_handler(client, message):

        if message.message_thread_id not in SLOT_TOPICS:
            return

        dice = message.dice
        if dice.emoji != "🎰":
            return

        print(f"🎰 Результат: {dice.value}")
        print(f"От пользователя: {message.from_user.first_name if message.from_user else 'Нет данных'}")

        if dice.value in WIN_VALUES:
            await message.reply("🎉 ВЫ ВЫИГРАЛИ! Поздравляем!")

            if message.from_user:
                try:
                    await client.send_message(
                        message.from_user.id,
                        "🎁 Поздравляем! Вы выиграли."
                    )
                    print("Личка отправлена")
                except Exception as e:
                    print(f"Не удалось отправить ЛС: {e}")