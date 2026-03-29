from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# 🔑 TOKEN
TOKEN = os.environ.get("BOT_TOKEN")


# 🌐 FAKE SERVER (for Render)
def run_fake_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is running!")

    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


# 🚀 START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    text = f"""✨ Hello {user} 👋

🚀 I am a powerful private file manager bot
🔐 I store files securely in a protected channel
⚡ Access files instantly using special links"""

    keyboard = [
        [InlineKeyboardButton("📢 JOIN BACKUP", url="https://t.me/BP_MOVIE_SEARCH_GROUP")],
        [
            InlineKeyboardButton("✨ ABOUT", callback_data="about"),
            InlineKeyboardButton("❌ CLOSE", callback_data="close")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)


# 🎯 BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        keyboard = [
            [InlineKeyboardButton("❌ Close", callback_data="close")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            "⚡ MADE BY MASTER:\n[ʟʏɴx † 666](https://t.me/+MhjCXtPu7txjNzBl)",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "close":
        await query.message.delete()


# ▶️ MAIN APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot is running...")

# 🚀 Start fake server 
threading.Thread(target=run_fake_server).start()

# ▶️ Run bot
app.run_polling()
