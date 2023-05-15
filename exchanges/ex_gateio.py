import os
import json
import requests
import time
import hashlib
import hmac

from dotenv import load_dotenv

load_dotenv()


class ExGate:
    """"""

    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    query_param = ''

    def __init__(self):
        self.key = os.environ.get('GATE_API_KEY')  # api_key
        self.secret = os.environ.get('GATE_API_SECRET_KEY')  # api_secret

    def gen_sign(self, method, url, query_string=None, payload_string=None):
        """"""
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        # print('1 - ', s)
        sign = hmac.new(self.secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        # print('2 - ', sign)
        return {'KEY': self.key, 'Timestamp': str(t), 'SIGN': sign}

    def get_total_balance(self):
        """"""
        url = '/wallet/total_balance'
        return self._get_request(url)

    def get_accounts(self):
        """"""
        url = '/spot/accounts'
        currencies = self._get_request(url)
        # print(currencies)

        return sorted(currencies, key=lambda x: x['currency'])

    def _get_request(self, url):
        """"""
        sign_headers = self.gen_sign('GET', self.prefix + url, self.query_param)
        self.headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + url, headers=self.headers)
        # print(r.json())

        return r.json()


if __name__ == '__main__':
    currencies = ExGate()
    # print(currencies.get_total_balance())
    for symbol in currencies.get_accounts():
        print(f"{symbol['currency']} = {float(symbol['available']) + float(symbol['locked'])}")
