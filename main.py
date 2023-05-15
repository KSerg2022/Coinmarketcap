""""""
import os

from dotenv import load_dotenv

from get_data import get_cryptocurrency, parse_cryptocurrencies

from json_file import wright_to_json, load_data_from_file
from xlsx_file import create_xlsx
from csv_file import create_csv_file

load_dotenv()


def main(api_cmc: str):
    """"""
    # get info from coinmarketcap for cryptocurrencies
    cryptocurrencies_data = get_cryptocurrency(api_cmc)

    # dump all data to json file
    wright_to_json(cryptocurrencies_data)

    # load all data from json file
    # cryptocurrencies_data = load_data_from_file()

    # parse all data for using
    cryptocurrencies_data = parse_cryptocurrencies(cryptocurrencies_data)

    # dump data to xlsx file
    create_xlsx(cryptocurrencies_data)

    # dump data to csv file
    # create_csv_file(cryptocurrencies_data)


if __name__ == '__main__':
    api_cmc = os.environ.get('API_COINMARCETCAP')
    main(api_cmc)
