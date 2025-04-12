import logging
from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_PANEL_MESSAGE, ADMINS
from keyboards import get_admin_keyboard
from database import get_all_users

logger = logging.getLogger(__name__)

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /admin command."""
    user_id = update.effective_user.id
    
    # Check if user is admin
    if user_id in ADMINS:
        await update.message.reply_text(
            ADMIN_PANEL_MESSAGE,
            reply_markup=get_admin_keyboard()
        )
        logger.info(f"Admin {user_id} accessed admin panel")
    else:
        await update.message.reply_text("You don't have permission to access the admin panel.")
        logger.warning(f"User {user_id} tried to access admin panel without permission")

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user statistics."""
    query = update.callback_query
    await query.answer()
    
    if query.data == "admin_stats":
        users = get_all_users()
        user_count = len(users)
        
        stats_message = f"Bot Statistics:\n\nTotal users: {user_count}"
        
        await query.edit_message_text(
            text=stats_message,
            reply_markup=get_admin_keyboard()
        )
        logger.info(f"Admin {query.from_user.id} viewed stats")
