""""""
import time

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dateutil import parser

from settings import (currencies_symbols_by_several,
                      additional_currencies_symbols_by_several,
                      currencies_symbols_spec_by_several)


def normalize_data(data: list[str]) -> list[str]:
    return [value.upper() for value in data]


symbols = normalize_data(currencies_symbols_by_several) \
         + normalize_data(additional_currencies_symbols_by_several) \
         + currencies_symbols_spec_by_several


def get_cryptocurrency_by_several(api_cmc: str) -> dict[dict]:
    """"""
    symbols_ = ','.join(symbols)
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Latest quotes

    parameters = {
        'symbol': symbols_,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_cmc,
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        message = f'openweathermap.org returned non-200 code. Actual code is: {response.status_code},' \
                  f' message is: {response.json()["status"]["error_message"]}'
        print('error ----- ', message)
        raise RuntimeError(message)

    return response.json()


def parse_cryptocurrencies_data_by_several(currencies_data: dict[dict]) -> dict[dict]:
    """Parse weather data"""
    date = currencies_data['status']['timestamp']

    currencies = {}
    for symbol in symbols:

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
            'symbol': symbol,
            'price': price,

            # additional data
            # 'circulating_supply': circulating_supply,
            # 'total_supply': total_supply,
            # 'market_cap': market_cap,
            # 'fully_diluted_market_cap': fully_diluted_market_cap,
        }

        currencies[symbol] = data
    return dict(sorted(currencies.items()))
