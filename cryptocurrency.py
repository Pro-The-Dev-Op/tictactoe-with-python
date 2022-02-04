'get price of cryptocurrency'
import requests
def get_price(currency):
    'get the price of cryptocurrency'
    url = 'https://api.coinmarketcap.com/v1/ticker/' + currency
    response = requests.get(url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])
'get the price of bitcoin'
bitcoin_price = get_price('bitcoin')
'get the price of ethereum'
ethereum_price = get_price('ethereum')
'get the price of litecoin'
litecoin_price = get_price('litecoin')
'get the price of ripple'    
ripple_price = get_price('ripple')
'get the price of bitcoin cash'
bitcoin_cash_price = get_price('bitcoin-cash')
'get the price of eos'
eos_price = get_price('eos')
'get the price of binance coin'
binance_coin_price = get_price('binance-coin')
'get the price of bitcoin gold'
bitcoin_gold_price = get_price('bitcoin-gold')
'get the price of dash'
dash_price = get_price('dash')
'get the price of stellar'
stellar_price = get_price('stellar')
'get the price of monero'
monero_price = get_price('monero')
'get the price of neo'
neo_price = get_price('neo')
'get the price of ethereum classic'
ethereum_classic_price = get_price('ethereum-classic')
'get the price of bitcoin-diamond'
bitcoin_diamond_price = get_price('bitcoin-diamond')
'get the price of bitcoin-private'
bitcoin_private_price = get_price('bitcoin-private')
'get the price of bitcoin-z'
bitcoin_z_price = get_price('bitcoin-z')
'get the price of bitcoin-sv'
bitcoin_sv_price = get_price('bitcoin-sv')
'get the price of bitcoin-cash-sv'
bitcoin_cash_sv_price = get_price('bitcoin-cash-sv')
'get the price of bitcoin-gold-sv'
bitcoin_gold_sv_price = get_price('bitcoin-gold-sv')

if __name__=='__main__':
    get_price()