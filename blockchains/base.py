"""

"""

import requests

from dotenv import load_dotenv
load_dotenv()


class Base:
    """"""
    def __init__(self):
        self.host = ''
        self.api_key = ''
        self.wallet = ''
        self.currencies = {}

    def _get_account(self) -> list[dict]:
        """"""
        results = []
        for currency, contractaddress in self.currencies.items():
            params = {'module': 'account',
                      'action': 'tokenbalance',
                      'contractaddress': contractaddress,
                      'address': self.wallet,
                      'tag': 'latest',
                      'apikey': self.api_key,
                      }
            result = self._get_request(self.host, params)
            if currency in ['MCRT', ]:
                results.append({'coin': currency, 'bal': float(result['result']) / (10 ** 9)})
            else:
                results.append({'coin': currency, 'bal': float(result['result']) / (10 ** 18)})
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
                print(f"Ошибка получения данных. Код ответа: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {str(e)}")
        return None

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
