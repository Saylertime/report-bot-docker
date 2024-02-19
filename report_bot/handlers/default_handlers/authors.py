from loader import bot
from pg_maker import all_authors

@bot.message_handler(commands=['authors'])
def authors(message):
    msg = ''
    authors = all_authors()
    for author in authors:
        msg += f"{author[0]} — {author[1]}. В таблице: {author[2]}\n\n"
    print(authors)
    bot.send_message(message.from_user.id, msg)
