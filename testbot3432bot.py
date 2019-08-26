from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup
import logging
from testbot3432bot_pro.commands import commands
#######################################  Bot  #####################################################
def start(bot, update):
    update.message.reply_text(start_message(),
                              reply_markup=start_keyboard())
########  Callback_KeyBoards_Handler  ########
def callback_query_handler(bot, update):
    query = update.callback_query
    data = query.data
    if data == 'main':
        bot.edit_message_text(chat_id = query.message.chat_id,
                              message_id = query.message.message_id,
                              text = main_menu_message(),
                              reply_markup = main_menu_keyboard())
    elif data == "opt1":
        bot.edit_message_text(chat_id = query.message.chat_id,
                              message_id = query.message.message_id,
                              text = opt1_message(),
                              reply_markup = opt1_keyboard())

    elif data == 'opt2':
            bot.edit_message_text(chat_id = query.message.chat_id,
                                  message_id = query.message.message_id,
                                  text = opt2_message(),
                                  reply_markup = opt2_keyboard())

    elif data == 'opt2':
            bot.edit_message_text(chat_id = query.message.chat_id,
                                  message_id = query.message.message_id,
                                  text = opt3_message(),
                                  reply_markup = opt3_keyboard())

    elif data == 'opt1_1':
            bot.edit_message_text(chat_id = query.message.chat_id,
                                  message_id = query.message.message_id,
                                  text = opt1_1_message() + commands.time1(),
                                  reply_markup = back_in_main_keyboard(bot, update))

    elif data == 'opt1_2':
            bot.edit_message_text(chat_id = query.message.chat_id,
                                  message_id = query.message.message_id,
                                  text = 'Введите название города: ',)
            city = updater.update_queue.get()['message']['text']
            bot.send_message(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text= str('Прогода в городе ' + city + ': ' + commands.temp(bot, update, city)),
                                  reply_markup=back_in_main_keyboard(bot, update))
########  Message_Handler  ########
def message_handler(bot, update):
    query = update.message
    text = query.text
    if text == 'Меню':
        bot.send_message(chat_id = query.chat_id,
                         text = 'Главное меню:    ',
                         reply_markup = main_menu_keyboard())

#######################################  KeyBoards  ###############################################
def start_keyboard():
    keyboards = [
        [
            KeyboardButton('Меню')
        ]
    ]
    return ReplyKeyboardMarkup(keyboards, resize_keyboard=True)

def main_menu_keyboard():
    keyboards = [
        [InlineKeyboardButton('Время и Температура', callback_data = 'opt1')],
        [InlineKeyboardButton('opt2', callback_data = 'opt2')],
        [InlineKeyboardButton('opt3', callback_data = 'opt3')]
    ]
    return InlineKeyboardMarkup(keyboards)

def opt1_keyboard():
    keyboards = [
        [InlineKeyboardButton('Время', callback_data='opt1_1'),
         InlineKeyboardButton('Температура', callback_data='opt1_2')],

        [InlineKeyboardButton('Назад', callback_data='main')]
    ]
    return InlineKeyboardMarkup(keyboards)

def opt2_keyboard():
    keyboards = [
        [InlineKeyboardButton('opt2_1', callback_data = 'opt2_1')],
        [InlineKeyboardButton('opt2_2', callback_data = 'opt2_2')],
        [InlineKeyboardButton('main menu', callback_data = 'main')]
    ]
    return InlineKeyboardMarkup(keyboards)

def opt3_keyboard():
    keyboards = [
        [InlineKeyboardButton('opt3_1', callback_data = 'opt3_1')],
        [InlineKeyboardButton('opt3_2', callback_data = 'opt3_2')],
        [InlineKeyboardButton('main menu', callback_data = 'main')]
    ]
    return InlineKeyboardMarkup(keyboards)

def back_in_main_keyboard(bot, update):
    callback_data = str(update.callback_query.data).rsplit('_')[0]
    keyboards = [
        [InlineKeyboardButton('Назад', callback_data = callback_data)]
    ]
    return InlineKeyboardMarkup(keyboards)
#######################################  Messages  ################################################
def start_message():
    return 'Привет! Чем могу помочь?'
def main_menu_message():
    return 'The main menu, choose one command: '
def opt1_message():
    return 'The Option 1, choose one command:'
def opt2_message():
    return 'The Option 2, choose one command: '
def opt3_message():
    return 'The Option 3, choose one command: '
def opt1_1_message():
    return 'Время: '
def opt1_2_message():
    return 'Opt1_2'

#######################################  Hendler  #################################################
token = '941878373:AAEHl6jN4o6pLnzeEvZlkgeF5-ZgPcNwDZI'
request_kwargs = {
        'proxy_url':'socks5h://207.97.174.134:1080'
    }

updater = Updater(token, request_kwargs = request_kwargs)
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))
updater.start_polling()


#######################################  Logger  ##################################################
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)