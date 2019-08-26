from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

import logging
from testbot3432bot_pro.commands import commands
import telegram


token = '941878373:AAEHl6jN4o6pLnzeEvZlkgeF5-ZgPcNwDZI'
request_kwargs = {
        'proxy_url':'socks5h://207.97.174.134:1080'
    }

updater = Updater(token, request_kwargs = request_kwargs)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)


# --------------------------------------------------------------------------------------------------------------------
def start(bot, update):
    commands.start(bot, update)
    commands.menu_actions(bot, update)
def date(bot, update):
    commands.time1(bot, update)
def temp(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='В каком городе температуру показать? ')
    city = updater.update_queue.get()['message']['text']
    commands.temp(bot, update, city)

# --------------------------------------------------------------------------------------------------------------------
def main():
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('date', date))
    dispatcher.add_handler(CommandHandler('temp', temp))
    dispatcher.add_handler(CallbackQueryHandler(commands.start))
    updater.start_polling()
if __name__ == '__main__':
    main()
