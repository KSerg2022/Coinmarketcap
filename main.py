""""""
import os

from dotenv import load_dotenv

from get_data_one_by_one import parse_cryptocurrencies_data, get_cryptocurrency
from get_data_by_several_ import get_cryptocurrency_by_several, parse_cryptocurrencies_data_by_several
from json_file import wright_to_json, load_data_from_file
from xlsx_file import create_xlsx_file
from csv_file import create_csv_file

load_dotenv()


def main(api_cmc: str):
    """"""
    # for query one by one
    # get info from coinmarketcap for cryptocurrencies for query one by one
    cryptocurrencies_data = get_cryptocurrency(api_cmc)

    # for query by several
    # get info from coinmarketcap for cryptocurrencies for query by several
    # cryptocurrencies_data = get_cryptocurrency_by_several(api_cmc)

    # dump all data to json file
    wright_to_json(cryptocurrencies_data)

    # load all data from json file
    # cryptocurrencies_data = load_data_from_file()

    # for query one by one
    # parse all data for using for query one by one
    cryptocurrencies_data = parse_cryptocurrencies_data(cryptocurrencies_data)

    # for query by several
    # parse all data for using for query by several
    # cryptocurrencies_data = parse_cryptocurrencies_data_by_several(cryptocurrencies_data)

    # dump data to xlsx file
    create_xlsx_file(cryptocurrencies_data)

    # dump data to csv file
    create_csv_file(cryptocurrencies_data)


if __name__ == '__main__':
    api_cmc = os.environ.get('API_COINMARCETCAP')
    main(api_cmc)
