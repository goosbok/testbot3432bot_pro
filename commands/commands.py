import time
from temperature import temper
import telegram
from telegram.ext import CommandHandler


# показать время
def time1():
    return time.ctime(time.time())


#  приветсвие
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = 'Привет!')
    reply_buttons = [
        [telegram.InlineKeyboardButton(text='тык сюда', callback_data='123')],
        [telegram.InlineKeyboardButton(text='или сюда', callback_data='321')]
    ]
    reply_markup = telegram.InlineKeyboardMarkup(reply_buttons)
    bot.send_message(chat_id=update.message.chat_id, text='Чем могу помочь?', reply_markup=reply_markup)

def menu_actions(bot, update):
    query = update.callback_query
    print(dir(update))
    # if query.data == '123':
    #     time1(bot, update)

# температура
def temp(bot, update, city):
    t = temper(bot, update, city)
    return str(t)

