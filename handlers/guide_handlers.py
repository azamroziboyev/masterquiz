import logging
import os
from telegram import Update
from telegram.ext import ContextTypes

from config import GUIDE_TEXT, MANUAL_VIDEO_PATH

logger = logging.getLogger(__name__)

async def guide_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /guide command - send guide text and video."""
    user_id = update.effective_user.id
    
    # First, send the guide text
    await update.message.reply_text(GUIDE_TEXT)
    
    # Then, send the video guide
    try:
        # Check if video file exists
        if os.path.exists(MANUAL_VIDEO_PATH):
            with open(MANUAL_VIDEO_PATH, 'rb') as video_file:
                await context.bot.send_video(
                    chat_id=user_id,
                    video=video_file,
                    caption="Video guide on how to use the bot"
                )
            logger.info(f"Sent guide video to user {user_id}")
        else:
            logger.error(f"Guide video file not found: {MANUAL_VIDEO_PATH}")
            await update.message.reply_text(
                "Sorry, the video guide is temporarily unavailable. Please try again later."
            )
    except Exception as e:
        logger.error(f"Failed to send guide video: {e}")
        await update.message.reply_text(
            "Sorry, there was an error sending the video guide. Please try again later."
        )
