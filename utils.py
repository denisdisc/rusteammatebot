from emoji import emojize
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton
import config


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(config.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def main_keyboard():
    return ReplyKeyboardMarkup([['Discgolf', 'Ultimate'], [ 'Badminton' ], [KeyboardButton('Мои координаты', request_location=True)]])
