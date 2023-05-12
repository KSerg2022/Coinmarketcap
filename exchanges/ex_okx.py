import os
import  json

from dotenv import load_dotenv
load_dotenv()


from settings import base_dir, time_stamp

api_key = os.environ.get('OKX_API_KEY')
api_secret = os.environ.get('OKX_API_SECRET_KEY')
passphrase = os.environ.get('OKX_PWD')

import okx.Trade as Trade

import okx.Account as Account


account = Account.AccountAPI(api_key=api_key, api_secret_key=api_secret, passphrase=passphrase,
                             domain='https://www.okx.com/')


result = account.get_account_balance(ccy='ATOM')
# result = account.get_account_position_tiers(instType='SPOT')
print(result)


