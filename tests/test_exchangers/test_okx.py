import unittest

import okx.Funding as Funding
import okx.Account as Account

from exchangers.ex_okx import ExOkx
from .test_base import TestBase

import warnings

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


class TestExOkx(unittest.TestCase, TestBase):

    def setUp(self) -> None:
        self.exchanger = ExOkx()

        self.api_key_wrong = 'wrong'
        self.api_secret_wrong = 'wrong'
        self.passphrase_wrong = 'wrong'
        self.host_wrong = 'https://www.okx.com/wrong'
        self.currencies_funding = {'code': '0',
                                   'data': [{'availBal': '1.0', 'bal': '1.0', 'ccy': 'USDC', 'frozenBal': '0'},
                                            {'availBal': '2.4', 'bal': '4.4', 'ccy': 'ATOM', 'frozenBal': '2.0'}],
                                   'msg': ''}
        self.currencies_trading = {'code': '0',
                                   'data': [{'adjEq': '',
                                             'details': [{'availBal': '106.44801351999999',
                                                          'availEq': '106.44801351999999',
                                                          'cashBal': '132.15261352',
                                                          'ccy': 'TON',
                                                          'disEq': '336.9168062010949',
                                                          'eq': '366.6124115354678',
                                                          'eqUsd': '673.8336124021898',
                                                          'frozenBal': '25.7046',
                                                          'isoEq': '234.4597980154678',
                                                          'isoUpl': '-39.83560198453216',
                                                          'ordFrozen': '25.7046',
                                                          'spotInUseAmt': '',
                                                          'uTime': '1679603648793',
                                                          'upl': '-39.83560198453216'}],
                                             'isoEq': '1762.2836545566988',
                                             'totalEq': '2716.910269253983',
                                             'uTime': '1685565174842'}],
                                   'msg': ''}

    def tearDown(self) -> None:
        del self.exchanger

    def _set_params_with_data(self, api_key=None,
                              api_secret=None,
                              passphrase=None,
                              host=None,
                              account=None):
        self.params = {'api_key': api_key,
                       'api_secret_key': api_secret,
                       'passphrase': passphrase,
                       'domain': host,
                       'use_server_time': False,
                       'flag': '0',
                       'debug': False}
        if account == 'funding':
            self.exchanger.funding = Funding.FundingAPI(**self.params)
        elif account == 'trading':
            self.exchanger.account = Account.AccountAPI(**self.params)

    def _check_data(self, result):
        self.assertFalse(result)
        # self.assertEqual(result['code'], 50111)
        # self.assertEqual(result['msg'], 'Invalid OK-ACCESS-KEY')

    def test_get_funding(self):
        result = self.exchanger.get_funding()

        self.assertIsInstance(result, dict)
        self.assertIn('data', result)
        self.assertIn('bal', result['data'][0])
        self.assertIn('ccy', result['data'][0])

    def test_get_funding_with_wrong_api(self):
        self._set_params_with_data(api_key=self.api_key_wrong,
                                   api_secret=self.exchanger.api_secret,
                                   passphrase=self.exchanger.passphrase,
                                   host=self.exchanger.host,
                                   account='funding')
        result = self.exchanger.get_funding()
        self._check_data(result)

    def test_get_funding_with_wrong_secret(self):
        self._set_params_with_data(api_key=self.exchanger.api_key,
                                   api_secret=self.api_secret_wrong,
                                   passphrase=self.exchanger.passphrase,
                                   host=self.exchanger.host,
                                   account='funding')
        result = self.exchanger.get_funding()
        self._check_data(result)

    def test_get_funding_with_wrong_passphrase(self):
        self._set_params_with_data(api_key=self.exchanger.api_key,
                                   api_secret=self.exchanger.api_secret,
                                   passphrase=self.host_wrong,
                                   host=self.exchanger.host,
                                   account='funding')
        result = self.exchanger.get_funding()
        self._check_data(result)

    def test_get_funding_with_wrong_host(self):
        self._set_params_with_data(api_key=self.exchanger.api_key,
                                   api_secret=self.exchanger.api_secret,
                                   passphrase=self.exchanger.passphrase,
                                   host=self.host_wrong,
                                   account='funding')
        result = self.exchanger.get_funding()
        self._check_data(result)

    def test_get_account_trading(self):
        result = self.exchanger.get_account_trading()

        self.assertIsInstance(result, dict)
        self.assertIn('data', result)
        self.assertIn('details', result['data'][0])
        self.assertIn('eq', result['data'][0]['details'][0])
        self.assertIn('ccy', result['data'][0]['details'][0])

    def test_get_account_trading_with_wrong_api(self):
        self._set_params_with_data(api_key=self.api_key_wrong,
                                   api_secret=self.exchanger.api_secret,
                                   passphrase=self.exchanger.passphrase,
                                   host=self.exchanger.host,
                                   account='trading')
        result = self.exchanger.get_account_trading()
        self._check_data(result)

    def test_get_account_trading_with_wrong_secret(self):
        self._set_params_with_data(api_key=self.exchanger.api_key,
                                   api_secret=self.api_secret_wrong,
                                   passphrase=self.exchanger.passphrase,
                                   host=self.exchanger.host,
                                   account='trading')
        result = self.exchanger.get_account_trading()
        self._check_data(result)

    def test_get_account_trading_with_wrong_passphrase(self):
        self._set_params_with_data(api_key=self.exchanger.api_key,
                                   api_secret=self.exchanger.api_secret,
                                   passphrase=self.host_wrong,
                                   host=self.exchanger.host,
                                   account='trading')
        result = self.exchanger.get_account_trading()
        self._check_data(result)

    def test_get_account_trading_with_wrong_host(self):
        self._set_params_with_data(api_key=self.exchanger.api_key,
                                   api_secret=self.exchanger.api_secret,
                                   passphrase=self.exchanger.passphrase,
                                   host=self.host_wrong,
                                   account='trading')
        result = self.exchanger.get_account_trading()
        self._check_data(result)

    # def test_get_account(self):
    #     result = self.exchanger.get_account()
    #     print(result)
    #
    #     self.assertIsInstance(result, dict)
    #     self.assertIsInstance(list(result.values())[0], list)
    #     self.assertIn(self.exchanger.exchanger, result)
    #     self.assertIn('coin', list(result.values())[0][0])
    #     self.assertIn('bal', list(result.values())[0][0])

    def test_normalize_data(self):
        self._check_data_in_test_base(
            self.exchanger._normalize_data(self.currencies_trading,
                                           self.currencies_funding))

    def test_normalize_with_empty_data(self):
        result = self.exchanger._normalize_data({}, {})

        self.assertIn(self.exchanger.exchanger, result)
        self.assertEqual(result[self.exchanger.exchanger], {})
