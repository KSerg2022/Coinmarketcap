"""https://github.com/LBank-exchange/lbank-python-api/blob/master/LBank/rest.py"""
import os


from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('LBANK_API_KEY')
PRIVATE_KEY = os.environ.get('LBANK_API_SECRET_KEY')
print(len(PRIVATE_KEY), PRIVATE_KEY)

from LBank import LBankAPI

api = LBankAPI(API_KEY, PRIVATE_KEY)
assets = api.user_assets()
# print(assets.keys())
# print(assets['info']['toBtc'])
for symbol, value in assets['info']['toBtc'].items():
    # print(symbol, value)
    if float(value) != 0:
        print(f"{symbol} = {value}")
