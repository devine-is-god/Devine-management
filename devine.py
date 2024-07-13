import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler
from pytube import YouTube
from config import TOKEN  # Import the bot token from config.py

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to start the bot and respond to /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your bot.')

# Function to handle /help command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help command: List of available commands and how to use them.')

# Function to handle unknown commands
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sorry, I didn't understand that command.")

# Function to download a YouTube video
def download(update: Update, context: CallbackContext) -> None:
    url = update.message.text.split(" ", 1)[1]
    path = "/path/to/download"  # Change this to your desired path
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(path)
        update.message.reply_text(f"Downloaded: {yt.title}")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")

# Function to echo messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Function to handle inline queries
def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id='1', 
            title='Inline Result 1', 
            input_message_content=InputTextMessageContent('Hello, this is inline result 1!')
        ),
        InlineQueryResultArticle(
            id='2', 
            title='Inline Result 2', 
            input_message_content=InputTextMessageContent('Hey, here is inline result 2!')
        )
    ]
    update.inline_query.answer(results)

# Main function to run the bot
def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("download", download))  # Add the download handler

    # Register unknown command handler
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Register message handler (echo all messages)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Register inline query handler
    dispatcher.add_handler(InlineQueryHandler(inline_query))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
