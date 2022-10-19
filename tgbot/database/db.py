import sqlite3


async def db_start():
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users_notify(user_id INTEGER, user_name TEXT)")
    db.commit()


async def db_get_all_users_notify():
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    users_notify = cur.execute("SELECT * FROM users_notify").fetchall()
    return users_notify


async def db_add_new_user_notify(user_id, user_name):
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    cur.execute("INSERT INTO users_notify VALUES (?, ?)", (user_id, user_name))
    db.commit()