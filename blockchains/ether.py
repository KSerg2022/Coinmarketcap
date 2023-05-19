"""
https://etherscan.io/
"""

import os

from blockchains.base import Base
from settings import ETHER_CURRENCIES

blockchain = os.path.splitext(os.path.basename(__file__))[0]


class Ether(Base):
    """"""

    def __init__(self):
        super().__init__()
        self.host = 'https://api.etherscan.io/api'
        self.api_key = os.environ.get('ETHERSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = ETHER_CURRENCIES

    def get_account(self) -> dict[dict]:
        currencies = self._get_account()
        return {blockchain: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    result = Ether()
    # print(r.get_account_balance())

    res = result.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]

