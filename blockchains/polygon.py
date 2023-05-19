"""
https://polygonscan.com/
"""
import os

from blockchains.base import Base
from settings import POLYGON_CURRENCIES

blockchain = os.path.splitext(os.path.basename(__file__))[0]


class Polygon(Base):

    def __init__(self):
        super().__init__()
        self.host = 'https://api.polygonscan.com/api'
        self.api_key = os.environ.get('POLYGONSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = POLYGON_CURRENCIES

    def get_account(self) -> dict[dict]:
        currencies = self._get_account()
        return {blockchain: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    result = Polygon()
    # print(r.get_account_balance())

    res = result.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]
