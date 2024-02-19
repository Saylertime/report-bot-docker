from loader import bot
from utils.sheets import stats_for_month


@bot.message_handler(commands=['stats_month'])
def stats_month(message):
    msg = stats_for_month('Январь 2024')
    bot.send_message(message.from_user.id, msg)
