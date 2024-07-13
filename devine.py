import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube
from config import TOKEN  # Import the bot token from config.py

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Command handler functions
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your bot. Send /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - List available commands\n/download <URL> - Download a YouTube video')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def download(update: Update, context: CallbackContext) -> None:
    try:
        url = update.message.text.split(" ", 1)[1]
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        update.message.reply_text(f"Downloaded: {yt.title}")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")

# Main function to run the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("download", download))

    # Register message handler (echo all messages)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
