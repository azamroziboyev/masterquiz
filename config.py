import os

# Bot token from environment variable or fallback
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")

# List of admin Telegram user IDs
ADMINS = [int(admin_id) for admin_id in os.environ.get("ADMIN_IDS", "123456789").split(",")]

# Database filename
DATABASE_FILE = "bot_users.db"

# Path to manual video
MANUAL_VIDEO_PATH = "manual.mp4"

# Message texts
WELCOME_MESSAGE = "Welcome to our bot! Use /help to see available commands."
HELP_MESSAGE = """
Available commands:
/start - Start the bot
/help - Show this help message
/guide - Show guide with video tutorial
/admin - Access admin panel (for admins only)
"""
GUIDE_TEXT = """
Here's a detailed guide on how to use this bot:

1. Use the /start command to begin interacting with the bot.
2. Navigate through the menu to access different features.
3. If you have any questions, use the /help command.

Check out the video tutorial below for a visual guide:
"""
ADMIN_PANEL_MESSAGE = """
Admin Panel

You can manage the bot from here. Select an option:
"""
BROADCAST_START_MESSAGE = """
Broadcast mode activated. You can send a message to all users.

Send the content you want to broadcast (text, photo, video, or poll).
Or use /cancel to cancel the broadcast.
"""
BROADCAST_CONFIRM_MESSAGE = """
Are you sure you want to send this message to all users?
"""
