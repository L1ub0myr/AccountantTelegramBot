from database_pattern import DataBase


class BuyingCategory(DataBase):
    def __init__(self, user_id: int):
        super().__init__(user_id=user_id, name_database='categories', name_table='users')

    def _create_table(self):
        with self._connect:
            self._cursor.execute(f"""CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER,
                food REAL DEFAULT 0.0,
                utilities REAL DEFAULT 0.0,
                transport REAL DEFAULT 0.0,
                clothes REAL DEFAULT 0.0,
                health REAL DEFAULT 0.0,
                personal_care REAL DEFAULT 0.0,
                other REAL DEFAULT 0.0
            )""")

    def get_money_from_category(self, category: str):
        with self._connect:
            self._cursor.execute(f"""SELECT {category} FROM users WHERE user_id=?""", (self._user_id,))
            categories = self._cursor.fetchone()
        return categories[0]

    def get_all_categories(self):
        result = {}
        categories = ('food', 'utilities', 'transport', 'clothes', 'health', 'personal_care', 'other')
        for category in categories:
            result[category] = self.get_money_from_category(category)
        return result

    def add_money_for_category(self, value: int, category: str):
        value += self.get_money_from_category(category)
        with self._connect:
            self._cursor.execute(f"""UPDATE users SET {category}=? WHERE user_id=?""", (value, self._user_id))

    def clean_all_categories(self):
        with self._connect:
            self._cursor.execute("""
            UPDATE users SET food=?, utilities=?, transport=?, clothes=?, health=?, personal_care=?, other=? WHERE user_id=?
            """, (0, 0, 0, 0, 0, 0, 0, self._user_id))
