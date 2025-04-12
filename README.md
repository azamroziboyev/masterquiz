# Enhanced Telegram Bot

A Telegram bot with enhanced admin broadcasting capabilities and improved guide section with video content.

## Features

1. Admin broadcasting functionality:
   - Broadcast messages to all users
   - Support for text, photos, videos, and polls
   - Exclude sender from broadcast recipients
   
2. Enhanced guide section:
   - Text guide with detailed instructions
   - Video tutorial support (manual.mp4)

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install python-telegram-bot
   ```
3. Set environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
   - `ADMIN_IDS`: Comma-separated list of admin Telegram user IDs
   
4. Place your `manual.mp4` video in the root directory
   
5. Run the bot:
   ```
   python main.py
   ```

## Bot Commands

- `/start` - Start the bot
- `/help` - Show help information
- `/guide` - Show guide with video tutorial
- `/admin` - Access admin panel (admins only)
- `/broadcast` - Start broadcast process (admins only)

## Admin Features

1. **Broadcasting**:
   - Text messages
   - Photos with captions
   - Videos with captions
   - Polls with multiple options
   
2. **User Statistics**:
   - View total user count

## File Structure

- `main.py` - Main bot file
- `config.py` - Configuration settings
- `database.py` - Database functions
- `keyboards.py` - Keyboard layouts
- `filters.py` - Custom filters
- `utils.py` - Utility functions
- `handlers/` - Command and message handlers

## Requirements

- Python 3.7+
- python-telegram-bot (v20.0+)
