# Cooper W | Spacetraders API
# Contract Logic

import requests
import logging

logging.basicConfig(filename="history.log", encoding="utf-8", format="%(asctime)s | %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)

def get_my_contracts(access_token):
    url = "https://api.spacetraders.io/v2/my/contracts"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve contracts: (status code %s)" % response.status_code)
        logging.debug("Failed to retrieve contracts: (status code %s)" % response.status_code)
        return None
    
def accept_contract(contract_id, access_token):
    url = f"https://api.spacetraders.io/v2/my/contracts/{contract_id}/accept"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to accept contract: %s | (status code %s)" %  contract_id, response.status_code)
        logging.debug("Failed to accept contract: %s | (status code %s)" % contract_id, response.status_code)
        return None
    
def deliver_cargo_contract(contract_id, access_token, shiptrade_json):
    url = f"https://api.spacetraders.io/v2/my/contracts/{contract_id}/deliver"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    data = shiptrade_json
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to deliver cargo to contract: %s | (status code %s)" % contract_id, response.status_code)
        logging.debug("Failed to deliver cargo to contract: %s | (status code %s)" % contract_id, response.status_code)
        return None
    
def fulfill_contract(contract_id, access_token):
    url = f"https://api.spacetraders.io/v2/my/contracts/{contract_id}/fulfill"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fulfill contract: %s | (status code %s)" % contract_id, response.status_code)
        logging.debug("Failed to fulfill contract: %s | (status code %s)" % contract_id, response.status_code)
        return None