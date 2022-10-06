# Создать калькулятор для работы с рациональными и комплексными числами,
#  организовать меню, добавив в неё систему логирования(Дополнительно)
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5737519432:AAFjqfphiSW_eHa5itIl8AQsu1PnWEfC-Wc')
updater = Updater(token='5737519432:AAFjqfphiSW_eHa5itIl8AQsu1PnWEfC-Wc')
dispatcher = updater.dispatcher

def welcome(update, context):
    context.bot.send_message(update.effective_chat.id, 'Это калькулятор введите выражение')
    return calc
    
def calc(update, context):
    text = update.message.text
    result = eval(text)
    context.bot.send_message(update.effective_chat.id, result)
    logging(text,result)

def logging(text,result):
    with open('calc_log.txt', 'a+') as file:
        file.write(f'{text} = {result}\n')
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'пока')
    return ConversationHandler.END

 
calc_handler = CommandHandler('calc', welcome)
message_handler = MessageHandler(Filters.text, calc)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[calc_handler],
                                   states={calc:[message_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(cancel_handler)

updater.start_polling()
updater.idle()  