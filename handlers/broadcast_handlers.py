import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ContextTypes, 
    ConversationHandler, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler,
    filters
)

from config import BROADCAST_START_MESSAGE, BROADCAST_CONFIRM_MESSAGE, ADMINS
from keyboards import get_broadcast_confirm_keyboard, get_broadcast_type_keyboard, get_admin_keyboard
from database import get_all_users
from utils import broadcast_to_users

logger = logging.getLogger(__name__)

# Define conversation states
CHOOSING_TYPE, TYPING_TEXT, SENDING_PHOTO, SENDING_VIDEO, CREATING_POLL, POLL_OPTIONS = range(6)

# Store temporary broadcast data
broadcast_data = {}

async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /broadcast command."""
    user_id = update.effective_user.id
    
    # Check if user is admin
    if user_id in ADMINS:
        # Clear any previous broadcast data
        if user_id in broadcast_data:
            del broadcast_data[user_id]
            
        await update.message.reply_text(
            BROADCAST_START_MESSAGE,
            reply_markup=get_broadcast_type_keyboard()
        )
        logger.info(f"Admin {user_id} started broadcast")
        return CHOOSING_TYPE
    else:
        await update.message.reply_text("You don't have permission to broadcast messages.")
        logger.warning(f"User {user_id} tried to broadcast without permission")
        return ConversationHandler.END

async def handle_broadcast_type_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle broadcast type selection."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    # Initialize broadcast data for this user
    broadcast_data[user_id] = {'type': None, 'content': None}
    
    if query.data == "broadcast_text":
        broadcast_data[user_id]['type'] = 'text'
        await query.edit_message_text("Please send the text message you want to broadcast:")
        return TYPING_TEXT
    
    elif query.data == "broadcast_photo":
        broadcast_data[user_id]['type'] = 'photo'
        await query.edit_message_text("Please send the photo you want to broadcast (with optional caption):")
        return SENDING_PHOTO
    
    elif query.data == "broadcast_video":
        broadcast_data[user_id]['type'] = 'video'
        await query.edit_message_text("Please send the video you want to broadcast (with optional caption):")
        return SENDING_VIDEO
    
    elif query.data == "broadcast_poll":
        broadcast_data[user_id]['type'] = 'poll'
        await query.edit_message_text("Please send the poll question:")
        return CREATING_POLL
    
    elif query.data == "cancel_broadcast":
        await query.edit_message_text("Broadcast canceled.", reply_markup=get_admin_keyboard())
        if user_id in broadcast_data:
            del broadcast_data[user_id]
        return ConversationHandler.END

async def broadcast_text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text message for broadcasting."""
    user_id = update.effective_user.id
    text = update.message.text
    
    broadcast_data[user_id]['content'] = text
    
    await update.message.reply_text(
        f"You are about to broadcast the following text message:\n\n{text}\n\n{BROADCAST_CONFIRM_MESSAGE}",
        reply_markup=get_broadcast_confirm_keyboard()
    )
    return ConversationHandler.END

async def broadcast_photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photo for broadcasting."""
    user_id = update.effective_user.id
    photo = update.message.photo[-1].file_id
    caption = update.message.caption or ""
    
    broadcast_data[user_id]['content'] = (photo, caption)
    
    # Send confirmation message
    await context.bot.send_photo(
        chat_id=user_id,
        photo=photo,
        caption=caption
    )
    await update.message.reply_text(
        f"You are about to broadcast this photo with caption:\n\n{caption}\n\n{BROADCAST_CONFIRM_MESSAGE}",
        reply_markup=get_broadcast_confirm_keyboard()
    )
    return ConversationHandler.END

async def broadcast_video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle video for broadcasting."""
    user_id = update.effective_user.id
    video = update.message.video.file_id
    caption = update.message.caption or ""
    
    broadcast_data[user_id]['content'] = (video, caption)
    
    # Send confirmation message
    await context.bot.send_video(
        chat_id=user_id,
        video=video,
        caption=caption
    )
    await update.message.reply_text(
        f"You are about to broadcast this video with caption:\n\n{caption}\n\n{BROADCAST_CONFIRM_MESSAGE}",
        reply_markup=get_broadcast_confirm_keyboard()
    )
    return ConversationHandler.END

