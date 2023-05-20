import datetime

from pathlib import Path

base_dir = Path(__file__).parent
time_stamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

data_dir = base_dir / 'handlers' / 'data'

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
additional_currencies_symbols = ['XCC', 'POOLZ', 'RD', 'SOLO', 'GALA', ]

# do not change for query
currencies_symbols_spec = ['CFi', ]

BSC_CURRENCIES = {
    'BUSD': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
    'CAKE': '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82',
    'DIA': '0x99956D38059cf7bEDA96Ec91Aa7BB2477E0901DD',
    'GMI': '0x93D8d25E3C9A847a5Da79F79ecaC89461FEcA846',
    'KZEN': '0x455B75A6DCF86e700B020765DFbcbE7D4A3b73f5',  # eKZEN
    'LPOOL': '0xCfB24d3C3767364391340a2E6d99c64F1CBd7A3D',
    'MATE': '0x696c2D3c711d5727c3686672F411583faeDAA29F',
    'MCRT': '0x4b8285aB433D8f69CB48d5Ad62b415ed1a221e4f',
    'ONT': '0xFd7B3A77848f1C2D67E05E54d78d174a0C850335',
    'PPAD': '0x93Bb13E90678cCd8BBab07D1dAEF15086746dc9B',
    'USDT': '0x55d398326f99059fF775485246999027B3197955',  # BSC-USD
    'ETH': '0x2170ed0880ac9a755fd29b2688956bd959f933f8'

}

ETHER_CURRENCIES = {
    'ETH': '0x2170ed0880ac9a755fd29b2688956bd959f933f8'
}

FTM_CURRENCIES = {
    'FTM': '0x4e15361fd6b4bb609fa63c81a2be19d873717870',
    'BRO': '0x230576a0455d7Ae33c6dEfE64182C0BB68bAFAF3',
    'ESCROW': '0xE613a914bbb433855378183c3aB13003285da40A',
    'FS': '0xC758295Cd1A564cdb020a78a681a838CF8e0627D',
    'MCRT': '0xE705aF5f63fcaBDCDF5016aA838EAaac35D12890',
    'SAVG': '0xa097c96ACc9587D140AD8aEaAC13D9db2C6CC07f',
    'WIS': '0xF24be6c063Bee7c7844dD90a21fdf7d783d41a94',

}

POLYGON_CURRENCIES = {
    'MATIC': '0x0000000000000000000000000000000000001010',

}

SOLANA_CURRENCIES = {
    'BGS': 'At7RLMbA6ZUjj7riyvFq2j5NHQ19aJabCju2VxLDAqso',
    'BONK': 'DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263',
    'GARI': 'CKaKtYvz6dKPyMvYq9Rh3UBrnNqYZAyd7iF4hJtjUvks',
    'GWT': 'GWTipxSJVPmmW2wCjBdkbnEJbCRCyrhL2x9zuHRPPTj1',
    'RAZR': 'RAZRymwM9F2nP9ZAsojyKRoneydftoqztsx3MnRS9MC',
    'SOLC': 'Bx1fDtvTN6NvE4kjdPHQXtmGSg582bZx9fGy4DQNMmAT',
    'SOLR': '7j7H7sgsnNDeCngAPjpaCN4aaaru4HS7NAFYSEUyzJ3k',
    'TICKET': 'AymKzSDznoLT7Vhsb4wSRnCj1gjcG3zkgYFY8fxsHHer',
    'TRBL': '3CKQgrcvwhvFqVXXxLTb1u262nh26SJ3uutkSCTtbZxH',
    'USDC': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
    'USDT': 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
    'WAG': '5tN42n9vMi6ubp67Uy4NnmM5DMZYN8aS8GeB3bEDHr6E',
    'YOM': 'yomFPUqz1wJwYSfD5tZJUtS3bNb8xs8mx9XzBv8RL39',

}
