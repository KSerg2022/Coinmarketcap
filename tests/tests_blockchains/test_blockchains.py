""""""
import unittest
import json

from pathlib import Path

from blockchains.bsc import Bsc

from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).parent.parent


class TestCmc(unittest.TestCase):

    def setUp(self) -> None:
        self.bsc = Bsc()

    def tearDown(self) -> None:
        del self.bsc

    @staticmethod
    def get_headers(api_cmc):
        return {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_cmc}

    @staticmethod
    def get_parameters(symbols):
        return {'symbol': symbols, 'convert': 'USD'}

    @staticmethod
    def _get_params(module='account',
                    action='tokenbalance',
                    contractaddress='0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
                    wallet=None,
                    apikey=None):
        return {'module': module,
                'action': action,
                'contractaddress': contractaddress,
                'address': wallet,
                'tag': 'latest',
                'apikey': apikey,
                }

    def test__get_request(self):
        params = self._get_params(wallet=self.bsc.wallet,
                                  apikey=self.bsc.api_key)
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result['message'], 'OK')
        self.assertTrue(isinstance(int(result['result']), int))

    def test__get_request_with_wrong_contractaddress(self):
        params = self._get_params(contractaddress='0',
                                  wallet=self.bsc.wallet,
                                  apikey=self.bsc.api_key)
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], 'Invalid contractAddress format')

    def test__get_request_with_wrong_api(self):
        params = self._get_params(wallet=self.bsc.wallet,
                                  apikey='wrong')
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], 'Invalid API Key')

    def test__get_request_with_empty_api(self):
        params = self._get_params(wallet=self.bsc.wallet,
                                  apikey='')
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertIn('OK-Missing/Invalid API Key', result['message'])

    def test__get_request_with_wrong_wallet(self):
        params = self._get_params(wallet='wrong',
                                  apikey=self.bsc.api_key)
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], 'Error! Invalid address format')

    def test__get_request_with_wrong_host(self):
        params = self._get_params(wallet=self.bsc.wallet,
                                  apikey=self.bsc.api_key)
        result = self.bsc._get_request('https://api.bscscan.com/wrong', params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], "Ошибка получения данных. Код ответа: 404")

    def test__get_request_with_wrong_module(self):
        params = self._get_params(module='wron',
                                  wallet=self.bsc.wallet,
                                  apikey=self.bsc.api_key)
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'],
                         "Error! Missing Or invalid Module name")

    def test__get_request_with_wrong_action(self):
        params = self._get_params(action='wron',
                                  wallet=self.bsc.wallet,
                                  apikey=self.bsc.api_key)
        result = self.bsc._get_request(self.bsc.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'],
                         "Error! Missing Or invalid Action name")

    # def test__get_request_status_not_200(self):
    #     """нужно черезх мок"""
    #     pass


class testBscGetAccount(TestCmc):

    def test_get_account(self):
        result = self.bsc.get_account()

        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(list(result.values())[0], list))
        self.assertIn(self.bsc.COIN, list(result.values())[0][0])
        self.assertIn(self.bsc.BAL, list(result.values())[0][0])

    def test_get_account_with_wrong_api(self):
        self.bsc.params = self._get_params(wallet=self.bsc.wallet,
                                            apikey='wrong')
        result = self.bsc.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Invalid API Key')

    def test_get_account_with_wrong_wallet(self):
        self.bsc.params = self._get_params(wallet='wrong',
                                            apikey=self.bsc.api_key)
        result = self.bsc.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Error! Invalid address format')

    def test_get_account_with_wrong_host(self):
        self.bsc.host = 'https://api.bscscan.com/wrong'
        result = self.bsc.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], "Ошибка получения данных. Код ответа: 404")

    def test_get_account_with_wrong_host_(self):
        self.bsc.host = 'ttps://api.bscscan.com/api'
        result = self.bsc.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'],
                         "No connection adapters were found for 'ttps://api.bscscan.com/api'")

    def test_get_account_with_wrong_currencies(self):
        self.bsc.currencies = {
            'BUSD': '0',
            'CAKE': '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82_', }
        result = self.bsc.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Invalid contractAddress format')


if __name__ == '__main__':
    unittest.main()
