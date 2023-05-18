"""


"""
import os
import requests

from dotenv import load_dotenv

load_dotenv()


class Solana:
    """"""

    def __init__(self):
        super().__init__()
        self.host = 'https://public-api.solscan.io/account/tokens'
        self.api_key = os.environ.get('SOLANA_API_KEY')
        self.wallet = os.environ.get('WALLET_SOLANA')

        self.currencies = {
            # 'GARI': 'CKaKtYvz6dKPyMvYq9Rh3UBrnNqYZAyd7iF4hJtjUvks',
            'GWT': 'GWTipxSJVPmmW2wCjBdkbnEJbCRCyrhL2x9zuHRPPTj1',
            'YOM': 'yomFPUqz1wJwYSfD5tZJUtS3bNb8xs8mx9XzBv8RL39',
            'BONK': 'DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263',
        }

    def get_account(self):
        """"""
        headers = {
            'accept': 'application/json',
            'token': self.api_key,
        }
        params = {'account': self.wallet,
                  }
        response = self._get_request(self.host, params, headers)
        currencies = self._normalize_data(response)
        return currencies

    @staticmethod
    def _get_request(url, params, headers):
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

    def _normalize_data(self, currencies):
        results = []
        for currency in currencies:
            try:
                results.append({'coin': currency['tokenSymbol'],
                                'bal': int(currency['tokenAmount']['amount']) /
                                       10 ** currency['tokenAmount']['decimals']})
            except KeyError:
                if currency['tokenAddress'] in self.currencies.values():
                    for symbol, address in self.currencies.items():
                        if currency['tokenAddress'] == address:
                            results.append({'coin': symbol,
                                            'bal': int(currency['tokenAmount']['amount']) /
                                                   10 ** currency['tokenAmount']['decimals']})

        return {os.path.splitext(os.path.basename(__file__))[0]: sorted(results, key=lambda x: x['coin'])}


if __name__ == '__main__':
    r = Solana()

    res = r.get_account()
    print(res)

