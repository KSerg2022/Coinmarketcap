""""""
import unittest


from pathlib import Path

from blockchains.bsc import Bsc
from blockchains.polygon import Polygon
from blockchains.ether import Ether
from blockchains.fantom import Fantom
from tests.tests_blockchains.test_base import (TestBaseGetRequest,
                                                TestBaseGetAccount)

from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).parent.parent


class TestBsc(unittest.TestCase, TestBaseGetRequest, TestBaseGetAccount):

    def setUp(self) -> None:
        self.b_chain = Bsc()
        self.contract_address = '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'

    def tearDown(self) -> None:
        del self.b_chain


class TestPolygon(unittest.TestCase, TestBaseGetRequest, TestBaseGetAccount):

    def setUp(self) -> None:
        self.b_chain = Polygon()
        self.contract_address = '0x0000000000000000000000000000000000001010'

    def tearDown(self) -> None:
        del self.b_chain


class TestEther(unittest.TestCase, TestBaseGetRequest, TestBaseGetAccount):

    def setUp(self) -> None:
        self.b_chain = Ether()
        self.contract_address = '0x2170ed0880ac9a755fd29b2688956bd959f933f8'

    def tearDown(self) -> None:
        del self.b_chain


class TestFantom(unittest.TestCase, TestBaseGetRequest, TestBaseGetAccount):

    def setUp(self) -> None:
        self.b_chain = Fantom()
        self.contract_address = '0xE705aF5f63fcaBDCDF5016aA838EAaac35D12890'

    def tearDown(self) -> None:
        del self.b_chain


if __name__ == '__main__':
    unittest.main(verbosity=1)
