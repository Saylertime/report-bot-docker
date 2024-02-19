from pg_maker import all_authors
from loader import bot

@bot.message_handler(commands=['test'])
def test(message):
    msg = ''
    authors = all_authors()
    for author in authors:
        msg += f"{author[0]} — {author[1]}\n\n"
    print(authors)
    bot.send_message(message.from_user.id, msg)
