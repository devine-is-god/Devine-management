from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext

def demote(update: Update, context: CallbackContext) -> None:
    if context.bot.get_chat_member(update.message.chat_id, update.message.from_user.id).status in ['administrator', 'creator']:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.promote_chat_member(update.message.chat_id, user_id, can_change_info=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False)
    else:
        update.message.reply_text("You are not allowed to use this command.")

# Register /demote command handler
demote_handler = CommandHandler('demote', demote)
dispatcher.add_handler(demote_handler)
