from loader import bot
from utils.sheets import who_is_free

@bot.message_handler(commands=['free_authors'])
def free_authors(message):
    free_authors = who_is_free()
    msg = 'Сейчас свободны: \n\n'
    for author in free_authors:
        msg += f"{author[1]} — {author[0]}\n"
    bot.send_message(message.from_user.id, msg)



    # busy_authors, free_authors = who_is_free()
    # msg = 'Сейчас свободны: \n\n'
    # for author in free_authors:
    #     msg += f"{author}\n"
    # bot.send_message(message.from_user.id, msg)

    # msg2 = '\n\nИ заняты: \n\n'
    # for author in busy_authors:
    #     msg2 += f"{author}\n"
    # bot.send_message(message.from_user.id, msg2)
