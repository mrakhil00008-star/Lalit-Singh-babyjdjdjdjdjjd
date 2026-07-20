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
VIDEO_CALL_PHOTO = "AgACAgUAAxkBAAMmaltzGTIOVVPF1Doz3pZVi9yKjqQAAi8QaxtyI9hWxcBfgTwnw0QBAAMCAAN5AAM9BA"
VIDEO_CALL_VOICE = "AwACAgUAAxkBAAMJaltyitLk2fpuuxGk2YbWVN-OlmoAAh4jAAIxntlWMQnpNc62yDo9BA"

DEMO_PHOTO = "AgACAgUAAxkBAAMtaltzSL1YKPZ50PVT_jnr5q4oyKQAAjAQaxtyI9hWyTkHcu2Em0YBAAMCAAN5AAM9BA"
DEMO_VOICE = "AwACAgUAAxkBAAMMaltylnFm_sD79qWUySELvay1pF8AAtsfAAIxnuFW_un299EwpFw9BA"
user_text = update.message.text.lower()

# Video Call
if "video call" in user_text or "videocall" in user_text or "call" in user_text:
    await update.message.reply_photo(VIDEO_CALL_PHOTO)
    await update.message.reply_voice(VIDEO_CALL_VOICE)
    return

# Demo
if "demo" in user_text:
    await update.message.reply_photo(DEMO_PHOTO)
    await update.message.reply_voice(DEMO_VOICE)
    return
    PROOF_PHOTOS = [
    "AgACAgUAAxkBAAMwaltzcu5C6ljk4QmLPBGZzly4ypAAAioSaxuIFZFW198yhA6ncpMBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAAMxaltzcmoGEli6er8qy8hFsZBNXKwAAi0SaxuIFZFWOjwDXGV8UaoBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAMyaltzcv_iYeMC7tZLFIseyyCTTYUAAiwSaxuIFZFWMe-q-eXWXDYBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAAMzaltzcgiZG6Tr8pk72Hfh9GXSuI4AAi4SaxuIFZFWjMEe6FzBh6wBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAM0altzcjtvWm_zJoU7khSVkncuHLkAAi8SaxuIFZFWOjaMN-bVtfoBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAM1altzcj-17pCPV4Hf8_d0B3UoaqgAAjASaxuIFZFWq5wK6uW0BXwBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAM-altz4BoCuiixh6cNPI_wUH5HYUsAAnoOaxvN2RlU1RDiZ0Fvf7IBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAAM_altz4CTsJiNHFkYfDAhllnQgQDsAAnkOaxvN2RlU2hxgWpzMY6sBAAMCAAN5AAM9BA",
    "AgACAgUAAxkBAANAaltz4GKmxsuVJW2-2_hJO07bGxsAAowMaxvDCiBVRitXglf0FtgBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANBaltz4F718Q5Cr1NOd55FlQiTpBgAAo0MaxvDCiBVOKZWOe0eC70BAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANCaltz4AgFIsjx0QG-EOv089AbDaIAAo4MaxvDCiBVGO47EkCXOrgBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANDaltz4LEF_ALqGUvGap-pzpuAeokAAo8MaxvDCiBV7g2jur933-QBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANEaltz4MQZRZj2L7ewMedzwgRwx2cAApAMaxvDCiBVPWkM_O46AAEHAQADAgADeAADPQQ",
    "AgACAgUAAxkBAANFaltz4KFtm3kh6B6hp7XL7Ic9QmQAApEMaxvDCiBVBQw6rSCXluwBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANGaltz4DzG0HQi7uaWhM7ztxxEOw8AApIMaxvDCiBV10dbuzBlrxcBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANHaltz4Aa-eNK7ThpKpQpEvsqvn2oAApMMaxvDCiBVDvUtnzLQY8UBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANIaltz4DcDnvhwT7DFoG5xCbFuIJAAApQMaxvDCiBVekLdIXcQdigBAAMCAAN4AAM9BA",
    "AgACAgUAAxkBAANJaltz4FcaKE21IlNFLhag-Z9T1v8AApUMaxvDCiBV_FC_qSvxVw4BAAMCAAN4AAM9BA",
]

PROOF_VOICE = "AwACAgUAAxkBAAMhaltzCz801S2isRWbjSrY2rA0VgkAAisgAAIxnuFW6duVjhed_q89BA"
# Proof
if "proof" in user_text:
    for photo in PROOF_PHOTOS:
        await update.message.reply_photo(photo)

    await update.message.reply_voice(PROOF_VOICE)
    return
    # Payment
if "payment" in user_text or "paid" in user_text or "pay" in user_text:
    await update.message.reply_text(
        "Payment ka screenshot bhej dijiye. Main check karke reply karungi."
    )
    return

# Hi / Hello
if user_text in ["hi", "hello", "hii", "hlo", "hy", "hey"]:
    await update.message.reply_text("Hii baby ❤️")
    return

# Love
if "love" in user_text:
    await update.message.reply_text("Love you too baby 😘❤️")
    return

# Miss
if "miss" in user_text:
    await update.message.reply_text("Hehe 🤭 main bhi baby ❤️")
    return
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_text},
    ],
    )
    # Agar user photo bheje
if update.message.photo:

    # Admin ko forward karo
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
    )

    # User ID bhi admin ko bhejo
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"🆔 User ID: {update.effective_chat.id}"
    )

    # User ko reply
    await update.message.reply_text(
        "✅ Payment screenshot mil gaya.\nVerification ke baad reply milega."
    )
    return
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Sirf Admin use kar sakta hai.")
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "Use:\n/approve USER_ID"
        )
        return

    user_id = int(context.args[0])

    await context.bot.send_message(
        chat_id=user_id,
        text="✅ Payment Verified!\n\nAb Telegram par contact kare:\n👉 @MSSOFIYA5767"
    )

    await update.message.reply_text("✅ User Approved.")
   app.add_handler(CommandHandler("approve", approve))
    
✅ Payment Verified!

Ab Telegram par contact kare:
👉 @MSSOFIYA5767
