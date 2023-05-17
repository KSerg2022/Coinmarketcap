""""""

from .ex_lbank import ExLbank
from .ex_mexc import ExMexc
from .ex_gateio import ExGate
from .ex_bybit import ExBybit
from .ex_okx import ExOkx
from .ex_binance import ExBinance


class DataFromExchangers:
    """"""
    def __init__(self):
        self.currencies = []
        self.exchangers = [ExLbank().get_account,
                           ExMexc().get_account,
                           ExGate().get_account,
                           ExBybit().get_account,
                           ExOkx().get_account,
                           ExBinance().get_account
                           ]

    def get_data_from_exchangers(self):
        for exchanger in self.exchangers:
            self.currencies.append(exchanger())
        return self.currencies


if __name__ == '__main__':
    c = DataFromExchangers()
    r = c.get_data_from_exchangers()
    print(len(r), r)
