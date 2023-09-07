import os
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters, ContextTypes, ApplicationBuilder
from telegram import Update

from misc import TELEGRAMM_URL, TELEGRAM_TOKEN

TOKEN = TELEGRAM_TOKEN

com = "screenfetch"
com = "ls -la"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, ...")

async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = os.popen(com).read()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=data)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("start", start)
    get_handler = CommandHandler("get", get_command)

    app.add_handler(start_handler)
    app.add_handler(get_handler)

    app.run_polling()
