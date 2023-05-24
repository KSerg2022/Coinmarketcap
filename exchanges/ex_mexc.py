import os
import requests
import urllib.parse

from datetime import datetime
from requests.exceptions import RequestException
from MexcClient.Utils.Signature import generate_signature

from dotenv import load_dotenv

load_dotenv()


class ExMexc:
    """"""
    host = "https://api.mexc.com"
    prefix = "/api/v3/"

    def __init__(self):
        self.apiKey = os.environ.get('MEXC_API_KEY')
        self.apiSecret = os.environ.get('MEXC_API_SECRET_KEY')
        self.headers = {"X-MEXC-APIKEY": self.apiKey, "Content-Type": "application/json"}
        self.exchanger = os.path.splitext(os.path.basename(__file__))[0][3:]

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
        try:
            r = requests.request('GET', self.host + self.prefix + url, headers=self.headers, params=sign_params)
            return r.json()
        except RequestException as e:
            print(f'{self.exchanger.upper()} -- {e}')
            return {}

    def _normalize_data(self, currencies_account):
        """"""
        if not currencies_account:
            return {self.exchanger: currencies_account}

        currencies = []
        for symbol in currencies_account['balances']:
            currencies.append({
                'coin': symbol['asset'].upper(),
                'bal': float(symbol['free']) + float(symbol['locked'])
            })
        return {self.exchanger: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    currencies = ExMexc()
    result = currencies.get_account()
    print(result)

