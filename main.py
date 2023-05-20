"""Only data from coinmarketcap.com"""

from cmc.cmc import Cmc
from handlers.json_file import JsonFile
from handlers.xlsx_file import XlsxFileOnlyCmc
from handlers.csv_file import CsvFileOnlyCmc

from dotenv import load_dotenv
load_dotenv()


def main():
    """"""
    cmc = Cmc()
    json = JsonFile()

    # get info from coinmarketcap for cryptocurrencies
    cryptocurrencies_data = cmc.get_cryptocurrency()

    # dump all data to json file
    json.wright_to_json_cmc_data(cryptocurrencies_data)

    # load all data from json file
    cryptocurrencies_data = json.load_cmc_data_from_file()

    # parse all data for using
    cryptocurrencies_data = cmc.parse_cryptocurrencies(cryptocurrencies_data)

    # dump data to xlsx file
    XlsxFileOnlyCmc().create_xlsx(cryptocurrencies_data)

    # dump data to csv file
    # CsvFileOnlyCmc().create_csv_file(cryptocurrencies_data)


if __name__ == '__main__':
    main()
