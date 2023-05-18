"""
https://www.dappuniversity.com/articles/web3-py-intro
https://www.youtube.com/watch?v=cFB1BGeCpn0
https://app.infura.io/dashboard
"""
import os


from web3 import Web3

from dotenv import load_dotenv
load_dotenv()


class MetaMask:
    # host = 'https://api.binance.com'

    # Fill in your infura API key here
    infura_url = "https://mainnet.infura.io/v3/"
    Avalanche_C_Chain = 'https://avalanche-mainnet.infura.io/v3/'

    def __init__(self):
        self.infura_api_key = os.environ.get('INFURA_API_KEY')
        self.wallet = os.environ.get('WALLET_ADDRESS')
        self.web3_eth = Web3(Web3.HTTPProvider(self.infura_url + self.infura_api_key))
        self.web3_avalanche = Web3(Web3.HTTPProvider(self.Avalanche_C_Chain + self.infura_api_key))


    def check_connect(self):
        print(self.web3_eth.is_connected())
        return self.web3_eth.is_connected()

    def get_block_numer(self):
        print(self.web3_eth.eth.block_number)
        return self.web3_eth.eth.block_number

    def get_balance(self):
        # Fill in your account here
        balance = self.web3_eth.eth.get_balance(self.wallet)
        print(self.web3_eth.from_wei(balance, "ether"))
        print(self.web3_eth.)
        return self.web3_eth.from_wei(balance, "ether")

    def get_balance_avalanche(self):
        # Fill in your account here
        balance = self.web3_avalanche.eth.get_balance(self.wallet)
        print(self.web3_avalanche.from_wei(balance, "ether"))
        return self.web3_avalanche.from_wei(balance, "ether")



if __name__ == '__main__':
    r = MetaMask()
    # r.check_connect()
    # r.get_block_numer()
    r.get_balance()

    r.get_balance_avalanche()
