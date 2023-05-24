"""https://github.com/LBank-exchange/lbank-python-api/blob/master/LBank/rest.py"""
import os

from exchanges.handlers.LBank import LBankAPI
from exchanges.handlers.LBank import LBankError

from dotenv import load_dotenv

load_dotenv()


class ExLbank:
    """"""

    def __init__(self):
        self.api_key = os.environ.get('LBANK_API_KEY')
        self.private_key = os.environ.get('LBANK_API_SECRET_KEY')
        self.api = LBankAPI(self.api_key, self.private_key)
        self.exchanger = os.path.splitext(os.path.basename(__file__))[0][3:]

    def get_account(self):
        """"""
        try:
            currencies_account = self.api.user_assets()
        except LBankError as e:
            print(f'{self.exchanger.upper()} -- {e}')
            currencies_account = {}
        currencies = self._normalize_data(currencies_account)
        return currencies

    def _normalize_data(self, currencies_account):
        """"""
        if not currencies_account:
            return {self.exchanger: currencies_account}

        currencies = []
        for symbol, value in currencies_account['info']['toBtc'].items():
            if float(value) != 0:
                currencies.append({
                    'coin': symbol.upper(),
                    'bal': value
                })
        return {self.exchanger: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    currencies = ExLbank()
    r = currencies.get_account()
    print(r)