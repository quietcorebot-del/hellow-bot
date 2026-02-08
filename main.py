import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def reply_hellow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only respond when a real message text exists
    if update.message and update.message.text:
        await update.message.reply_text("hellow!")

def main():
    if not TOKEN:
        raise ValueError("Missing BOT_TOKEN environment variable")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_hellow))
    app.run_polling()

if __name__ == "__main__":
    main()
