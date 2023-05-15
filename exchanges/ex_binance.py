"""
https://dev.binance.vision/t/ip-whitelist-does-not-have-effect/2767
"""
import os
import json

from dotenv import load_dotenv
load_dotenv()

from binance.spot import Spot

from settings import base_dir, time_stamp


api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET_KEY')


client = Spot(api_key=api_key, api_secret=api_secret, base_url='https://api.binance.com')


# print(client.account())
account = client.account()

print(account.keys())
print(account['permissions'])

for symbol in account['balances']:
    if (float(symbol['free']) > 0) or (float(symbol['locked']) > 0):
        # print(f'{symbol["asset"]} - free={symbol["free"]}, locked={symbol["locked"]},'
        #       f'TOTAL ={float(symbol["free"]) + float(symbol["locked"])}')

        print(f'{symbol["asset"]} = {float(symbol["free"]) + float(symbol["locked"])}')

print('~' * 50)
result = client.account_snapshot(type="SPOT")
for symbol in result['snapshotVos'][-1]['data']['balances']:
    if (float(symbol['free']) > 0) or (float(symbol['locked']) > 0):
        print(f"{symbol['asset']} = {float(symbol['free']) + float(symbol['locked'])}")

print('~' * 50)
# print(client.account_snapshot(type="MARGIN"))
print(client.account_snapshot(type="FUTURES"))
print(len(client.coin_info()), client.coin_info()[:3])
print(client.user_asset())
print(client.api_key_permissions())
print(client.api_key_permissions())

print('~' * 50)


print('~' * 50)




def wright_to_json(data: list[dict] | dict[dict]):
    """Writing to file human-readable data."""
    filename = base_dir / 'json_files' / f'binance_{time_stamp}.json'
    with open(filename, 'w') as file_json:
        json.dump(data, file_json, indent=4)

# wright_to_json(client.account())
