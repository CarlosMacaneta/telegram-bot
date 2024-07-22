import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from app.helpers.commands import start_command, help_command, custom_command
from app.helpers.message_handler import errors, handle_message


if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(os.environ.get('TOKEN_KEY')).build()
    
    # Command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Error handlers
    app.add_error_handler(errors)
    
    
    # checking app updates
    print("Polling...")
    app.run_polling(poll_interval=5)