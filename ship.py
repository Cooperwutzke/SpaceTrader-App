# Cooper W | Spacetraders API
# Ship Management Logic

import requests
import logging

logging.basicConfig(filename="history.log", encoding="utf-8", format="%(asctime)s | %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)

## ----------------  SHIP DETAILS SECTION --------------- ##

def get_my_ships(access_token):
    url = "https://api.spacetraders.io/v2/my/ships"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get ships list: (status code %s)" % response.status_code)
        logging.debug("Failed to get ships list: (status code %s)" % response.status_code)
        return None
    
def get_ship_details(ship_symbol, access_token):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get ship details: %s | (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to get ship details: %s | (status code %s)" % ship_symbol, response.status_code)
        return None
    
## ----------------  SHIP TRANSACTIONS SECTION --------------- ##
    
def get_ship_cargo(ship_symbol, access_token):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/cargo"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get ship cargo: %s | (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to get ship cargo: %s | (status code %s)" % ship_symbol, response.status_code)
        return None
    
def move_ship_orbit(ship_symbol, access_token):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/orbit"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to move ship to orbit: %s | (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to move ship to orbit: %s | (status code %s)" % ship_symbol, response.status_code)
        return None

## ----------------  SHIP MOVEMENT SECTION --------------- ##

def move_ship_dock(ship_symbol, access_token):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/dock"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to move ship to dock: %s | (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to move ship to dock: %s | (status code %s)" % ship_symbol, response.status_code)
        return None
    

## ----------------  SHIP UTILITIES SECTION --------------- ##