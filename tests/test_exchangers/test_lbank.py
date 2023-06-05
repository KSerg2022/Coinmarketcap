import unittest

from exchangers.ex_lbank import ExLbank

from .test_base import TestBase


class TestExLbank(unittest.TestCase, TestBase):

    def setUp(self) -> None:
        self.exchanger = ExLbank()

        self.api_key_wrong = 'wrong'
        self.api_secret_wrong = 'wrong'
        self.session = None
        self.test_data = {'result': 'true',
                          'info': {'toBtc':
                                       {'ksm': '1',
                                        'gki': '2',
                                        'sxp3s': '5',
                                        }
                                   }
                          }
        self.test_data_empty = {}

    def tearDown(self) -> None:
        del self.exchanger
