import requests

def get_contracts(): 
    contracts = [] 
    test = requests.get("https://testnet.bitmex.com/api/v1/instrument/active")
    print(test)
    return contracts


get_contracts()