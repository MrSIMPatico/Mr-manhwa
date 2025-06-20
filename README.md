from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes


PALABRAS_PROHIBIDAS = ['puta', 'niños', 'cp', 'puto']

ID_ADMIN = 7204903761

async def monitorear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        mensaje = update.message.text.lower()
        if any(p in mensaje for p in PALABRAS_PROHIBIDAS):
            alerta = f"🚨 Palabra prohibida detectada:\n\n{mensaje}"
            await context.bot.send_message(chat_id=ID_ADMIN, text=alerta)

if __name__ == '__main__':
    app = ApplicationBuilder().token("7687915645:AAHDgKrBJXOoJp3n7QAuheLt-hdInvPMWpQ").build()
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.CHANNEL, monitorear))
    app.run_polling()
