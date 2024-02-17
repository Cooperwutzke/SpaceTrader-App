# Cooper W | Spacetraders API
# Navigation Logic

import requests
import logging

logging.basicConfig(filename="history.log", encoding="utf-8", format="%(asctime)s | %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)

def get_all_systems():
    url = "https://api.spacetraders.io/v2/systems"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get systems list: (status code %s)" % response.status_code)
        logging.debug("Failed to get systems list: (status code %s)" % response.status_code)
        return None
    
def get_system(system_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get system details: %s | (status code %s)" % system_symbol, response.status_code)
        logging.debug("Failed to get system details: %s | (status code %s)" % system_symbol, response.status_code)
        return None
    
def get_all_waypoints(system_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get waypoints list for system: %s | (status code %s)" % system_symbol, response.status_code)
        logging.debug("Failed to get waypoints list for system: %s | (status code %s)" % system_symbol, response.status_code)
        return None
    
def get_waypoint(system_symbol, waypoint_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get waypoint details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        logging.debug("Failed to get waypoint details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        return None
    
def get_market(system_symbol, waypoint_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/market"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get market details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        logging.debug("Failed to get market details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        return None
    
def get_market(system_symbol, waypoint_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get shipyard details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        logging.debug("Failed to get shipyard details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        return None
    
def get_jump_gate(system_symbol, waypoint_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/jumpgate"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get jump gate details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        logging.debug("Failed to get jump gate details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        return None
    
def get_construction_site(system_symbol, waypoint_symbol):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/construction"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get construction details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        logging.debug("Failed to get construction details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        return None

def supply_construction_site(system_symbol, waypoint_symbol, access_token, shiptrade_json):
    url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/construction/supply"
    headers = {"Accept": "application/json",
               "Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"}
    data = shiptrade_json
    response = requests.get(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get construction details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        logging.debug("Failed to get construction details: %s | (status code %s)" % waypoint_symbol, response.status_code)
        return None