from telegram import Update
from telegram import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.reply_text('Hello! Thanks for starting a new conversation. I can teach you everything!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.reply_text('I am nerd! Please type something to help.')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.reply_text('This is a custom command.')