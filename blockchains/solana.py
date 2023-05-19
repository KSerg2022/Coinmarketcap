"""
https://solscan.io/
"""
import os

from blockchains.base import Base
from settings import SOLANA_CURRENCIES

blockchain = os.path.splitext(os.path.basename(__file__))[0]


class Solana(Base):
    """"""

    def __init__(self):
        super().__init__()
        self.host = 'https://public-api.solscan.io/account/tokens'
        self.api_key = os.environ.get('SOLANA_API_KEY')
        self.wallet = os.environ.get('WALLET_SOLANA')
        self.currencies = SOLANA_CURRENCIES

    def get_account(self) -> dict[dict]:
        """"""
        headers = {
            'accept': 'application/json',
            'token': self.api_key,
        }
        params = {'account': self.wallet,
                  }
        response = self._get_request(self.host, params, headers)
        currencies = self._normalize_data(response)
        return {blockchain: sorted(currencies, key=lambda x: x['coin'])}

    def _normalize_data(self, currencies):
        results = []
        for currency in currencies:
            try:
                results.append({'coin': currency['tokenSymbol'],
                                'bal': int(currency['tokenAmount']['amount']) /
                                       10 ** currency['tokenAmount']['decimals']})
            except KeyError:
                if currency['tokenAddress'] in self.currencies.values():
                    for symbol, address in self.currencies.items():
                        if currency['tokenAddress'] == address:
                            results.append({'coin': symbol,
                                            'bal': int(currency['tokenAmount']['amount']) /
                                                   10 ** currency['tokenAmount']['decimals']})

        return results


if __name__ == '__main__':
    result = Solana()
    # print(r.get_account_balance())

    res = result.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]
