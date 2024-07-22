import os
from telegram import Update
from telegram import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.reply_text('Hello! Thanks for starting a new conversation. I can teach you everything!')