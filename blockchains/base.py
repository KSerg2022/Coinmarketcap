"""

"""

import requests
from requests.exceptions import RequestException

from dotenv import load_dotenv
load_dotenv()


class Base:
    """"""
    COIN = 'coin'
    BAL = 'bal'

    def __init__(self):
        self.host = ''
        self.api_key = ''
        self.wallet = ''
        self.currencies = {}
        self.params = {}

    def _get_account(self) -> list[dict]:
        """"""
        results = []
        for currency, contractaddress in self.currencies.items():
            self.params['contractaddress'] = contractaddress

            result = self._get_request(self.host, self.params)
            if result['message'] == 'NOTOK':
                print(f"Error - {result['result']}, host={self.host}")
                return [result]
            if currency in ['MCRT', ]:
                results.append({self.COIN: currency, self.BAL: float(result['result']) / (10 ** 9)})
            else:
                results.append({self.COIN: currency, self.BAL: float(result['result']) / (10 ** 18)})
        return results

    @staticmethod
    def _get_request(url: str, params: dict[str, str], headers=None) -> dict | None:
        """"""
        try:
            response = requests.request(method='GET', url=url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                e = f"Ошибка получения данных. Код ответа: {response.status_code}"
                print(e)
                return {'message': 'NOTOK', "result": e}
        except RequestException as e:
            print(f"Ошибка подключения: {str(e)}")
            return {'message': 'NOTOK', "result": str(e)}

    def get_account_balance(self) -> dict | None:
        """"""
        params = {'module': 'account',
                  'action': 'balance',
                  'address': self.wallet,
                  'apikey': self.api_key,
                  }
        result = self._get_request(self.host, params)
        return result

    def get_address_BEP20_token_holding(self):
        """API PRO need"""
        params = {'module': 'account',
                  'action': 'addresstokenbalance',
                  'address': self.wallet,
                  'page': 1,
                  'offset': 100,
                  'apikey': self.api_key,
                  }
        result = self._get_request(self.host, params)
        return result
