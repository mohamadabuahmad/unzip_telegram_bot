from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
from pyunpack import Archive
import shutil
from dotenv import load_dotenv
import asyncio

DOWNLOAD_DIR = "downloads"
EXTRACT_DIR = "extracted"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a .zip or .rar file and I'll extract it!")

# Handle incoming files
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    file_name = file.file_name
    file_path = os.path.join(DOWNLOAD_DIR, file_name)

    # Download file
    telegram_file = await context.bot.get_file(file.file_id)
    await telegram_file.download_to_drive(file_path)
    await update.message.reply_text(f"Downloaded {file_name}. Extracting...")

    try:
        Archive(file_path).extractall(EXTRACT_DIR)
        await update.message.reply_text("Extraction completed. Here are the files:")
        for root, _, files in os.walk(EXTRACT_DIR):
            for f in files:
                file_to_send = os.path.join(root, f)
                await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_to_send, 'rb'))
    except Exception as e:
        await update.message.reply_text(f"Extraction failed: {e}")
    finally:
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
        shutil.rmtree(EXTRACT_DIR)
        os.makedirs(EXTRACT_DIR, exist_ok=True)

def main():
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not found in .env")

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()