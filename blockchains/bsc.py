"""
https://bscscan.com/
"""
import os

from blockchains.base import Base
from settings import BSC_CURRENCIES

blockchain = os.path.splitext(os.path.basename(__file__))[0]


class Bsc(Base):
    """"""

    def __init__(self):
        super().__init__()
        self.host = 'https://api.bscscan.com/api'
        self.api_key = os.environ.get('BSCSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = BSC_CURRENCIES

    def get_account(self) -> dict[dict]:
        currencies = self._get_account()
        return {blockchain: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    result = Bsc()
    # print(r.get_account_balance())

    res = result.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]