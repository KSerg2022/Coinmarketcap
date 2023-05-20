""""""
import unittest
import json

from pathlib import Path

from cmc.cmc import Cmc

# import warnings
# warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).parent.parent


class TestCmc(unittest.TestCase):

    def setUp(self) -> None:
        self.cmc = Cmc()

    def tearDown(self) -> None:
        del self.cmc


class testCncGetCryptocurrency(TestCmc):

    def test_get_cryptocurrency(self):
        response = self.cmc.get_cryptocurrency()

        self.assertTrue(isinstance(response, dict))
        self.assertIsNotNone(response['data'])
        self.assertEqual(response['status']['error_code'], 0)

    def test_get_cryptocurrency_with_wrong_api(self):
        self.cmc.api_cmc = 'qwqw'
        response = self.cmc.get_cryptocurrency()

        self.assertEqual(response['status']['error_code'], 1001)
        self.assertEqual(response['status']['error_message'], 'This API Key is invalid.')

    def test_get_cryptocurrency_with_wrong_url(self):
        self.cmc.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/'
        response = self.cmc.get_cryptocurrency()

        self.assertEqual(response['statusCode'], 404)
        self.assertEqual(response['message'], 'Not Found')

    def test_get_cryptocurrency_with_empty_symbols(self):
        self.cmc.symbols = []
        response = self.cmc.get_cryptocurrency()

        self.assertEqual(response['status']['error_code'], 400)
        self.assertEqual(response['status']['error_message'], '"symbol" is not allowed to be empty')

    def test_get_cryptocurrency_with_wrong_symbol(self):
        self.cmc.symbols = ['QQQQQQ']
        response = self.cmc.get_cryptocurrency()

        self.assertEqual(response['status']['error_code'], 0)
        self.assertEqual(response['data'], {})


class TestCmcParseCryptocurrencies(TestCmc):

    def test_parse_cryptocurrencies_data(self):
        path_to_file = base_dir / 'data_for_tests' / 'cmc_data__for_tests.json'
        data = load_data_from_file(path_to_file)

        result = self.cmc.parse_cryptocurrencies(data)
        self.assertTrue(isinstance(result, dict))

    def test_parse_cryptocurrencies_data_with_empty_data(self):
        data = {}
        result = self.cmc.parse_cryptocurrencies(data)

        self.assertTrue(isinstance(result, dict))
        self.assertEqual(list(result.values()), [])

    def test_parse_cryptocurrencies_data_with_not_correct_data(self):
        data = {
            "status": {
                "timestamp": "2023-05-20T13:26:55.517Z",
            },
            "data": {
                "ADA": {
                    "id": 2010,
                    "name": "Cardano",
                    "symbol": "ADA",
                    "quote": {
                        "USD": {
                            "price": 0.36510704694717705,
                        }
                    }
                }
            }
        }
        path_to_file = base_dir / 'data_for_tests' / 'cmc_data__for_tests_not_correct.json'
        data = load_data_from_file(path_to_file)
        self.cmc.symbols = ['ADA']

        for i in data[:2]:
            result = self.cmc.parse_cryptocurrencies(i)
            self.assertEqual(result, {})

        result = self.cmc.parse_cryptocurrencies(data[2])
        self.assertEqual(list(result.values())[0]['id'], 'not in CMC')


class TestCmcParseCryptocurrenciesData(TestCmc):
    pass


class TestCmcFillValuesIfIsNotSymbol(TestCmc):
    pass


def load_data_from_file(file) -> dict:
    with open(file, 'r') as file_json:
        loaded_data = json.load(file_json)
    return loaded_data


if __name__ == '__main__':
    unittest.main()
