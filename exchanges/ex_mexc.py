import os
# import json
# import requests
# import time
# import hashlib
# import hmac

from dotenv import load_dotenv

load_dotenv()

from datetime import datetime
import urllib.parse

import requests

from MexcClient.Utils.Signature import generate_signature


class ExMexc:
    """"""
    host = "https://api.mexc.com"
    prefix = "/api/v3/"

    def __init__(self):
        self.apiKey = os.environ.get('MEXC_API_KEY')
        self.apiSecret = os.environ.get('MEXC_API_SECRET_KEY')
        self.headers = {"X-MEXC-APIKEY": self.apiKey, "Content-Type": "application/json"}

    def gen_sign(self):
        """"""
        params = {"timestamp": int(datetime.now().timestamp()) * 1000}
        str_params = urllib.parse.urlencode(params)
        signature = generate_signature(self.apiSecret.encode(), str_params.encode())
        params["signature"] = signature
        return params

    def get_account(self):
        """"""
        url = 'account'
        currencies_account = self._get_request(url)
        currencies = self._normalize_data(currencies_account)
        return currencies

    def _get_request(self, url):
        """"""
        sign_params = self.gen_sign()
        r = requests.request('GET', self.host + self.prefix + url, headers=self.headers, params=sign_params)
        return r.json()

    @staticmethod
    def _normalize_data(currencies_account):
        """"""
        currencies = []
        for symbol in currencies_account['balances']:
            currencies.append({
                'coin': symbol['asset'],
                'bal': float(symbol['free']) + float(symbol['locked'])
            })
        return {os.path.splitext(os.path.basename(__file__))[0][3:]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    currencies = ExMexc()
    currencies.get_account()

    # for symbol in currencies.get_account():
    #     print(f"{symbol['coin']} = {float(symbol['bal']) }")
