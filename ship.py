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
    
def get_ship_cooldown(ship_symbol, access_token):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/cooldown"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200 or 204:
        return response.json()
    else:
        print("Failed to get ship cooldown: %s | (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to get ship cooldown: %s | (status code %s)" % ship_symbol, response.status_code)
        return None
    
#def get_ship_mounts(ship_symbol, access_token):
#def install_ship_mounts(ship_symbol, access_token):
#def remove_ship_mounts(ship_symbol, access_token):
    
## ----------------  SHIP LOGISTICS SECTION --------------- ##

def refuel_ship(ship_symbol, access_token, amount, keep_cargo_fuel):
    refuel_json = {"units": f"{amount}",
                   "fromCargo": f"{keep_cargo_fuel}"}
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/refuel"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=refuel_json)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to refuel [%s]: (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to refuel [%s]: (status code %s)" % ship_symbol, response.status_code)
        return None

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
    
def purchase_cargo(ship_symbol, access_token, commodity, amount):
    purchase_json = {"symbol": f"{commodity}",
                     "units": f"{amount}"}
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/purchase"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=purchase_json)
    
    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to purchase commodity [%s] for [%s]: (status code %s)" % commodity, ship_symbol, response.status_code)
        logging.debug("Failed to purchase commodity [%s] for [%s]: (status code %s)" % commodity, ship_symbol, response.status_code)
        return None
    
def sell_cargo(ship_symbol, access_token, commodity, amount):
    sell_json = {"symbol": f"{commodity}",
                 "units": f"{amount}"}
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/sell"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=sell_json)
    
    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to sell commodity [%s] in [%s]: (status code %s)" % commodity, ship_symbol, response.status_code)
        logging.debug("Failed to sell commodity [%s] in [%s]: (status code %s)" % commodity, ship_symbol, response.status_code)
        return None
    
def transfer_cargo(ship_symbol, target_ship_symbol, access_token, commodity, amount):
    sell_json = {"tradeSymbol": f"{commodity}",
                 "units": f"{amount}",
                 "shipSymbol": f"{target_ship_symbol}"}
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/sell"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=sell_json)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to transfer commodity from [%s] to [%s]: (status code %s)" % ship_symbol, target_ship_symbol, response.status_code)
        logging.debug("Failed to transfer commodity [%s] to [%s]: (status code %s)" % ship_symbol, target_ship_symbol, response.status_code)
        return None
    
def jettison_cargo(ship_symbol, access_token, commodity, amount):
    jettison_json = {"symbol": f"{commodity}",
                     "units": f"{amount}"}
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/jettison"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=jettison_json)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to jettison commodity [%s] in [%s]: (status code %s)" % commodity, ship_symbol, response.status_code)
        logging.debug("Failed to jettison commodity [%s] in [%s]: (status code %s)" % commodity, ship_symbol, response.status_code)
        return None

def negotiate_contract(ship_symbol, access_token):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/negotiate/contract"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to negotiate contract with HQ: %s | (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to negotiate contract with HQ: %s | (status code %s)" % ship_symbol, response.status_code)
        return None

def purchase_ship(waypoint_symbol, access_token, ship_type):
    purchase_json = {"shipType": f"{ship_type}",
                 "waypointSymbol": f"{waypoint_symbol}"}
    url = f"https://api.spacetraders.io/v2/my/ships"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=purchase_json)
    
    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to purchase ship of type [%s] at %s: (status code %s)" % ship_type, waypoint_symbol, response.status_code)
        logging.debug("Failed to purchase ship of type [%s] at %s: (status code %s)" % ship_type, waypoint_symbol, response.status_code)
        return None

## ----------------  SHIP MOVEMENT SECTION --------------- ##

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
    
#def get_ship_nav(ship_symbol, access_token):
#def patch_ship_nav(ship_symbol, access_token):
#def navigate_ship(ship_symbol, access_token):
#def jump_ship(ship_symbol, access_token):
#def warp_ship(ship_symbol, access_token):
    

## ----------------  SHIP UTILS SECTION --------------- ##

#def scan_systems(ship_symbol, access_token):
#def scan_waypoints(ship_symbol, access_token):
#def scan_ships(ship_symbol, access_token):

#def create_resources_survey(ship_symbol, access_token):
    
def extract_resources(ship_symbol, access_token, survey_json=None):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/extract"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers, data=survey_json)

    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to extract resources at %s: (status code %s)" % ship_symbol, response.status_code)
        logging.debug("Failed to extract resources at %s: (status code %s)" % ship_symbol, response.status_code)
        return None

#def siphon_resources(ship_symbol, access_token, survey_json=None):

def ship_refine(ship_symbol, access_token, commodity):
    url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/refine"
    headers = {"Authorization": "Bearer %s" % access_token}
    response = requests.get(url, headers=headers, data={"produce": f"{commodity}"})
    
    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to refine: %s on %s | (status code %s)" % commodity, ship_symbol, response.status_code)
        logging.debug("Failed to refine: %s on %s | (status code %s)" % commodity, ship_symbol, response.status_code)
        return None