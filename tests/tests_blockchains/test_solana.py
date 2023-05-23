""""""
import unittest

from pathlib import Path

from blockchains.solana import Solana

from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).parent.parent


class TestSolana(unittest.TestCase):

    def setUp(self) -> None:
        self.b_chain = Solana()

    def tearDown(self) -> None:
        del self.b_chain

    def _get_params(self, wallet=None):
        if wallet is None:
            wallet = self.b_chain.wallet
        return {'account': wallet}

    def _get_headers(self, api_key=None):
        if api_key is None:
            api_key = self.b_chain.api_key
        return {'account': api_key}


class TestSolanaGetRequest(TestSolana):

    def test__get_request(self):
        response = self.b_chain._get_request(self.b_chain.host,
                                           self.b_chain.params,
                                           self.b_chain.headers)

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertIsNotNone(response[0]['tokenAddress'])

    def test__get_request_with_wrong_api(self):
        self.b_chain.headers = self._get_headers(api_key='wrong')
        response = self.b_chain._get_request(self.b_chain.host,
                                           self.b_chain.params,
                                           self.b_chain.headers)

        self.assertEqual(response['message'], 'NOTOK')
        self.assertEqual(response['result'], 'Ошибка получения данных. Код ответа: 429')

    def test__get_request_with_wrong_wallet(self):
        self.b_chain.params = self._get_params(wallet='0')
        response = self.b_chain._get_request(self.b_chain.host,
                                             self.b_chain.params,
                                             self.b_chain.headers)

        self.assertEqual(response['message'], 'NOTOK')
        self.assertEqual(response['result'], 'Ошибка получения данных. Код ответа: 400')

    def test__get_request_with_wrong_host(self):
        response = self.b_chain._get_request('https://public-api.solscan.io/wrong',
                                             self.b_chain.params,
                                             self.b_chain.headers)

        self.assertEqual(response['message'], 'NOTOK')
        self.assertEqual(response['result'], "Ошибка получения данных. Код ответа: 404")


class testSolanaGetAccount(TestSolana):

    def test_get_account(self):
        result = self.b_chain.get_account()

        self.assertIsInstance(result, dict)
        self.assertIsInstance(list(result.values())[0], list)
        self.assertIn(self.b_chain.COIN, list(result.values())[0][0])
        self.assertIn(self.b_chain.BAL, list(result.values())[0][0])

    def test_get_account_with_wrong_api(self):
        self.b_chain.headers = self._get_headers(api_key='wrong')
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Ошибка получения данных. Код ответа: 429')

    def test_get_account_with_wrong_wallet(self):
        self.b_chain.params = self._get_params(wallet='0')
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Ошибка получения данных. Код ответа: 400')

    def test_get_account_with_wrong_host(self):
        self.b_chain.host = 'https://public-api.solscan.io/wrong'
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], "Ошибка получения данных. Код ответа: 404")

    def test_get_account_with_wrong_currencies(self):
        self.b_chain.currencies = {'BUSD': 'wrong'}
        result = self.b_chain.get_account()

        self.assertIsInstance(result, dict)
        self.assertIsInstance(list(result.values())[0], list)
        self.assertIn(self.b_chain.COIN, list(result.values())[0][0])
        self.assertIn(self.b_chain.BAL, list(result.values())[0][0])


if __name__ == '__main__':
    unittest.main()
