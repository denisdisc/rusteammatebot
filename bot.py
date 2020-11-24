import logging
import config
from emoji import emojize
from random import choice
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log', level=logging.INFO)
sports_list = {'ultimate', 'discgolf', 'badminton'}

def main_keyboard():
    return ReplyKeyboardMarkup([['Discgolf', 'Ultimate'], [ 'Badminton' ]])

def greet_user(update, context):
    print('Вызван /start')
    smile = choice(config.USER_EMOJI)
    smile = emojize(smile, use_aliases=True)
    update.message.reply_text(f'Привет! {smile} Найди партнера(ов) для игры с помощю команды /sport')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def sport_type(update, context):
    # i use global variable 'sports_list', be careful
    print('Вызван /sport')
    if context.args: 
        sport = context.args[0]
        if sport in sports_list:
            message = f"You search mate by {sport}"
        else:
            message = f"I dont't known {sport}, please choose another sport"
    else:
        message = "Specify the sport"
    update.message.reply_text(
        message,
        reply_markup=main_keyboard()
    )

def find_teammate(update, context):
    print('Вызван /discgolf')
    update.message.reply_text(f'Ищу тебе партнеров по диск-гольфу!')

def main():
    mybot = Updater(config.API_KEY, use_context=True, request_kwargs=config.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("sport", sport_type))
    dp.add_handler(MessageHandler(Filters.regex('^(Discgolf)$'), find_teammate))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
