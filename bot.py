from telebot import TeleBot, types
from config import token_key, chat_id
from sql import init_ticket


bot = TeleBot(token_key)


def send_ticket_bot(user,subj,msg):
    #keytab=types.InlineKeyboardMarkup()
    #keytab.add(types.InlineKeyboardButton(text="Взять заявку", callback_data=1))
    bot.send_message(chat_id ,f"Пользователь: {user}\nТему: {subj}\nСообщение: {msg}")#, reply_markup=keytab)
    return {'send'}