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


async def db_admin_get_users():
    db = sqlite3.connect(r"tgbot/database/data.db")
    cur = db.cursor()
    users_notify = cur.execute("SELECT * FROM users_notify").fetchall()
    db.commit()
    user_ids = []
    user_names = []
    for user_id, user_name in users_notify:
        user_ids.append(user_id)
        user_names.append(user_name)
    return user_ids, user_names


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