import os
from datetime import datetime
import urllib.parse
import requests

from MexcClient.Utils.Signature import generate_signature

from dotenv import load_dotenv

load_dotenv()

from pybit.unified_trading import HTTP


class ExBybit:
    """"""

    def __init__(self):
        self.apiKey = os.environ.get('BYBIT_API_KEY')
        self.apiSecret = os.environ.get('BYBIT_API_SECRET_KEY')
        self.session = HTTP(testnet=False, api_key=self.apiKey, api_secret=self.apiSecret)

    def get_account(self):
        """"""
        return self.session.get_spot_asset_info()
        # return self.session.get_wallet_balance(accountType="SPOT")

    def get_account_margin(self):
        """"""
        return self.session.get_wallet_balance(accountType="CONTRACT")


if __name__ == '__main__':
    c = ExBybit()
    currencies = c.get_account()
    currencies = currencies['result']['spot']['assets']
    for symbol in currencies:
        print(f"{symbol['coin']} = {float(symbol['free']) + float(symbol['frozen'])}")

    currencies = c.get_account_margin()
    currencies = currencies['result']['list']
    # print(len(currencies), currencies[0])
    for symbol in currencies[0]['coin']:
        print(f"{symbol['coin']} = {float(symbol['equity'])},"
              f" (walletBalance={symbol['walletBalance']} + unrealisedPnl={symbol['unrealisedPnl']})")
