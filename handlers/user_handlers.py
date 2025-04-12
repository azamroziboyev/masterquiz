import logging
from telegram import Update
from telegram.ext import ContextTypes

from config import WELCOME_MESSAGE, HELP_MESSAGE
from database import add_user
from keyboards import get_main_keyboard
from utils import extract_user_data

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    user_data = extract_user_data(update)
    
    # Add user to database
    add_user(
        user_data['user_id'],
        user_data['username'],
        user_data['first_name'],
        user_data['last_name']
    )
    
    # Send welcome message with main keyboard
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=get_main_keyboard()
    )
    logger.info(f"User {user_data['user_id']} started the bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command."""
    await update.message.reply_text(
        HELP_MESSAGE,
        reply_markup=get_main_keyboard()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks."""
    query = update.callback_query
    await query.answer()
    
    # Handle different callback data
    if query.data == "back_to_main":
        await query.edit_message_text(
            text="Back to main menu",
            reply_markup=get_main_keyboard()
        )
