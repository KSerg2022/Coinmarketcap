import datetime

from pathlib import Path

base_dir = Path(__file__).parent
time_stamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


# base currencies
currencies_symbols = [
    'AGV', 'TICKET', 'FS', 'BEAM', 'YOM', 'LUNA', 'SOLC', 'ATOM', 'KZEN', 'LUNC', 'VENT', 'CAKE', 'MCRT', 'ESCROW',
    'AVXL', 'ONG', 'BRO', 'SAVG', 'KDA', 'ETH', 'BSCPAD', 'SLIM', 'SAMO', 'FLM', 'USDT', 'LTC', 'ICP', 'CFX',
    'POLS', 'DOT', 'XRP', 'ETC', 'ONT', 'EOS', 'MATE', 'POOLX', 'ETHW', 'SEON', 'XCH', 'FIRO', 'RVN', 'PEAK', 'BONK',
    'MIOTA', 'BTC', 'GALA', 'WIS', 'SOLR', 'BUSD', 'ADA', 'GMI', 'BSC', 'GWT', 'CTXC', 'DOGE', 'NEAR', 'RAZR', 'GT',
    'HT', 'WAG', 'LZ', 'FTM', 'EJS', 'GZONE', 'AION', 'GRT', 'XAVA', 'DIA', 'DASH', 'SERO', 'PPAD', 'FLOW', 'USDC',
    'ERG', 'ALPH', 'XLM', 'BLP', 'IDIA', 'TRBL', 'GARI', 'MATIC', 'BSCS', 'PBR', 'SWAP', 'CELO', 'DAL', 'IRON', 'ZEC',
    'ETHPAD', 'GAIN', 'BGS', 'HINATA', 'TON', 'SOL', 'GAME', 'LPOOL', 'ARTEM', 'AE', 'OKB', 'BNB', 'SLP', 'KOM', 'AVAX',
]

# here can add currency
additional_currencies_symbols = []

# do not change
currencies_symbols_spec = ['CFi', ]

header_columns_in_xlsx_file = ['data', 'id', 'name', 'symbol', 'price']