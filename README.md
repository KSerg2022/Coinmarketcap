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

    **Group** - _"### here can add currency for query one by one"_ - for querying one cryptocurrency.<br>
    If some cryptocurrency does not exist, then only there will be no result.
    - currencies_symbols_by_one = […] is the list of cryptocurrencies you created initially.
    - additional_currencies_symbols_by_one = […] - list of cryptocurrencies that you add.
    - currencies_symbols_spec_by_one = […] - list of cryptocurrencies that have a special notation.<br>
    ----
    **Group** - _"### base currencies for query by several"_ - one general request is made for all cryptocurrencies at once.<br>
    Use only when you are sure that all cryptocurrencies are on Coinmarketcap. Otherwise, you will receive an error.
    - currencies_symbols_ by_several = […] is the list of cryptocurrencies you created initially.
    - additional_currencies_symbols_ by_several = […] - list of cryptocurrencies that you add.
    - currencies_symbols_spec_ by_several = […] - list of cryptocurrencies that have a special notation.
    - currency_is_not_on_coinmarketcap = […] - list of cryptocurrencies that are not yet on coinmarketcap.


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
In him:
    1. “## for query one by one” – the functions are commented out so that they are used to query and <br>
    process the data received for each cryptocurrency separately.
        - get_cryptocurrency_onr_by_one(api_cmc),
        - parse_cryptocurrencies_data_one_by_one(cryptocurrencies_data).

    2. “#### for query by several” - the functions are commented out so that they are used to query and <br>
    process data received in one query for all cryptocurrencies.
        - get_cryptocurrency_by_several(api_cmc),
        - parse_cryptocurrencies_data_by_several(cryptocurrencies_data).

        ***Use either pair 1 or pair 2.***

    3. The function - "load_data_from_file()" - is used to work with loaded data,<br>
    if you do not want to make a request to the site every time.<br>
    The following functions must be commented out:
        - get_cryptocurrency_onr_by_one(api_cmc),
        - get_cryptocurrency_by_several(api_cmc),
        - wright_to_json(cryptocurrencies_data).

        *Which function to use for data processing<br>*
            (parse_cryptocurrencies_data_one_by_one, parse_cryptocurrencies_data_by_several)<br>
        depends on which last request you made<br>
            (get_cryptocurrency_onr_by_one, get_cryptocurrency_by_several).*