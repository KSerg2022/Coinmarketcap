"""


"""
import os

from blockchains.base import Base

from dotenv import load_dotenv
load_dotenv()


class Polygon(Base):

    def __init__(self):
        super().__init__()
        self.host = 'https://api.polygonscan.com/api'
        self.api_key = os.environ.get('POLYGONSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')

        self.currencies = {
            'MATIC': '0x0000000000000000000000000000000000001010',
        }

    def get_account(self):
        currencies = self.get_available_currencies()
        return {os.path.splitext(os.path.basename(__file__))[0]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    r = Polygon()
    # print(r.get_account_balance())

    res = r.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]

