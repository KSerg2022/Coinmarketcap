"""
https://dev.binance.vision/t/ip-whitelist-does-not-have-effect/2767
https://algotrading101.com/learn/binance-python-api-guide/
"""
import os
import json

from dotenv import load_dotenv

load_dotenv()

# from binance.spot import Spot
from binance.client import Client
from binance.exceptions import BinanceAPIException

from settings import base_dir, time_stamp


class ExBinance:
    host = 'https://api.binance.com'

    def __init__(self):
        self.api_key = os.environ.get('BINANCE_API_KEY')
        self.api_secret = os.environ.get('BINANCE_API_SECRET_KEY')

        self.coin_m = Client(api_key=self.api_key, api_secret=self.api_secret)

    def get_futures_coin_account(self):
        futures_coin_account = self._get_response(self.coin_m.futures_coin_account)
        if not futures_coin_account:
            return futures_coin_account
        return [x for x in futures_coin_account['assets'] if float(x['walletBalance']) != 0]

    def get_spot_account(self) -> list[dict]:
        spot_account = self._get_response(self.coin_m.get_account)
        if not spot_account:
            return spot_account
        return [x for x in spot_account['balances'] if float(x['free']) != 0 or float(x['locked']) != 0]

    def _get_response(self, fn) -> dict | list:
        try:
            response = fn()
        except BinanceAPIException as e:
            print(f'{os.path.splitext(os.path.basename(__file__))[0][3:].upper()} -- {e}')
            return []
        return response

    def get_account(self):
        spot_account = self.get_spot_account()
        futures_coin_account = self.get_futures_coin_account()
        currencies = self._normalize_data(spot_account,
                                          futures_coin_account)

        return currencies

    @staticmethod
    def _normalize_data(spot_account, futures_coin_account):
        """"""
        currencies = []
        for symbol in spot_account + futures_coin_account:
            if y := [x for x in currencies if x['coin'] == symbol['asset']]:
                try:
                    q = symbol['free'] + symbol['locked']
                except KeyError:
                    q = symbol['marginBalance']
                currencies[currencies.index(y[0])] = {'coin': symbol['asset'],
                                                      'bal': y[0]['bal'] + float(q)}
            else:
                try:
                    currencies.append({
                        'coin': symbol['asset'],
                        'bal': float(symbol['free']) + float(symbol['locked'])
                    })
                except KeyError:
                    currencies.append({
                        'coin': symbol['asset'],
                        'bal': float(symbol['marginBalance'])
                    })
        return {os.path.splitext(os.path.basename(__file__))[0][3:]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    r = ExBinance()
    result = r.get_account()
    print(result)
