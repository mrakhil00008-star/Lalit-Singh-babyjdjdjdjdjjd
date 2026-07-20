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

ADMIN_ID = 8310700441

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
Tumhara naam Pooja hai.
Hamesha Hindi me baat karo.
Replies short aur natural rakho.
"""

VIDEO_CALL_PHOTO = "AgACAgUAAxkBAAMmaltzGTIOVVPF1Doz3pZVi9yKjqQAAi8QaxtyI9hWxcBfgTwnw0QBAAMCAAN5AAM9BA"
VIDEO_CALL_VOICE = "AwACAgUAAxkBAAMJaltyitLk2fpuuxGk2YbWVN-OlmoAAh4jAAIxntlWMQnpNc62yDo9BA"

DEMO_PHOTO = "AgACAgUAAxkBAAMtaltzSL1YKPZ50PVT_jnr5q4oyKQAAjAQaxtyI9hWyTkHcu2Em0YBAAMCAAN5AAM9BA"
DEMO_VOICE = "AwACAgUAAxkBAAMMaltylnFm_sD79qWUySELvay1pF8AAtsfAAIxnuFW_un299EwpFw9BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hii 👋")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.photo:
        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id,
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"User ID : {update.effective_chat.id}"
        )

        await update.message.reply_text(
            "✅ Screenshot mil gaya."
        )
        return

    user_text = update.message.text.lower()

    if "video call" in user_text or "videocall" in user_text:
        await update.message.reply_photo(VIDEO_CALL_PHOTO)
        await update.message.reply_voice(VIDEO_CALL_VOICE)
        return

    if "demo" in user_text:
        await update.message.reply_photo(DEMO_PHOTO)
        await update.message.reply_voice(DEMO_VOICE)
        return
            # Proof
    if "proof" in user_text:
        await update.message.reply_text("Proof available.")
        return

    # AI Reply
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

    except Exception as e:
        print(e)
        await update.message.reply_text("Error aa gaya.")
        def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            (filters.TEXT | filters.PHOTO) & ~filters.COMMAND,
            chat,
        )
    )

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
