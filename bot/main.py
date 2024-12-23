from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from bot.config import HELP_MESSAGE, INITIAL_MESSAGE, TOKEN
from bot.handlers import error, handle_message


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(INITIAL_MESSAGE)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_MESSAGE)


if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("ayuda", help_command))

    # Mensajes
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errores
    app.add_error_handler(error)

    # Revisa cada 5 segundos por mensajes nuevos
    print("Polling...")
    app.run_polling(poll_interval=5)
