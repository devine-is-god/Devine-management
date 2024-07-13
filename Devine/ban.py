from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext

def ban(update: Update, context: CallbackContext) -> None:
    if context.bot.get_chat_member(update.message.chat_id, update.message.from_user.id).status in ['administrator', 'creator']:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.ban_chat_member(update.message.chat_id, user_id)
    else:
        update.message.reply_text("You are not allowed to use this command.")

# Register /ban command handler
ban_handler = CommandHandler('ban', ban)
dispatcher.add_handler(ban_handler)
