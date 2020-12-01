from random import choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handlers import (greet_user, sport_type, user_coordinates, find_teammate,
                        talk_to_me)
from questionnaire import form_start, user_name, bot_rating, anketa_comment, anketa_skip, anketa_dontknow
import logging
import config


logging.basicConfig(filename='bot.log', level=logging.INFO)
sports_list = {'ultimate', 'discgolf', 'badminton'}

def main():
    mybot = Updater(config.API_KEY, use_context=True, request_kwargs=config.PROXY)
    
    dp = mybot.dispatcher

    anketa = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Заполнить анкету)$'), form_start)],
        states={
            "name": [MessageHandler(Filters.text, user_name)],
            "rating": [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), bot_rating)],
            "comment": [
                CommandHandler("skip", anketa_skip),
                MessageHandler(Filters.text, anketa_comment)
            ]
        },
        fallbacks=[
            MessageHandler(
                Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location,
                anketa_dontknow
            )
        ]
    )
    dp.add_handler(anketa)
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
