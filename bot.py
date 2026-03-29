from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os
TOKEN = os.environ.get("BOT_TOKEN")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    text = f"✨ Hello {user} 👋\n\nI manage and store private files in a protected channel so users can access them anytime using special links.!"

    keyboard = [
        [InlineKeyboardButton("📢 JOIN BACKUP", url="https://t.me/BP_MOVIE_SEARCH_GROUP")],
        [
            InlineKeyboardButton("✨ ABOUT", callback_data="about"),
            InlineKeyboardButton("❌ CLOSE", callback_data="close")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)

# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ABOUT BUTTON
    if query.data == "about":
        keyboard = [
            [InlineKeyboardButton("❌ Close", callback_data="close")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            "MADE BY - MASTER:   [ʟʏɴx † 666](https://t.me/+MhjCXtPu7txjNzBl)",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    # CLOSE BUTTON
    elif query.data == "close":
        await query.message.delete()


# MAIN APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot is running...")
app.run_polling()
