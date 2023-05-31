""""""
import unittest


from pathlib import Path

from blockchains.base import Base

from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).parent.parent


class TestBase:

    def setUp(self) -> None:
        self.b_chain = Base()
        self.contract_address = ''

    def tearDown(self) -> None:
        del self.b_chain

    def _get_params(self,
                    module='account',
                    action='tokenbalance',
                    contract_address=None,
                    wallet=None,
                    apikey=None):

        if contract_address is None:
            contract_address = self.contract_address
        return {'module': module,
                'action': action,
                'contractaddress': contract_address,
                'address': wallet,
                'tag': 'latest',
                'apikey': apikey,
                }

    def assertIsInstance(self, param, list):
        pass

    def assertIn(self, exchanger, result):
        pass

    def assertEqual(self, param, param1):
        pass

    def assertTrue(self, param):
        pass


class TestBaseGetRequest(TestBase):

    def test__get_request(self):
        b_chain = self.b_chain
        params = self._get_params(wallet=b_chain.wallet,
                                  apikey=b_chain.api_key)
        result = b_chain._get_request(b_chain.host, params)

        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result['message'], 'OK')
        self.assertTrue(isinstance(int(result['result']), int))

    def test__get_request_with_wrong_contract_address(self):
        params = self._get_params(contract_address='0',
                                  wallet=self.b_chain.wallet,
                                  apikey=self.b_chain.api_key)
        result = self.b_chain._get_request(self.b_chain.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], 'Invalid contractAddress format')

    def test__get_request_with_wrong_api(self):
        params = self._get_params(wallet=self.b_chain.wallet,
                                  apikey='wrong')
        result = self.b_chain._get_request(self.b_chain.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], 'Invalid API Key')

    def test__get_request_with_empty_api(self):
        params = self._get_params(wallet=self.b_chain.wallet,
                                  apikey='')
        result = self.b_chain._get_request(self.b_chain.host, params)

        self.assertIn('OK-Missing/Invalid API Key', result['message'])

    def test__get_request_with_wrong_wallet(self):
        params = self._get_params(wallet='wrong',
                                  apikey=self.b_chain.api_key)
        result = self.b_chain._get_request(self.b_chain.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], 'Error! Invalid address format')

    def test__get_request_with_wrong_host(self):
        params = self._get_params(wallet=self.b_chain.wallet,
                                  apikey=self.b_chain.api_key)
        result = self.b_chain._get_request('https://api.bscscan.com/wrong', params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'], "Ошибка получения данных. Код ответа: 404")

    def test__get_request_with_wrong_module(self):
        params = self._get_params(module='wron',
                                  wallet=self.b_chain.wallet,
                                  apikey=self.b_chain.api_key)
        result = self.b_chain._get_request(self.b_chain.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'],
                         "Error! Missing Or invalid Module name")

    def test__get_request_with_wrong_action(self):
        params = self._get_params(action='wron',
                                  wallet=self.b_chain.wallet,
                                  apikey=self.b_chain.api_key)
        result = self.b_chain._get_request(self.b_chain.host, params)

        self.assertEqual(result['message'], 'NOTOK')
        self.assertEqual(result['result'],
                         "Error! Missing Or invalid Action name")


class TestBaseGetAccount(TestBase):

    def test_get_account(self):
        result = self.b_chain.get_account()

        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(list(result.values())[0], list))
        self.assertIn(self.b_chain.COIN, list(result.values())[0][0])
        self.assertIn(self.b_chain.BAL, list(result.values())[0][0])

    def test_get_account_with_wrong_api(self):
        self.b_chain.params = self._get_params(wallet=self.b_chain.wallet,
                                            apikey='wrong')
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Invalid API Key')

    def test_get_account_with_wrong_wallet(self):
        self.b_chain.params = self._get_params(wallet='wrong',
                                            apikey=self.b_chain.api_key)
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Error! Invalid address format')

    def test_get_account_with_wrong_host(self):
        self.b_chain.host = 'https://api.bscscan.com/wrong'
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], "Ошибка получения данных. Код ответа: 404")

    def test_get_account_with_wrong_host_(self):
        self.b_chain.host = 'ttps://api.bscscan.com/api'
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'],
                         "No connection adapters were found for 'ttps://api.bscscan.com/api'")

    def test_get_account_with_wrong_currencies(self):
        self.b_chain.currencies = {
            'BUSD': '0',
            'CAKE': '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82_', }
        result = self.b_chain.get_account()

        self.assertEqual(list(result.values())[0][0]['message'], 'NOTOK')
        self.assertEqual(list(result.values())[0][0]['result'], 'Invalid contractAddress format')

