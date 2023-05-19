""""""

from exchanges.ex_lbank import ExLbank
from exchanges.ex_mexc import ExMexc
from exchanges.ex_gateio import ExGate
from exchanges.ex_bybit import ExBybit
from exchanges.ex_okx import ExOkx
from exchanges.ex_binance import ExBinance

from blockchains.bsc import Bsc
from blockchains.ether import Ether
from blockchains.fantom import Fantom
from blockchains.polygon import Polygon
from blockchains.solana import Solana


class DataFromExchangers:
    """"""

    def __init__(self):
        self.currencies = []
        self.exchangers = [
            ExLbank().get_account,
            ExMexc().get_account,
            ExGate().get_account,
            ExBybit().get_account,
            ExOkx().get_account,
            ExBinance().get_account,
            Bsc().get_account,
            Ether().get_account,
            Polygon().get_account,
            Fantom().get_account,
            Solana().get_account,
        ]

    def get_data_from_exchangers(self):
        """"""
        for exchanger in self.exchangers:
            self.currencies.append(exchanger())
        return self.currencies


if __name__ == '__main__':
    c = DataFromExchangers()
    r = c.get_data_from_exchangers()
    print(len(r), r)
