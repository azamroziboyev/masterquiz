from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """Return the main menu keyboard."""
    keyboard = [
        [KeyboardButton("Guide"), KeyboardButton("Help")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_admin_keyboard():
    """Return the admin menu keyboard."""
    keyboard = [
        [InlineKeyboardButton("Broadcast", callback_data="admin_broadcast")],
        [InlineKeyboardButton("User Stats", callback_data="admin_stats")],
        [InlineKeyboardButton("Back to Main Menu", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_broadcast_confirm_keyboard():
    """Return the keyboard for confirming a broadcast."""
    keyboard = [
        [InlineKeyboardButton("Confirm", callback_data="confirm_broadcast")],
        [InlineKeyboardButton("Cancel", callback_data="cancel_broadcast")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_broadcast_type_keyboard():
    """Return the keyboard for selecting broadcast type."""
    keyboard = [
        [InlineKeyboardButton("Text", callback_data="broadcast_text")],
        [InlineKeyboardButton("Photo", callback_data="broadcast_photo")],
        [InlineKeyboardButton("Video", callback_data="broadcast_video")],
        [InlineKeyboardButton("Poll", callback_data="broadcast_poll")],
        [InlineKeyboardButton("Cancel", callback_data="cancel_broadcast")]
    ]
    return InlineKeyboardMarkup(keyboard)
