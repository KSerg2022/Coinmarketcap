"""

"""
import os
from blockchains.base import Base


from dotenv import load_dotenv

load_dotenv()


class Ether(Base):
    """"""

    def __init__(self):
        super().__init__()
        self.host = 'https://api.etherscan.io/api'
        self.api_key = os.environ.get('ETHERSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = {
            'ETH': '0x34a9c05b638020a07bb153bf624c8763bf8b4a86',
            'FTM': '0x4e15361fd6b4bb609fa63c81a2be19d873717870',
        }

    def get_account(self):
        currencies = self.get_available_currencies()
        return {os.path.splitext(os.path.basename(__file__))[0]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    r = Ether()
    # print(r.get_account_balance())

    res = r.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]

