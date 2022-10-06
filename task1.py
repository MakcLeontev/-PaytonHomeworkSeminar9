# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5737519432:AAFjqfphiSW_eHa5itIl8AQsu1PnWEfC-Wc')
updater = Updater(token='5737519432:AAFjqfphiSW_eHa5itIl8AQsu1PnWEfC-Wc')
dispatcher = updater.dispatcher

def del_abv(update, context):
    text = update.message.text.split()
    for i in text:
        if 'абв' in i:
            text.remove(i)        
    a=' '.join(map(str, text))
    context.bot.send_message(update.effective_chat.id, a )

delabv_handler = MessageHandler(Filters.text, del_abv)

dispatcher.add_handler(delabv_handler)

updater.start_polling()
updater.idle()