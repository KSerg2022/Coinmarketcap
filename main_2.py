""""""
import os

from copy import deepcopy

from get_data import get_cryptocurrency, parse_cryptocurrencies
from exchanges.exchangers import DataFromExchangers


from json_file import wright_to_json, load_data_from_file
# from xlsx_file import create_xlsx
# from csv_file import create_csv_file

from dotenv import load_dotenv
load_dotenv()


def get_data_from_cmc(api_cmc: str):
    ## get info from coinmarketcap for cryptocurrencies
    cryptocurrencies_data = get_cryptocurrency(api_cmc)

    ## dump all data to json file
    wright_to_json(cryptocurrencies_data)

    ## load all data from json file
    # cryptocurrencies_data = load_data_from_file()

    ## parse all data for using
    cryptocurrencies_data = parse_cryptocurrencies(cryptocurrencies_data)

    return cryptocurrencies_data


def get_data_from_exchangers():
    return DataFromExchangers().get_data_from_exchangers()


def get_aggregation_data(data_from_cmc, data_from_exchangers):
    """"""
    aggregation_data = deepcopy(data_from_exchangers)
    for exchanger in aggregation_data:
        for currency in list(exchanger.values())[0]:
            try:
                currency.update(data_from_cmc[currency['coin']])
            except KeyError:
                currency.update({'data': '---', 'id': '---', 'name': '---', 'price': 0})

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
    print(aggregation_data)

    create_xlsx(aggregation_data)

if __name__ == '__main__':
    api_cmc = os.environ.get('API_COINMARCETCAP')
    main(api_cmc)
