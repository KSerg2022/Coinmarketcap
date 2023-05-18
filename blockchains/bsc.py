"""
https://bscscan.com/

"""
import os
from blockchains.base import Base


from dotenv import load_dotenv

load_dotenv()


class Bsc(Base):
    host = 'https://api.bscscan.com/api'

    def __init__(self):
        super().__init__()
        self.host = 'https://api.bscscan.com/api'
        self.api_key = os.environ.get('BSCSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = {
            'BNB': '0xe9e7cea3dedca5984780bafc599bd69add087d56',
            'BSC-USD': '0x55d398326f99059fF775485246999027B3197955',
            'CAKE': '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82',
            'DIA': '0x99956D38059cf7bEDA96Ec91Aa7BB2477E0901DD',
            'ONT': '0xFd7B3A77848f1C2D67E05E54d78d174a0C850335',
            'LPOOL': '0xCfB24d3C3767364391340a2E6d99c64F1CBd7A3D',
            'MCRT': '0x4b8285aB433D8f69CB48d5Ad62b415ed1a221e4f',
            'PPAD': '0x93Bb13E90678cCd8BBab07D1dAEF15086746dc9B',
            'BUSD': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
            'GMI': '0x93D8d25E3C9A847a5Da79F79ecaC89461FEcA846',
            # 'GMI 2.0': '0xC5CF060cAEaC400Db05f796755576CE60FF7Baf1',
            'eKZEN': '0x455B75A6DCF86e700B020765DFbcbE7D4A3b73f5',
            'MATE': '0x696c2D3c711d5727c3686672F411583faeDAA29F',
            # 'ARTEM': '0x6450B164D763268Bf0A27C9E7f602e2b095b11cF',
            # 'ARTEM_': '0x6853F29b4261d7c291AcE06DeEb4de04FF4Ca3F0',
            # 'ARTEM.RWRD': '0xeB5eefbA6a2d01BC466328C0B9EC4e12106Fd76E',
        }

    def get_account(self):
        currencies = self.get_available_currencies()
        return {os.path.splitext(os.path.basename(__file__))[0]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    r = Bsc()
    # r.get_account_balance()

    res = r.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]
