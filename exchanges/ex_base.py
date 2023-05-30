import os
import json

from dotenv import load_dotenv

load_dotenv()


class Exchanger:

    # def __init__(self):
    #     pass

    @staticmethod
    def _get_response(fn, exchanger=None, exception=None,  accountType=None, url=None) -> dict | list:
        try:
            if accountType:
                response = fn(accountType=accountType)
            elif url:
                response = fn(url=url)
            else:
                response = fn()
        except (Exception, *exception) as e:
            print(f'{exchanger.upper()} -- {e}')
            return {}
        return response
