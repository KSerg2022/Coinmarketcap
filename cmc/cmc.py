""""""
import os

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dateutil import parser

from settings import (currencies_symbols,
                      additional_currencies_symbols,
                      currencies_symbols_spec)


class Cmc:
    """"""

    def __init__(self):
        self.symbols = self.normalize_data(currencies_symbols) \
                  + self.normalize_data(additional_currencies_symbols) \
                  + currencies_symbols_spec
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Latest quotes
        self.api_cmc = os.environ.get('API_COINMARCETCAP')

    def get_cryptocurrency(self: str) -> dict[dict]:
        """"""
        symbols = ','.join(self.symbols)

        parameters = {
            'symbol': symbols,
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_cmc,
        }
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(self.url, params=parameters)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            message = f'openweathermap.org returned non-200 code. Actual code is: {response.status_code},' \
                      f' message is: {response.json()["status"]["error_message"]}'
            print('error ----- ', message)
            raise RuntimeError(message)

        session.close()
        return response.json()

    def parse_cryptocurrencies(self, currencies_data: dict[dict]) -> dict[dict[str, dict]]:
        """Parse weather data"""
        currencies = {}
        for symbol in self.symbols:
            result = self.parse_cryptocurrencies_data(currencies_data, symbol)
            if not result:
                continue
            else:
                if symbol == 'MIOTA':
                    symbol = 'IOTA'
                currencies[symbol.upper()] = result
        return dict(sorted(currencies.items()))

    def parse_cryptocurrencies_data(self, currencies_data: dict[dict], symbol: str) -> dict[str, str]:
        """Parse data"""
        try:
            date = currencies_data['status']['timestamp']
        except KeyError:
            return {}

        try:
            currencies_data['data'][symbol]
        except KeyError:
            data = self.fill_values_if_is_not_symbol(date, symbol)
            return data

        id = currencies_data['data'][symbol]['id']
        name = currencies_data['data'][symbol]['name']
        symbol = currencies_data['data'][symbol]['symbol']
        price = currencies_data['data'][symbol]['quote']['USD']['price']

        # additional data
        # circulating_supply = currency_data['data'][currency_symbol]['circulating_supply']
        # total_supply = currency_data['data'][currency_symbol]['total_supply']
        # market_cap = currency_data['data'][currency_symbol]['quote']['USD']['market_cap']
        # fully_diluted_market_cap = currency_data['data'][currency_symbol]['quote']['USD']['fully_diluted_market_cap']

        data = {
            'data': parser.isoparse(date).strftime("%d-%m-%Y %H:%M:%S"),
            'id': id,
            'name': name,
            'coin': symbol.upper(),
            'price': price,

            # additional data
            # 'circulating_supply': circulating_supply,
            # 'total_supply': total_supply,
            # 'market_cap': market_cap,
            # 'fully_diluted_market_cap': fully_diluted_market_cap,
        }
        return data

    @staticmethod
    def fill_values_if_is_not_symbol(date: str, symbol: str) -> dict[str, str]:
        """"""
        result = {
            'data': parser.isoparse(date).strftime("%d-%m-%Y %H:%M:%S"),
            'id': 'not in CMC',
            'name': '---',
            'coin': symbol.upper(),
            'price': 0,

            # additional data
            # 'circulating_supply': '---',
            # 'total_supply': '---',
            # 'market_cap': '---',
            # 'fully_diluted_market_cap': '---',
        }
        return result

    @staticmethod
    def normalize_data(data: list[str]) -> list[str]:
        return [value.upper() for value in data]