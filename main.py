from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler
import gspread
import os
import json

#CONFIG
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
SPREAD_CREDENTIALS = json.loads(os.environ["SPREAD_CREDENTIALS"])
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
###

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()


def add_link(link):
    print(f"Adding link {link}")
    gc = gspread.service_account_from_dict(SPREAD_CREDENTIALS)
    sh = gc.open_by_key(SPREADSHEET_ID)
    counter = sh.get_worksheet(0)
    current_value = int(counter.acell('B1').value)
    new_value = current_value + 1
    data = sh.get_worksheet(1)
    data.update_cell(new_value, 1, link)
    counter.update('B1', new_value)
    gc.session.close()
    return f"Old size was {current_value}, new size is {new_value}"


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "ping":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="pong")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Storing...")
        r = add_link(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=r)

handler = MessageHandler(filters.TEXT, unknown)
application.add_handler(handler)
application.run_polling()
