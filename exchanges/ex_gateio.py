import os
import json
import requests
import time
import hashlib
import hmac

from dotenv import load_dotenv
load_dotenv()


print('~' * 50)

def gen_sign(method, url, query_string=None, payload_string=None):
    key = os.environ.get('GATE_API_KEY')        # api_key
    secret = os.environ.get('GATE_API_SECRET_KEY')      # api_secret

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    # print('1 - ', s)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    # print('2 - ', sign)
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}


host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/wallet/total_balance'
# url = '/spot/accounts'

query_param = ''
# query_param = 'currency=ADA'
# for `gen_sign` implementation, refer to section `Authentication` above


sign_headers = gen_sign('GET', prefix + url, query_param)
headers.update(sign_headers)
r = requests.request('GET', host + prefix + url, headers=headers)
print(r.json())


host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/accounts'
query_param = ''

sign_headers = gen_sign('GET', prefix + url, query_param)
headers.update(sign_headers)
r = requests.request('GET', host + prefix + url, headers=headers)

currencies = r.json()
# print(currencies)
currencies = sorted(currencies, key=lambda x: x['currency'])


for symbol in currencies:
    print(f"{symbol['currency']} = {float(symbol['available']) + float(symbol['locked'])}")