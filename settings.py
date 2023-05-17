import datetime

from pathlib import Path

base_dir = Path(__file__).parent
time_stamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# base currencies for query.
currencies_symbols = [
    'AGV', 'TICKET', 'FS', 'BEAM', 'YOM', 'LUNA', 'SOLC', 'ATOM', 'KZEN', 'LUNC', 'VENT', 'CAKE', 'MCRT', 'ESCROW',
    'AVXL', 'ONG', 'BRO', 'SAVG', 'KDA', 'ETH', 'BSCPAD', 'SLIM', 'SAMO', 'FLM', 'USDT', 'LTC', 'ICP', 'CFX',
    'POLS', 'DOT', 'XRP', 'ETC', 'ONT', 'EOS', 'MATE', 'POOLX', 'ETHW', 'SEON', 'XCH', 'FIRO', 'RVN', 'PEAK', 'BONK',
    'MIOTA', 'BTC', 'GALA', 'WIS', 'SOLR', 'BUSD', 'ADA', 'GMI', 'BSC', 'GWT', 'CTXC', 'DOGE', 'NEAR', 'GT',
    'HT', 'WAG', 'LZ', 'FTM', 'EJS', 'GZONE', 'AION', 'GRT', 'XAVA', 'DIA', 'DASH', 'SERO', 'PPAD', 'FLOW', 'USDC',
    'ERG', 'ALPH', 'XLM', 'BLP', 'IDIA', 'TRBL', 'GARI', 'MATIC', 'BSCS', 'PBR', 'SWAP', 'CELO', 'DAL', 'IRON', 'ZEC',
    'ETHPAD', 'GAIN', 'BGS', 'TON', 'SOL', 'GAME', 'LPOOL', 'ARTEM', 'AE', 'OKB', 'BNB', 'SLP', 'KOM', 'AVAX',
    'HINATA', 'RAZR', 'LUNC', 'ATLAS', 'STARS',
]

# here can add currency for query
additional_currencies_symbols = ['XCC', 'POOLZ', 'RD', 'SOLO', 'GALA', 'IOTA']

# do not change for query
currencies_symbols_spec = ['CFi', ]
