import unittest
import time

from exchangers.ex_gateio import ExGate


class TestExMexc(unittest.TestCase):

    def setUp(self) -> None:
        self.exchanger = ExGate()

    def tearDown(self) -> None:
        del self.exchanger

    def test_gen_sign(self):
        url = '/spot/accounts'
        result = self.exchanger.gen_sign('GET',
                                         self.exchanger.host + url,
                                         self.exchanger.query_param)

        self.assertIn('KEY', result)
        self.assertIn('Timestamp', result)
        self.assertIn('SIGN', result)

    def test_get_total_balance(self):
        result = self.exchanger.get_total_balance().json()

        self.assertIsInstance(result, dict)
        self.assertIn('details', result.keys())
        self.assertIn('spot', list(result.values())[0])
        self.assertIn('total', result.keys())

    def test_get_account(self):
        result = self.exchanger.get_account()

        self.assertIsInstance(result, dict)
        self.assertIsInstance(list(result.values())[0], list)

    def test_normalize_data(self):
        test_data = [{'currency': 'FIRO', 'available': '5', 'locked': '0'},
                     {'currency': 'POLS', 'available': '10', 'locked': '5'}
                     ]
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
        url = '/spot/accounts'
        result = self.exchanger._get_request(url).json()

        self.assertIsInstance(result, list)
        self.assertNotEqual(len(result), 0)
        self.assertIn('currency', result[0])
        self.assertIn('available', result[0])
        self.assertIn('locked', result[0])

    def test_get_request_with_wrong_key(self):
        self.exchanger.key = 'wrong'
        url = '/spot/accounts'
        result = self.exchanger._get_request(url).json()

        self.assertEqual(result['message'], 'Invalid key provided')
        self.assertEqual(result['label'], 'INVALID_KEY')

    def test_get_request_with_wrong_secret(self):
        self.exchanger.secret = 'wrong'
        url = '/spot/accounts'
        result = self.exchanger._get_request(url).json()

        self.assertEqual(result['message'], 'Signature mismatch')
        self.assertEqual(result['label'], 'INVALID_SIGNATURE')

    def test_get_request_with_wrong_host(self):
        self.exchanger.host = "https://api.gateio.ws/wrong"
        url = '/spot/accounts'
        result = self.exchanger._get_request(url)

        self.assertEqual(result.status_code, 404)

    def test_get_request_with_wrong_prefix(self):
        self.exchanger.prefix = "/api/v1/"
        url = '/spot/accounts'
        result = self.exchanger._get_request(url)

        self.assertEqual(result.status_code, 404)

    def test_get_request_with_wrong_url(self):
        url = '/spot/wrong'
        result = self.exchanger._get_request(url)

        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=1)
