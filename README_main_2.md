# Coinmarketcap

## For file 'main_2.py'.

Program that by the lists cryptocurrencies, exchanges and blockchains returns "*.csv" and "*.exlx" files with the following data: exchange or blockchain, coin, data, id, name, price, total ptrice.

For the script to work you need:
1. Create a “.env” file in the root directory and put<br>
“API_COINMARCETCAP=\<your API key>” there, which you should get by registering on the Coinmarketcap.com website.
And fill other fields which you need:
- exchangers,
- blockchains.

**! For the exchanges API, the necessary permissions are not yet described.**


2. In the “settings.py” file, you need to enter the symbols of the <br>cryptocurrencies you are interested in (example in the file):

    - currencies_symbols = […] is the list of cryptocurrencies you created initially.
    - additional_currencies_symbols = […] - list of cryptocurrencies that you add.
    - currencies_symbols_spec = […] - list of cryptocurrencies that have a special notation.<

    """Blockchains"""
    - BSC_CURRENCIES = {}
    - ETHER_CURRENCIES = {}
    - FTM_CURRENCIES = {}
    - POLYGON_CURRENCIES = {}
    - SOLANA_CURRENCIES = {}


3. The file "main_2.py" - the file to run.<br>
    In him:<br>
    The functions - "load_cmc_data_from_file(), load_exchangers_data_from_file" - are used to work with loaded data,<br>
    if you do not want to make a request to the site every time.<br>
    The following functions must be commented out:
        - get_cryptocurrency(api_cmc),
        - wright_to_json_cmc_data(cryptocurrencies_data).
        - get_data_from_exchangers(cryptocurrencies_data).
        - wright_to_json_exchangers_data(cryptocurrencies_data).
