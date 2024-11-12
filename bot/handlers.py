from telegram import Update
from telegram.ext import (
    ContextTypes,
)

from api.client import RAGClient
from bot.config import BOT_USERNAME


def handle_response(text: str) -> str:
    lower_case = text.lower()
    rag_client = RAGClient()
    response = rag_client.query(lower_case, 8)
    print(response)
    return response["model_response"]


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}')

    if message_type == "group":
        if BOT_USERNAME in text:
            formatted_text = text.replace(BOT_USERNAME, "").strip()
            print(f"Formatted text: {formatted_text}")
            response = handle_response(formatted_text)
        else:
            return
    else:
        response = handle_response(text)

    print("Bot: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused the error {context.error}")
