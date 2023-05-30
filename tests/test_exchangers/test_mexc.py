
import unittest

from exchangers.ex_mexc import ExMexc


class TestExMexc(unittest.TestCase):

    def setUp(self) -> None:
        self.exchanger = ExMexc()

    def tearDown(self) -> None:
        del self.exchanger

    def test_gen_sign(self):
        result = self.exchanger.gen_sign()
        self.assertIn('timestamp', result)
        self.assertIn('signature', result)

    def test_gen_sign_with_wrong_apiSecret(self):
        correct_result = self.exchanger.gen_sign()
        self.exchanger.apiSecret = 'wrong'
        incorrect_result = self.exchanger.gen_sign()
        self.assertNotEqual(correct_result['signature'],
                            incorrect_result['signature'])

    def test_get_account(self):
        result = self.exchanger.get_account()

        self.assertIsInstance(result, dict)
        self.assertIsInstance(list(result.values())[0], list)

    def test_normalize_data(self):
        test_data = {'accountType': 'SPOT',
                     'balances': [{'asset': "USDT", "free": '1', 'locked': '0'},
                                  {'asset': 'DOT', 'free': '1', 'locked': '2'},
                                  ],
                     'permissions': ['SPOT']
                     }
        result = self.exchanger._normalize_data(test_data)

        self.assertIn(self.exchanger.exchanger, result)
        self.assertIn('coin', list(result.values())[0][0])
        self.assertIn('bal', list(result.values())[0][0])

    def test_normalize_with_empty_data(self):
        test_data = {}
        result = self.exchanger._normalize_data(test_data)

        self.assertIn(self.exchanger.exchanger, result)
        self.assertEqual(result[self.exchanger.exchanger], {})

    def test_get_request(self):
        result = self.exchanger._get_request().json()

        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result['balances'])
        self.assertEqual(result['accountType'], 'SPOT')

    def test_get_request_with_wrong_apiSecret(self):
        self.exchanger.apiSecret = 'wrong'
        result = self.exchanger._get_request().json()

        self.assertEqual(result['code'], 700002)
        self.assertEqual(result['msg'], 'Signature for this request is not valid.')

    def test_get_request_with_wrong_host(self):
        self.exchanger.host = "https://api.mexc.com/wrong"
        result = self.exchanger._get_request().json()

        self.assertEqual(result['code'], 404)
        self.assertEqual(result['msg'], 'Not Found')

    def test_get_request_with_wrong_prefix(self):
        self.exchanger.prefix = "/api/v1/"
        result = self.exchanger._get_request().json()

        self.assertEqual(result['code'], 404)
        self.assertEqual(result['msg'], 'Not Found')

    def test_get_request_to_other_url(self):
        self.exchanger.url = "myTrades"
        result = self.exchanger._get_request().json()

        self.assertEqual(result['code'], 700007)
        self.assertEqual(result['msg'], 'No permission to access the endpoint.')

    def test_get_request_with_wrong_url(self):
        self.exchanger.url = "wrong"
        result = self.exchanger._get_request()

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.text, '')


if __name__ == '__main__':
    unittest.main(verbosity=1)
