# Coinmarketcap


The script requests data on cryptocurrencies on the Coinmarketcap.com website,
saving the result in \<file>.json.<br>
After that, certain information is obtained and stored in the following formats:
- \<file>.csv
- \<file>.xlsx.

For the script to work you need:
1. Create a “.env” file in the root directory and put<br>
“API_COINMARCETCAP=\<your API key>” there, which you should get by registering on the Coinmarketcap.com website.


2. In the “settings.py” file, you need to enter the symbols of the <br>cryptocurrencies you are interested in (example in the file):

    - currencies_symbols = […] is the list of cryptocurrencies you created initially.
    - additional_currencies_symbols = […] - list of cryptocurrencies that you add.
    - currencies_symbols_spec = […] - list of cryptocurrencies that have a special notation.


3. In the file “get_data.py” in the function “parse_cryptocurrencies_data”.
    1. The following data is defined for saving:
        -date,
        - id,
        - name,
        - symbol,
        - price.
    2. There is also additional data that is commented out. If necessary, they can be quickly used.
        - additional data,
        - circulating_supply,
        - total_supply,
        - market_cap,
        - fully_diluted_market_cap.
    3. If you need any more data from \<file>.json, you need to add it in this function.


4. The file "main.py" - the file to run.<br>
    In him:<br>
    1. The functions are used to query and process data received in query for cryptocurrencies.
        - get_cryptocurrency(api_cmc),
        - parse_cryptocurrencies(cryptocurrencies_data).<br>

    2. The function - "load_data_from_file()" - is used to work with loaded data,<br>
    if you do not want to make a request to the site every time.<br>
    The following functions must be commented out:
        - get_cryptocurrency(api_cmc),
        - wright_to_json(cryptocurrencies_data).
    