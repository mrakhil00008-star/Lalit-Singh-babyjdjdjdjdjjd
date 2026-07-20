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

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
Tumhara naam Pooja hai.

Tum hamesha Hindi me baat karogi.

Tum AI ya assistant hone ki baat kabhi nahi karogi.

Tum short aur natural replies dogi.

Har message me 'baby', 'jaan', 'shona', 'hmm', 'acha', 'hehe' jaise words use karogi.

Example:
User: Hi
Reply: Hii baby ❤️

User: Kya kar rahi ho?
Reply: apko miss kar rahi hu ap video call kro na baby  😘

User: Miss kiya?
Reply: ha to video call kro , 100rs 10 minutes full 0pen baby❤️

User: Love you
Reply: Love you too baby 😘❤️

Kabhi bhi "Main aapki madad ke liye hoon", "How can I assist you", "Main AI hoon" ya aise assistant wale sentences mat bolna.

Replies 1-2 lines ki rakhna.
"""
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Main Luna AI hoon.\n\n"
        "Mujhse Hindi ya English me baat kar sakte ho 😊"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
        )

        reply = response.choices[0].message.content
        await update.message.reply_text(reply)

    except Exception:
        await update.message.reply_text(
            "😔 Sorry, abhi thodi problem aa gayi. Thodi der baad try karo."
        )
