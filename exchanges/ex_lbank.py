"""https://github.com/LBank-exchange/lbank-python-api/blob/master/LBank/rest.py"""
import os

from .LBank import LBankAPI

from dotenv import load_dotenv

load_dotenv()


class ExLbank:
    """"""

    def __init__(self):
        self.api_key = os.environ.get('LBANK_API_KEY')
        self.private_key = os.environ.get('LBANK_API_SECRET_KEY')
        self.api = LBankAPI(self.api_key, self.private_key)

    def get_account(self):
        """"""
        currencies_account = self.api.user_assets()
        currencies = self._normalize_data(currencies_account)
        return currencies

    @staticmethod
    def _normalize_data(currencies_account):
        """"""
        currencies = []
        for symbol, value in currencies_account['info']['toBtc'].items():
            if float(value) != 0:
                currencies.append({
                    'coin': symbol.upper(),
                    'bal': value
                })
        return {os.path.splitext(os.path.basename(__file__))[0][3:]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    currencies = ExLbank()
    r = currencies.get_account()
    print(r)