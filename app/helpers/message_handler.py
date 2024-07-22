import os
from telegram import Update
from telegram.ext import ContextTypes


def handle_response(txt: str) -> str:
    if 'hello' in txt.lower():
        return 'Hi there!'
    elif 'how are you' in txt.lower() or 'how are you?' in txt.lower():
        return 'I am good thanks.\nHow can I help?'
    elif 'I need to learn something' in txt.lower():
        return 'What would you like to learn?'
    elif 'anything' in txt.lower() or 'teach me what you know' in txt.lower():
        return "Alright, let's roll up your sleeves🙂"
    else:
        return 'I do not understand what you were trying to say.\nPlease try again later.'


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