async def create_poll_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle poll question for broadcasting."""
    user_id = update.effective_user.id
    question = update.message.text
    
    # Store question temporarily
    if 'poll_data' not in broadcast_data[user_id]:
        broadcast_data[user_id]['poll_data'] = {}
    
    broadcast_data[user_id]['poll_data']['question'] = question
    broadcast_data[user_id]['poll_data']['options'] = []
    
    await update.message.reply_text(
        f"Poll question: {question}\n\nNow send the poll options one by one. Send /done when finished."
    )
    return POLL_OPTIONS

async def poll_options_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle poll options for broadcasting."""
    user_id = update.effective_user.id
    
    # Check if user wants to finish adding options
    if update.message.text == "/done":
        # Need at least 2 options
        if len(broadcast_data[user_id]['poll_data']['options']) < 2:
            await update.message.reply_text("A poll needs at least 2 options. Please add more options:")
            return POLL_OPTIONS
        
        question = broadcast_data[user_id]['poll_data']['question']
        options = broadcast_data[user_id]['poll_data']['options']
        
        broadcast_data[user_id]['content'] = (question, options)
        
        # Show preview and confirmation
        options_text = "\n".join([f"- {option}" for option in options])
        await update.message.reply_text(
            f"You are about to broadcast a poll:\n\nQuestion: {question}\n\nOptions:\n{options_text}\n\n{BROADCAST_CONFIRM_MESSAGE}",
            reply_markup=get_broadcast_confirm_keyboard()
        )
        return ConversationHandler.END
    
    # Add the option
    option = update.message.text
    broadcast_data[user_id]['poll_data']['options'].append(option)
    
    options_so_far = "\n".join([f"- {opt}" for opt in broadcast_data[user_id]['poll_data']['options']])
    await update.message.reply_text(
        f"Option added. Current options:\n{options_so_far}\n\nSend another option or /done to finish."
    )
    return POLL_OPTIONS

async def confirm_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Confirm and send the broadcast."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    if user_id not in broadcast_data:
        await query.edit_message_text("Error: Broadcast data not found. Please try again.")
        return
    
    # Get all users from the database
    users = get_all_users()
    
    # Send broadcast message to all users
    content_type = broadcast_data[user_id]['type']
    content = broadcast_data[user_id]['content']
    
    await query.edit_message_text("Broadcasting messages... Please wait.")
    
    # Send the broadcast
    success_count, fail_count = await broadcast_to_users(
        context,
        users,
        content,
        content_type,
        exclude_user=user_id  # Exclude the sender from receiving the broadcast
    )
    
    # Inform admin about broadcast results
    await context.bot.send_message(
        chat_id=user_id,
        text=f"Broadcast completed!\n\nSuccessfully sent to: {success_count} users\nFailed: {fail_count} users",
        reply_markup=get_admin_keyboard()
    )
    
    # Clean up
    del broadcast_data[user_id]
    logger.info(f"Admin {user_id} sent broadcast to {success_count} users (failed: {fail_count})")

async def cancel_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the broadcast."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    # Clean up broadcast data
    if user_id in broadcast_data:
        del broadcast_data[user_id]
    
    await query.edit_message_text("Broadcast canceled.", reply_markup=get_admin_keyboard())
    logger.info(f"Admin {user_id} canceled broadcast")
    
# Set up the conversation handler
broadcast_conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("broadcast", broadcast_command),
        CallbackQueryHandler(handle_broadcast_type_selection, pattern="^broadcast_")
    ],
    states={
        CHOOSING_TYPE: [
            CallbackQueryHandler(handle_broadcast_type_selection, pattern="^broadcast_")
        ],
        TYPING_TEXT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, broadcast_text_handler)
        ],
        SENDING_PHOTO: [
            MessageHandler(filters.PHOTO, broadcast_photo_handler)
        ],
        SENDING_VIDEO: [
            MessageHandler(filters.VIDEO, broadcast_video_handler)
        ],
        CREATING_POLL: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, create_poll_handler)
        ],
        POLL_OPTIONS: [
            MessageHandler(filters.TEXT, poll_options_handler)
        ],
    },
    fallbacks=[
        CommandHandler("cancel", cancel_broadcast),
        CallbackQueryHandler(cancel_broadcast, pattern="^cancel_broadcast$")
    ]
)
