
from utils import get_smile, main_keyboard
from random import choice
from db import db, get_or_create_user
 

def greet_user(update, context):
    print('Вызван /start')
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Привет! {context.user_data["emoji"]} Найди партнера(ов) для игры с помощю команды /sport')

def talk_to_me(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
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

def user_coordinates(update, context):
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords}!",
        reply_markup=main_keyboard()
    )
