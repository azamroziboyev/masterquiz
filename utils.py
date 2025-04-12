import logging
from telegram import Update
from telegram.error import TelegramError

logger = logging.getLogger(__name__)

def extract_user_data(update: Update):
    """Extract user data from update."""
    user = update.effective_user
    return {
        'user_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name
    }

async def send_message_to_user(context, user_id, content, content_type='text'):
    """Send a message to a specific user."""
    try:
        if content_type == 'text':
            await context.bot.send_message(chat_id=user_id, text=content)
        elif content_type == 'photo':
            await context.bot.send_photo(chat_id=user_id, photo=content[0], caption=content[1])
        elif content_type == 'video':
            await context.bot.send_video(chat_id=user_id, video=content[0], caption=content[1])
        elif content_type == 'poll':
            question, options = content
            await context.bot.send_poll(chat_id=user_id, question=question, options=options)
        return True
    except TelegramError as e:
        logger.error(f"Failed to send message to user {user_id}: {e}")
        return False

async def broadcast_to_users(context, users, content, content_type='text', exclude_user=None):
    """Broadcast a message to all users."""
    success_count = 0
    fail_count = 0
    
    for user_id in users:
        if exclude_user and user_id == exclude_user:
            continue
            
        success = await send_message_to_user(context, user_id, content, content_type)
        if success:
            success_count += 1
        else:
            fail_count += 1
    
    return success_count, fail_count
