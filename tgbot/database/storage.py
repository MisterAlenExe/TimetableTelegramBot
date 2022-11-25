import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect(r"tgbot/database/data.db")
        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users_notify(user_id INTEGER, user_name TEXT)")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.db.commit()
        self.db.close()

    def get_users_notify(self):
        users = self.cur.execute("SELECT * FROM users_notify").fetchall()
        users = dict(users)
        return users

    def add_user_notify(self, user_id, user_name):
        self.cur.execute("INSERT INTO users_notify VALUES (?, ?)", (user_id, user_name))

    def delete_user_notify(self, user_id):
        self.cur.execute("DELETE FROM users_notify WHERE user_id=(?)", (user_id, ))
