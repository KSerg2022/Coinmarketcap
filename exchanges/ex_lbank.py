"""https://github.com/LBank-exchange/lbank-python-api/blob/master/LBank/rest.py"""
import os

from LBank import LBankAPI

from dotenv import load_dotenv
load_dotenv()


class ExLbank:
    """"""

    def __init__(self):
        self.api_key = os.environ.get('LBANK_API_KEY')
        self.private_key = os.environ.get('LBANK_API_SECRET_KEY')
        self.api = LBankAPI(self.api_key, self.private_key)

    def get_account(self):
        assets = self.api.user_assets()
        # print(assets.keys())
        # print(assets['info']['toBtc'])
        return assets['info']['toBtc']


if __name__ == '__main__':
    currencies = ExLbank()
    for symbol, value in currencies.get_account().items():
        # print(symbol, value)
        if float(value) != 0:
            print(f"{symbol} = {value}")
