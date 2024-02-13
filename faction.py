# Cooper W | Spacetraders API
# Faction Logic

import requests
import json
import time

def get_factions():
    factions = requests.get('https://api.spacetraders.io/v2/factions')
    factions_response = factions.json()
    print(type(factions_response))
    time.sleep(4)
    print(json.dumps(factions_response, indent=4))
    time.sleep(4)
    return factions_response

def filter_factions(tag):
    faction_list = get_factions()
    names_list = []
    print(faction_list)
    for fac in faction_list:
        if (fac[tag]):
            names_list.append(fac)
    return names_list
