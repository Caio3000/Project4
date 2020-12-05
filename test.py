import requests
import main_functions
from pprint import pprint

def currency_converter(cost,currency):
    url = "http://api.currencylayer.com/live?access_key=15013d1029614df61eeb55678416c601"
    response = requests.get(url).json()
    pprint(response)

    return


cost = 20
currency = "USDAUD"

currency_converter(cost, currency)

