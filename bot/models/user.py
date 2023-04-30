from . import wallet
from . import user_language
from . import categories


class User:
    def __init__(self, user_id: int):
        self.wallet = wallet.Wallet(user_id)
        self.language = user_language.Language(user_id)
        self.buying_category = categories.BuyingCategory(user_id)
