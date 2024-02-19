import psycopg2


def add_author(name, nickname, name_in_db, about='', phone=''):
    create_db()

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = f"INSERT INTO authors (name, nickname, name_in_db, about, phone) " \
          f"VALUES ('{name}', '{nickname}', '{name_in_db}', '{about}', '{phone}')"

    cursor.execute(sql)
    print(f"{nickname} добавлен")
    cursor.close()
    conn.close()

def all_authors():
    create_db()
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = "SELECT name, nickname, name_in_db FROM authors"

    cursor.execute(sql)
    authors = cursor.fetchall()
    cursor.close()
    conn.close()
    return authors


def create_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = 'CREATE TABLE IF NOT EXISTS authors (name VARCHAR, nickname VARCHAR, name_in_db VARCHAR, phone VARCHAR, about VARCHAR);'
    cursor.execute(sql)
    cursor.close()
    conn.close()

