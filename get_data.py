""""""
import time

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dateutil import parser


def get_cryptocurrency(api_cmc, symbols):
    """"""
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Latest quotes

    cryptocurrencies = []
    for symbol in symbols:
        parameters = {
            'symbol': symbol,
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
            print('error ----- ', symbol, message)
            raise RuntimeError(message)
        data = {
            symbol: response.json()
        }
        cryptocurrencies.append(data)
        time.sleep(2)

    return cryptocurrencies


def parse_cryptocurrencies_data(currencies_data: dict):
    """Parse weather data"""
    currencies = {}
    for currency_ in currencies_data:
        currency_symbol = list(currency_.keys())[0]
        currency_data = list(currency_.values())[0]
        date = currency_data['status']['timestamp']

        try:
            currency_data['data'][currency_symbol]
        except KeyError:
            id, name, symbol, price = [None]*4

            # additional data
            circulating_supply, total_supply, market_cap, fully_diluted_market_cap = [None] * 4
        else:
            id = currency_data['data'][currency_symbol]['id']
            name = currency_data['data'][currency_symbol]['name']
            symbol = currency_data['data'][currency_symbol]['symbol']
            price = currency_data['data'][currency_symbol]['quote']['USD']['price']

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

        currencies[currency_symbol] = data
    return dict(sorted(currencies.items()))
