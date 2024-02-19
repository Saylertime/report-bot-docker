from loader import bot
from utils.sheets import brief_is_free

@bot.message_handler(commands=['free_texts'])
def free_texts(message):
    free_authors = brief_is_free()
    msg = f'Сейчас свободны: \n\n' \
          f'{free_authors}'

    bot.send_message(message.from_user.id, msg)