from loader import bot
from states.overall import OverallState
from utils.sheets import rep_name_and_month

@bot.message_handler(commands=['history'])
def history(message):
    bot.send_message(message.from_user.id, "Введи имя автора 'Январь 2024'")
    bot.set_state(message.from_user.id, state=OverallState.name)


@bot.message_handler(state=OverallState.name)
def answer(message):
    msg = rep_name_and_month(name=message.text)
    bot.send_message(message.from_user.id, msg)
    bot.delete_state(message.from_user.id)
