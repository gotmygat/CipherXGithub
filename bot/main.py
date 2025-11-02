"""
CipherX Telegram Bot - Main Entry Point

This bot provides real-time cryptocurrency trading signals, whale wallet tracking,
and AI-powered market analysis directly in Telegram.
"""

import asyncio
import logging
import os
from datetime import datetime

from telegram import Update, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

from handlers.start import start_command
from handlers.wallet import wallet_command, track_wallet
from handlers.signals import signals_command, latest_signals
from handlers.stats import stats_command
from handlers.subscribe import subscribe_command
from handlers.help import help_command
from services.wallet_tracker import WalletTracker
from services.signal_generator import SignalGenerator
from config.settings import Settings

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class CipherXBot:
    """Main bot application class."""
    
    def __init__(self):
        self.settings = Settings()
        self.application = None
        self.wallet_tracker = WalletTracker()
        self.signal_generator = SignalGenerator()
        
    async def initialize(self):
        """Initialize bot application and services."""
        # Build application
        self.application = (
            Application.builder()
            .token(self.settings.TELEGRAM_BOT_TOKEN)
            .build()
        )
        
        # Register command handlers
        self.application.add_handler(CommandHandler("start", start_command))
        self.application.add_handler(CommandHandler("wallet", wallet_command))
        self.application.add_handler(CommandHandler("signals", signals_command))
        self.application.add_handler(CommandHandler("stats", stats_command))
        self.application.add_handler(CommandHandler("subscribe", subscribe_command))
        self.application.add_handler(CommandHandler("help", help_command))
        
        # Register callback handlers
        self.application.add_handler(CallbackQueryHandler(track_wallet, pattern="^track_"))
        self.application.add_handler(CallbackQueryHandler(latest_signals, pattern="^signal_"))
        
        # Error handler
        self.application.add_error_handler(self.error_handler)
        
        # Set bot commands (appears in Telegram menu)
        await self.set_bot_commands()
        
        logger.info("CipherX Bot initialized successfully")
        
    async def set_bot_commands(self):
        """Set bot command menu."""
        commands = [
            BotCommand("start", "Start CipherX bot"),
            BotCommand("wallet", "Get wallet information"),
            BotCommand("signals", "View AI trading signals"),
            BotCommand("stats", "Display your statistics"),
            BotCommand("subscribe", "Subscribe to premium alerts"),
            BotCommand("help", "Show help message"),
        ]
        await self.application.bot.set_my_commands(commands)
        
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors."""
        logger.error(f"Exception while handling update {update}: {context.error}")
        
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "❌ An error occurred while processing your request. "
                "Please try again later."
            )
    
    async def start_background_tasks(self):
        """Start background tasks for monitoring and alerts."""
        # Start wallet monitoring
        asyncio.create_task(self.wallet_tracker.monitor_wallets())
        
        # Start signal generation
        asyncio.create_task(self.signal_generator.generate_signals())
        
        logger.info("Background tasks started")
        
    async def run(self):
        """Run the bot."""
        await self.initialize()
        await self.start_background_tasks()
        
        logger.info("🚀 CipherX Bot is now running...")
        logger.info(f"Bot username: @{(await self.application.bot.get_me()).username}")
        
        # Start polling
        await self.application.run_polling(allowed_updates=Update.ALL_TYPES)


async def main():
    """Main entry point."""
    bot = CipherXBot()
    
    try:
        await bot.run()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
