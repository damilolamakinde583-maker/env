"""Main application entry point for ArtSpark6Bot."""
import logging
from telegram.ext import Application, Defaults, CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode

from config import BOT_TOKEN, LOG_LEVEL
from handlers import (
    start_command,
    help_command,
    about_command,
    imagine_command,
    shorten_command,
    echo_message,
    error_handler
)

logger = logging.getLogger(__name__)


def create_application() -> Application:
    """Create and configure the bot application."""
    # Configure default parsing mode
    defaults = Defaults(parse_mode=ParseMode.HTML)
    
    # Build the application
    app = Application.builder() \
        .token(BOT_TOKEN) \
        .defaults(defaults) \
        .build()
    
    # Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("imagine", imagine_command))
    app.add_handler(CommandHandler("shorten", shorten_command))
    
    # Register message handler for echo (catch-all)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
    
    # Register error handler
    app.add_error_handler(error_handler)
    
    return app


def main() -> None:
    """Start the bot."""
    logger.info("🤖 Starting ArtSpark6Bot...")
    
    try:
        app = create_application()
        logger.info("✅ Bot is running! (Press Ctrl+C to stop)")
        app.run_polling(allowed_updates=["message", "callback_query"])
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        raise


if __name__ == "__main__":
    main()
