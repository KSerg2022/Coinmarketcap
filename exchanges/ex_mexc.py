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
        currencies = self._get_request(url)
        # print(currencies)

        return sorted(currencies['balances'], key=lambda x: x['asset'])

    def _get_request(self, url):
        """"""
        sign_params = self.gen_sign()
        r = requests.request('GET', self.host + self.prefix + url, headers=self.headers, params=sign_params)
        return r.json()


if __name__ == '__main__':
    currencies = ExMexc()

    for symbol in currencies.get_account():
        print(f"{symbol['asset']} = {float(symbol['free']) + float(symbol['locked'])}")



