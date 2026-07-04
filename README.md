# ArtSpark6Bot 🎨

A Telegram bot for AI image generation and URL shortening.

## Features
- 🖼️ Generate AI images from text prompts
- 🔗 Shorten long URLs
- 📝 Echo messages (demo)

## Deployment on Railway
1. Fork this repository to GitHub
2. Create a new project on Railway
3. Connect your GitHub repository
4. Add environment variables
5. Deploy!

## Environment Variables
- `BOT_TOKEN` - Your Telegram bot token from @BotFather
- `STABILITY_API_KEY` - Stability AI API key (optional)
- `OPENAI_API_KEY` - OpenAI API key (optional)
- `BITLY_API_KEY` - Bitly API key (optional)
- `LOG_LEVEL` - Logging level (default: INFO)

## Commands
- `/start` - Welcome message
- `/help` - Show help
- `/about` - About the bot
- `/imagine <prompt>` - Generate an image
- `/shorten <url>` - Shorten a URL

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python src/bot.py
