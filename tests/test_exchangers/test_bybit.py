import unittest

from pybit.unified_trading import HTTP

from exchangers.ex_bybit import ExBybit
from tests.test_exchangers.test_base import TestBase

import warnings

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


class TestEcBybit(unittest.TestCase, TestBase):

    def setUp(self) -> None:
        self.exchanger = ExBybit()

        self.api_key_wrong = 'wrong'
        self.api_secret_wrong = 'wrong'
        self.session = None
        self.account_spot = {'retCode': 0,
                             'retMsg': 'success',
                             'result': {'spot':
                                            {'status': 'ACCOUNT_STATUS_NORMAL',
                                             'assets': [{'coin': 'BTC',
                                                         'frozen': '0',
                                                         'free': '1.0',
                                                         'withdraw': ''},
                                                        {'coin': 'ETH',
                                                         'frozen': '2.0',
                                                         'free': '2.0',
                                                         'withdraw': ''},
                                                        ]}},
                             'retExtInfo': {},
                             'time': 1685645543575}

        self.account_margin = {'retCode': 0,
                               'retMsg': 'OK',
                               'result': {'list':
                                              [{'accountType': 'CONTRACT',
                                                'coin': [{'coin': 'BTC',
                                                          'equity': '0.02',
                                                          'usdValue': '',
                                                          'walletBalance': '0.02',
                                                          'borrowAmount': '',
                                                          'availableToBorrow': '',
                                                          'availableToWithdraw': '0.00997847',
                                                          'accruedInterest': '',
                                                          'totalOrderIM': '0.01002153',
                                                          'totalPositionIM': '0',
                                                          'totalPositionMM': '',
                                                          'unrealisedPnl': '0',
                                                          'cumRealisedPnl': '0'},
                                                         {'coin': 'LTC',
                                                          'equity': '0.02',
                                                          'usdValue': '',
                                                          'walletBalance': '0.02',
                                                          'borrowAmount': '',
                                                          'availableToBorrow': '',
                                                          'availableToWithdraw': '0.00997847',
                                                          'accruedInterest': '',
                                                          'totalOrderIM': '0.01002153',
                                                          'totalPositionIM': '0',
                                                          'totalPositionMM': '',
                                                          'unrealisedPnl': '0',
                                                          'cumRealisedPnl': '0'},
                                                         ]}]},
                               'retExtInfo': {},
                               'time': 1685645665891}

    def tearDown(self) -> None:
        del self.exchanger

    def test_get_account_spot(self):
        result = self.exchanger.get_account_spot()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['retMsg'], 'success')
        self.assertIn('result', result)
        self.assertIn('spot', result['result'])
        self.assertIn('assets', result['result']['spot'])

    def test_get_account_margin(self):
        result = self.exchanger.get_account_margin()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['retMsg'], 'OK')
        self.assertIn('result', result)
        self.assertIn('list', result['result'])
        self.assertIn('coin', result['result']['list'][0])

    def test_normalize_data(self):
        self._check_data_in_test_base(
            self.exchanger._normalize_data(self.account_spot,
                                           self.account_margin))

    def test_normalize_with_empty_data(self):
        result = self.exchanger._normalize_data({}, {})

        self.assertIn(self.exchanger.exchanger, result)
        self.assertEqual(result[self.exchanger.exchanger], {})
