import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("authors", "Все авторы"),
    ("free_authors", "Свободные авторы"),
    ("free_texts", "Свободные брифы"),
    ("new_author", "Добавить автора"),
    ("money", "Гонорары за месяц"),
    ("test", "test"),
    ("stats_month", "Статистика по текстам за месяц"),
    ("history", "Инфа по отдельному автору"),
)
