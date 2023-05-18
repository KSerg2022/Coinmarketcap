"""

"""
import os
from blockchains.base import Base


from dotenv import load_dotenv

load_dotenv()


class Fantom(Base):

    def __init__(self):
        super().__init__()
        self.host = 'https://api.ftmscan.com/api'
        self.api_key = os.environ.get('FTMSCAN_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.currencies = {
            'FTM': '0xad29abb318791d579433d831ed122afeaf29dcfe',
            'MCRT': '0xE705aF5f63fcaBDCDF5016aA838EAaac35D12890',
            'BRO': '0x230576a0455d7Ae33c6dEfE64182C0BB68bAFAF3',
            'Escrow': '0xE613a914bbb433855378183c3aB13003285da40A',
            'FS': '0xC758295Cd1A564cdb020a78a681a838CF8e0627D',
            'SAVG': '0xa097c96ACc9587D140AD8aEaAC13D9db2C6CC07f',
            'WIS': '0xF24be6c063Bee7c7844dD90a21fdf7d783d41a94',
        }

    def get_account(self):
        currencies = self.get_available_currencies()
        return {os.path.splitext(os.path.basename(__file__))[0]: sorted(currencies, key=lambda x: x['coin'])}


if __name__ == '__main__':
    r = Fantom()
    # print(r.get_account_balance())

    res = r.get_account()
    print(res)
    [print(i) for i in list(res.values())[0]]

