from .database_pattern import DataBase


class Language(DataBase):
    def __init__(self, user_id: int):
        super().__init__(user_id, name_database='language', name_table='users')

    def _create_table(self):
        with self._connect:
            self._cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self._name_table}(
                user_id INTEGER,
                language TEXT DEFAULT 'en'
            )""")

    @property
    def value(self):
        with self._connect:
            value = self._cursor.execute("""SELECT language FROM users WHERE user_id=?""", (self._user_id,))
        return value.fetchone()[0]

    def change(self, value: str):
        with self._connect:
            self._cursor.execute(f"""UPDATE users SET language=? WHERE user_id={self._user_id}""", (value,))
