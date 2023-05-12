import os
import json
import requests
import time
import hashlib
import hmac

from dotenv import load_dotenv
load_dotenv()
apiKey = os.environ.get('MEXC_API_KEY')
apiSecret = os.environ.get('MEXC_API_SECRET_KEY')


# from MexcClient.client import MexcClient
# client = MexcClient(api_key='apiKey', api_secret='apiSecret')
#
# print(client)
# print(client.server_time())
# print(client.check_connection())
# print(client.base_url)
# # print(client.exchange_info())
# print(client.load_balances())



print('~' * 50)
from datetime import datetime
import urllib.parse

import requests

from MexcClient.Utils.Signature import generate_signature


headers = {"X-MEXC-APIKEY": apiKey, "Content-Type": "application/json"}
params = {"timestamp": int(datetime.now().timestamp()) * 1000}

str_params = urllib.parse.urlencode(params)
signature = generate_signature(apiSecret.encode(), str_params.encode())
params["signature"] = signature


host = "https://api.mexc.com"
prefix = "/api/v3/"
url = 'account'
r = requests.request('GET', host + prefix + url, headers=headers, params=params)
# print(r.json())

currencies = r.json()
print(currencies)
# print(currencies.keys())
currencies = sorted(currencies['balances'], key=lambda x: x['asset'])

for symbol in currencies:
    print(f"{symbol['asset']} = {float(symbol['free']) + float(symbol['locked'])}")



