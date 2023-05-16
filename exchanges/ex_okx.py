import os

from collections import defaultdict
from dotenv import load_dotenv
load_dotenv()

import okx.Account as Account
import okx.Funding as Funding


class ExOkx:
    host = "https://www.okx.com"

    def __init__(self):
        self.api_key = os.environ.get('OKX_API_KEY')
        self.api_secret = os.environ.get('OKX_API_SECRET_KEY')
        self.passphrase = os.environ.get('OKX_PWD')
        self.params = {'api_key': self.api_key,
                       'api_secret_key': self.api_secret,
                       'passphrase': self.passphrase,
                       'domain': self.host,
                       'use_server_time': False,
                       'flag': '0'}

        self.account = Account.AccountAPI(**self.params)
        self.funding = Funding.FundingAPI(**self.params)

    def get_funding(self):
        """"""
        return self.funding.get_balances()

    def get_account_trading(self):
        """"""
        return self.account.get_account_balance()

    def get_account(self):
        """"""
        currencies_trading = self.get_account_trading()
        currencies_funding = self.get_funding()
        currencies = self._normalize_data(currencies_trading,
                                          currencies_funding)
        return currencies

    @staticmethod
    def _normalize_data(currencies_trading, currencies_funding):
        """"""
        q = defaultdict(list)
        for symbol in currencies_trading['data'][0]['details']:
            q[symbol['ccy']].append(float(symbol['eq']))

        for symbol in currencies_funding['data']:
            if symbol['ccy'] in q:
                q[symbol['ccy']] = [q[symbol['ccy']][0] + float(symbol['bal'])]
            else:
                q[symbol['ccy']].append(float(symbol['bal']))

        currencies = []
        for currency, value in q.items():
            currencies.append({
                'coin': currency,
                'bal': value[0]
            })
        return {os.path.splitext(os.path.basename(__file__))[0][3:]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    currencies = ExOkx()
    data = currencies.get_account()
    print(data)

