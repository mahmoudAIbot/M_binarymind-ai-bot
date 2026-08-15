from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
BOT_TOKEN = "8606818676:AAFE0m2biaypqYkPk3t4JM16h8tQxWiTTeE"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("أهلاً بك في BinaryMind AI Bot")
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
