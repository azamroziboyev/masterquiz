from telegram.ext import MessageFilter
from config import ADMINS

class AdminFilter(MessageFilter):
    """Filter for admin users."""
    
    def filter(self, message):
        """Check if the user is an admin."""
        return message.from_user.id in ADMINS
