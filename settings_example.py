import datetime

from pathlib import Path

base_dir = Path(__file__).parent
time_stamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

data_dir = base_dir / 'handlers' / 'data'

# base currencies for query.
currencies_symbols = [
    'LUNA', 'ATOM', 'MATIC', 'ATLAS', 'STARS',
]

# here can add currency for query
additional_currencies_symbols = ['SOLO', 'GALA', ]

# do not change for query
currencies_symbols_spec = ['CFi', ]

# The result is returned in the token's smallest decimal representation == 9
RATE_DECIMALS_9 = ['MCRT', ]


# Fill for using file 'main_2.py'
"""Blockchains"""
# Coins which are in wallet on blockchain. Symbol, contract.
BSC_CURRENCIES = {
    'BUSD': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
    'CAKE': '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82',
}

# Coins which are in wallet on blockchain. Symbol, contract.
ETHER_CURRENCIES = {
    'ETH': '0x2170ed0880ac9a755fd29b2688956bd959f933f8'
}

# Coins which are in wallet on blockchain. Symbol, contract.
FTM_CURRENCIES = {
    'FTM': '0x4e15361fd6b4bb609fa63c81a2be19d873717870',
    'BRO': '0x230576a0455d7Ae33c6dEfE64182C0BB68bAFAF3',
}

# Coins which are in wallet on blockchain. Symbol, contract.
POLYGON_CURRENCIES = {
    'MATIC': '0x0000000000000000000000000000000000001010',
}


# Coins which are in wallet on blockchain. Symbol, contract.
# And has not field 'tokenSymbol' in data of coin in response from request.
SOLANA_CURRENCIES = {
    'BGS': 'At7RLMbA6ZUjj7riyvFq2j5NHQ19aJabCju2VxLDAqso',
    'GARI': 'CKaKtYvz6dKPyMvYq9Rh3UBrnNqYZAyd7iF4hJtjUvks',
}
