""""""
import os

from dotenv import load_dotenv

from settings import currencies_symbols, additional_currencies_symbols, currencies_symbols_spec
from get_data import parse_cryptocurrencies_data, get_cryptocurrency
from json_file import wright_to_json, load_data_from_file
from xlsx_file import create_xlsx_file
from csv_file import create_csv_file

load_dotenv()


def normalize_data(data: list[str]) -> list[str]:
    return [value.upper() for value in data]


def main(api_cmc: str):
    """"""
    # get list of symbol's cryptocurrencies
    cryptocurrencies = normalize_data(currencies_symbols)\
                       + normalize_data(additional_currencies_symbols)\
                       + currencies_symbols_spec

    # get info from coinmarketcap for cryptocurrencies
    cryptocurrencies_data = get_cryptocurrency(api_cmc, set(cryptocurrencies))

    # dump data to json file
    wright_to_json(cryptocurrencies_data)

    # load data from json file
    # cryptocurrencies_data = load_data_from_file()

    # parse data for using
    cryptocurrencies_data = parse_cryptocurrencies_data(cryptocurrencies_data)

    # dump data to xlsx file
    create_xlsx_file(cryptocurrencies_data)

    # dump data to csv file
    create_csv_file(cryptocurrencies_data)


if __name__ == '__main__':
    api_cmc = os.environ.get('API_COINMARCETCAP')
    main(api_cmc)
