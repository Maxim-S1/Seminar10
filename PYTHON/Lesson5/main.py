
from bots_comands import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5691972226:AAFNB5uv32W5PPV_rjnbDryZSaVAx-Jm7xg").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("minus", minus_command))
app.add_handler(CommandHandler("mult", multiplication_command))
app.add_handler(CommandHandler("div", division_command))
print('server start')
app.run_polling()