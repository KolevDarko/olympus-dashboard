from web3 import Web3
from contracts_abi import CUSTOM_TREASURY_ABI, CUSTOM_BOND_ABI, ERC20_ABI
import requests
from decimal import Decimal

INFURA_URL = "https://mainnet.infura.io/v3/71f5f61283a047f68ea209ff01f4a7c1"
CMC_API_KEY = "a98770be50430d344543261b2485f86a55f571e6db87d2c4b84fbda4c6598070"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))


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


def get_payout_token(custom_treasury_address):
    custom_treasury_contract = web3.eth.contract(address=web3.toChecksumAddress(custom_treasury_address),
                                                 abi=CUSTOM_TREASURY_ABI)
    token_address = custom_treasury_contract.functions.payoutToken().call()
    return token_address


def get_token_price(token_address):
    token_contract = web3.eth.contract(token_address, abi=ERC20_ABI)
    token_symbol = token_contract.functions.symbol().call()
    coin_market_cap_data = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={token_symbol}&tsyms=USD&api_key={CMC_API_KEY}')
    token_usd_price = coin_market_cap_data.json()['USD']
    return token_usd_price


def get_final_payout(token_amount, token_address):
    return token_amount * Decimal(get_token_price(token_address))


if __name__ == '__main__':
    all_events = extract_events('0x14dc5b46f607e2f0594bc633a50c1218f38f65216aaf3e9296f14bfa38fc3bc1')
    decimals_divider = 1e18
    payout_token_amount = all_events['bondCreated'][0]['args']['payout']
    full_tokens = web3.fromWei(payout_token_amount, 'ether')
    custom_treasury_address = all_events['transfers'][0]['args']['from']
    payout_token_address = get_payout_token(custom_treasury_address)
    payout_dollars = get_final_payout(full_tokens, payout_token_address)
    print(f'Payout tokens were {full_tokens}, in value of ${payout_dollars}')
