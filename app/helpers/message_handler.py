import os
from telegram import Update
from telegram.ext import ContextTypes
from app.helpers.ai.gemini_ai import get_gemini_model


def handle_response(txt: str) -> str:
    chat = get_gemini_model().start_chat(history=[])
    response = chat.send_message(txt)
    
    return response.text


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    message = update.message.text
    
    print(f'User({update.message.chat.id}) in {message_type}: "{message}"')
    
    if message_type == 'group':
        if os.environ.get('BOT_USERNAME') in message:
            new_message = message.replace('BOT_USERNAME','').strip()
            response = handle_response(new_message)
        else:
            return
    else:
        response = handle_response(message)
    
    print('Bot: ', response)
    await update.message.reply_text(response)


async def errors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} caused error {context.error}')