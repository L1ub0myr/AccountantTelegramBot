from database_pattern import DataBase


class Wallet(DataBase):
    def __init__(self, user_id: int):
        super().__init__(user_id=user_id, name_database='wallet', name_table='users')

    @property
    def balance(self):
        self._cursor.execute('''
                    SELECT balance FROM users WHERE user_id=?
                ''', (self._user_id,))
        row = self._cursor.fetchone()
        return row[0]

    def plus(self, value: float):
        with self._connect:
            self._cursor.execute("""UPDATE users SET balance=? WHERE user_id=?""",
                                  (self.balance + value, self._user_id))

    def minus(self, value: float):
        value = 0.0 if self.balance - value < 0 else self.balance - value
        with self._connect:
            self._cursor.execute("""UPDATE users SET balance=? WHERE user_id=?""", (value, self._user_id))

    def clean(self):
        with self._connect:
            self._cursor.execute("""UPDATE users SET balance=? WHERE user_id=?""", (0, self._user_id))
