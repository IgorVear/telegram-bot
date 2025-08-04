import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

import os
TOKEN = os.getenv("BOT_TOKEN")  

main_menu = ReplyKeyboardMarkup(
    [['📞 Связь с администратором', 'ℹ️ Информация о канале'], ['🛍 Посмотреть продукцию']],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    await update.message.reply_text(
        f"Привет, {user.first_name}! 🎁\nВот твой бесплатный подарок:\n👉 https://t.me/ТВОЙ_КАНАЛ",
        reply_markup=main_menu
    )

    await asyncio.sleep(600)
    await context.bot.send_message(
        chat_id=chat_id,
        text="🔥 Успей купить наш акционный продукт со скидкой! Переходи по ссылке: https://example.com"
    )

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '📞 Связь с администратором':
        await update.message.reply_text("Связаться с админом можно здесь: @твой_ник")

    elif text == 'ℹ️ Информация о канале':
        await update.message.reply_text("Наш канал — это полезности, акции и бонусы! Подписывайся: https://t.me/ТВОЙ_КАНАЛ")

    elif text == '🛍 Посмотреть продукцию':
        await update.message.reply_text(
            "🛍 Вот что ты можешь приобрести:\n"
    "1. ✅ [Продукт A — 199 грн](https://example.com/productA)\n"
    "2. ✅ [Продукт B — 299 грн](https://example.com/productB)\n"
    "3. ✅ [Продукт C — 399 грн](https://example.com/productC)"
            "(Подробности скоро появятся!)"
        ) 
 
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_menu))
app.run_polling()

