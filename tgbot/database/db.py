import sqlite3


async def db_start():
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users_notify(user_id INTEGER, user_name TEXT)")
    db.commit()


async def db_get_users_notify():
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    users_notify = cur.execute("SELECT * FROM users_notify").fetchall()
    db.commit()
    users = []
    for user_id, _ in users_notify:
        users.append(user_id)
    return users


async def db_add_new_user_notify(user_id, user_name):
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    cur.execute("INSERT INTO users_notify VALUES (?, ?)", (user_id, user_name))
    db.commit()


async def db_delete_user_notify(user_id):
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    cur.execute("DELETE FROM users_notify WHERE user_id=(?)", (user_id,))
    db.commit()