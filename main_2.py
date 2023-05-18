""""""
import os

from copy import deepcopy

from get_data import get_cryptocurrency, parse_cryptocurrencies
from exchanges.exchangers import DataFromExchangers

from json_file import (wright_to_json_cmc_data, load_cmc_data_from_file,
                       wright_to_json_exchangers_data, load_exchangers_data_from_file)
# from xlsx_file import create_xlsx
# from csv_file import create_csv_file

from dotenv import load_dotenv

load_dotenv()


def get_data_from_cmc(api_cmc: str):
    ## get info from coinmarketcap for cryptocurrencies
    cryptocurrencies_data = get_cryptocurrency(api_cmc)

    ## dump all data to json file
    wright_to_json_cmc_data(cryptocurrencies_data)

    ## load all data from json file
    # cryptocurrencies_data = load_cmc_data_from_file()

    ## parse all data for using
    cryptocurrencies_data = parse_cryptocurrencies(cryptocurrencies_data)

    return cryptocurrencies_data


def get_data_from_exchangers():
    ## get info from exchangers for cryptocurrencies
    exchangers_data = DataFromExchangers().get_data_from_exchangers()

    ## dump all data to json file
    wright_to_json_exchangers_data(exchangers_data)

    ## load all data from json file
    # exchangers_data = load_exchangers_data_from_file()

    return exchangers_data


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


import pandas as pd

from settings import base_dir, time_stamp


def create_table(data: list[dict]):
    table = []
    headers_lines = []
    for exchanger in data:
        for currency in list(exchanger.values())[0]:
            row = list(currency.values())
            table.append(row)

            headers_lines.append(list(exchanger.keys())[0])
    headers_columns = list(list(data[0].values())[0][0].keys())
    return table, headers_lines, headers_columns


def create_xlsx_file(table: list[list], line_index: list[dict], columns: list[str]):
    """"""
    path_to_file = base_dir / 'xlsx_files' / f'data_{time_stamp}.xlsx'

    df = pd.DataFrame(table, index=line_index, columns=columns)
    df.to_excel(path_to_file, sheet_name='Sheet1', startrow=0, startcol=0)


def create_xlsx(data: dict[dict]):
    table, headers_lines, headers_columns = create_table(data)
    create_xlsx_file(table, headers_lines, headers_columns)


def main(api_cmc: str):
    """"""
    data_from_cmc = get_data_from_cmc(api_cmc)
    data_from_exchangers = get_data_from_exchangers()

    aggregation_data = get_aggregation_data(data_from_cmc, data_from_exchangers)
    # print(aggregation_data)

    create_xlsx(aggregation_data)


if __name__ == '__main__':
    api_cmc = os.environ.get('API_COINMARCETCAP')
    main(api_cmc)
