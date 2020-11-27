from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard


def form_start(update, context):
    update.message.reply_text(
        "What is your name? (including last name)",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"

def user_name(update, context):
    name = update.message.text
    if len(name.split()) != 2:
        update.message.reply_text("Please, typing First and Last name")
        return "name"
    else:
        context.user_data["anketa"] = {"name": name}
        reply_keyboard = [["1", "2", "3", "4", "5"]]
        update.message.reply_text(
            "Оцените бота шкале от 1 до 5",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return "rating"

def bot_rating(update, context):
    context.user_data["anketa"]["rating"] = int(update.message.text)

    update.message.reply_text(
        "Оставьте комментарий в свободной форме или пропустите этот шаг, введя /skip"
    )
    return "comment"

def anketa_comment(update, context):
    context.user_data["anketa"]["comment"] = update.message.text
    user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
    <b>Оценка:</b> {context.user_data['anketa']['rating']}
    <b>Комментарий:</b> {context.user_data['anketa']['comment']}"""

    update.message.reply_text(user_text, reply_markup=main_keyboard(),
                                parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_skip(update, context):
    user_text = anketa_format(context.user_data["anketa"])
    update.message.reply_text(user_text, reply_markup=main_keyboard(),
                                parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_format(user_anketa):
    user_text = anketa_format(context.user_data["anketa"])
    if user_anketa.get('comment'):
        user_text += f"<b>Комментарий:</b> {user_anketa['comment']}"
 
    return user_text

def anketa_dontknow(update, context):
    update.message.reply_text("Не понимаю")
