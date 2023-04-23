import sqlite3


class DataBase:
    def __init__(self, user_id: int, name_database: str, name_table: str):
        self.name_table = name_table
        self._connect = sqlite3.connect(f'files_database/{name_database}.db')
        self._cursor = self._connect.cursor()
        self._user_id = user_id
        self._create_table()
        if not self._check_user_exists():
            self._add_user()

    def _create_table(self):
        with self._connect:
            self._cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.name_table}(
                user_id INTEGER,
                balance REAL DEFAULT 0.0
            )""")

    def _check_user_exists(self):
        with self._connect:
            for i in self._cursor.execute(f"""SELECT user_id FROM {self.name_table}""").fetchall():
                if self._user_id in i:
                    return True
            return False

    def _add_user(self):
        with self._connect:
            self._cursor.execute(f"""INSERT INTO {self.name_table}(user_id) VALUES(?)""", (self._user_id,))
