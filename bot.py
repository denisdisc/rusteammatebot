from random import choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, sport_type, user_coordinates, find_teammate,
                        talk_to_me)
import logging
import config

logging.basicConfig(filename='bot.log', level=logging.INFO)
sports_list = {'ultimate', 'discgolf', 'badminton'}

def main():
    mybot = Updater(config.API_KEY, use_context=True, request_kwargs=config.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("sport", sport_type))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.regex('^(Discgolf)$'), find_teammate))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
