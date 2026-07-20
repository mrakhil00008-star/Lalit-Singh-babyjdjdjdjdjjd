import os
from groq import Groq
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

ADMIN_ID = 8310700441  # 👈 Yahan apna Telegram numeric ID dalna

client = Groq(api_key=GROQ_API_KEY)
