from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext

def kick(update: Update, context: CallbackContext) -> None:
    if context.bot.get_chat_member(update.message.chat_id, update.message.from_user.id).status in ['administrator', 'creator']:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.kick_chat_member(update.message.chat_id, user_id)
    else:
        update.message.reply_text("You are not allowed to use this command.")

# Register /kick command handler
kick_handler = CommandHandler('kick', kick)
dispatcher.add_handler(kick_handler)
