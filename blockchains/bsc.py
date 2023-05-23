"""
https://bscscan.com/
"""
import os

from blockchains.base import Base
from settings import BSC_CURRENCIES


class Bsc(Base):
    """"""

    def __init__(self):
        super().__init__()
        self.host = 'https://api.bscscan.com/api'
        self.api_key = os.environ.get('BSCSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = BSC_CURRENCIES
        self.params = {'module': 'account',
                       'action': 'tokenbalance',
                       'contractaddress': '',
                       'address': self.wallet,
                       'tag': 'latest',
                       'apikey': self.api_key,
                       }
        self.blockchain = os.path.splitext(os.path.basename(__file__))[0]


if __name__ == '__main__':
    result = Bsc()
    # print(r.get_account_balance())

    res = result.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]
