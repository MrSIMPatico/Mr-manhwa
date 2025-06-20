from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def obtener_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"ID del grupo: `{update.message.chat_id}`", parse_mode='Markdown')

app.add_handler(CommandHandler("id", obtener_id))
