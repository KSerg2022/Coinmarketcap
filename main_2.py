""""""

from copy import deepcopy

from cmc.cmc import Cmc
from exchanges.exchangers import DataFromExchangers

from handlers.json_file import JsonFile
from handlers.xlsx_file import XlsxFile
from handlers.csv_file import CsvFile


class Main:
    """"""

    def __init__(self):
        self.cmc = Cmc()
        self.json = JsonFile()
        self.xlsx = XlsxFile()
        self.exchangers = DataFromExchangers()

    def get_data_from_cmc(self):
        ## get info from coinmarketcap for cryptocurrencies
        cryptocurrencies_data = self.cmc.get_cryptocurrency()

        ## dump all data to json file
        self.json.wright_to_json_cmc_data(cryptocurrencies_data)

        ## load all data from json file
        cryptocurrencies_data = self.json.load_cmc_data_from_file()

        ## parse all data for using
        cryptocurrencies_data = self.cmc.parse_cryptocurrencies(cryptocurrencies_data)

        return cryptocurrencies_data

    def get_data_from_exchangers(self):
        ## get info from exchangers for cryptocurrencies
        exchangers_data = self.exchangers.get_data_from_exchangers()

        ## dump all data to json file
        self.json.wright_to_json_exchangers_data(exchangers_data)

        ## load all data from json file
        exchangers_data = self.json.load_exchangers_data_from_file()

        return exchangers_data

    @staticmethod
    def get_aggregation_data(data_from_cmc, data_from_exchangers):
        """"""
        time_data = set()
        print(data_from_cmc)

        aggregation_data = deepcopy(data_from_exchangers)
        for exchanger in aggregation_data:
            for currency in list(exchanger.values())[0]:
                try:
                    currency.update(data_from_cmc[currency['coin']])
                    currency.update({'total': float(currency['bal']) * float(currency['price'])})
                    time_data.add(currency['coin'])
                except KeyError:
                    currency.update({'data': '---', 'id': '---', 'name': '---', 'price': 0, 'total': 0})

        w = []
        for symbol, value in data_from_cmc.items():
            if symbol in time_data:
                continue
            else:
                w.append({'coin': symbol,
                          'bal': 0,
                          'data': value['data'],
                          'id': value['id'],
                          'name': value['name'],
                          'price': value['price'],
                          'total': 0
                          })

        aggregation_data.append({'others': w})

        return aggregation_data


def main():
    """"""
    main = Main()
    data_from_cmc = main.get_data_from_cmc()
    data_from_exchangers = main.get_data_from_exchangers()

    aggregation_data = main.get_aggregation_data(data_from_cmc, data_from_exchangers)
    # print(aggregation_data)
    # [print(i) for i in aggregation_data]

    XlsxFile().create_xlsx(aggregation_data)

    # CsvFile().create_csv_file(aggregation_data)


if __name__ == '__main__':
    main()
