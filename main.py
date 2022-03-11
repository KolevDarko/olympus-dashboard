import os
from web3 import Web3
from contracts_abi import CUSTOM_TREASURY_ABI, CUSTOM_BOND_ABI, ERC20_ABI
import requests
from decimal import Decimal

INFURA_API_KEY = os.getenv('INFURA_API_KEY')
COINMARKETCAP_API_KEY = os.getenv('CMC_API_KEY')

# INFURA_URL = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
# CMC_API_KEY = "a98770be50430d344543261b2485f86a55f571e6db87d2c4b84fbda4c6598070"
web3 = Web3(Web3.HTTPProvider(INFURA_API_KEY))


def extract_events(tx_hash):
    custom_bond = web3.eth.contract(address=web3.toChecksumAddress('0x9BFb385c1aDB607a427183Bd3eB7dc687f639F26'),
                                    abi=CUSTOM_BOND_ABI)
    receipt = web3.eth.get_transaction_receipt(tx_hash)
    bond_created_event = custom_bond.events.BondCreated().processReceipt(receipt)
    transfers = custom_bond.events.Transfer().processReceipt(receipt)
    bond_changed = custom_bond.events.BondPriceChanged().processReceipt(receipt)
    return {
        'bondCreated': bond_created_event,
        'transfers': transfers,
        'bondChanged': bond_changed
    }


def get_payout_token_data(custom_treasury_address):
    custom_treasury_contract = web3.eth.contract(address=web3.toChecksumAddress(custom_treasury_address),
                                                 abi=CUSTOM_TREASURY_ABI)
    token_address = custom_treasury_contract.functions.payoutToken().call()
    token_contract = web3.eth.contract(token_address, abi=ERC20_ABI)
    token_symbol = token_contract.functions.symbol().call()
    coin_market_cap_data = requests.get(
        f'https://min-api.cryptocompare.com/data/price?fsym={token_symbol}&tsyms=USD&api_key={COINMARKETCAP_API_KEY}')
    token_usd_price = coin_market_cap_data.json()['USD']
    return {
        'price': token_usd_price,
        'symbol': token_symbol
    }


if __name__ == '__main__':
    all_events = extract_events('0x14dc5b46f607e2f0594bc633a50c1218f38f65216aaf3e9296f14bfa38fc3bc1')
    decimals_divider = 1e18
    payout_token_amount = all_events['bondCreated'][0]['args']['payout']
    full_tokens = web3.fromWei(payout_token_amount, 'ether')
    custom_treasury_address = all_events['transfers'][0]['args']['from']
    payout_token_data = get_payout_token_data(custom_treasury_address)
    payout_token_symbol = payout_token_data['symbol']
    usd_price = payout_token_data['price']
    total_usd_payout = payout_token_amount * Decimal(usd_price)
    print(f'Payout tokens were {full_tokens} {payout_token_symbol}, in value of ${total_usd_payout}')
