# Cooper W | Spacetraders API
# Faction Logic

import requests
import json
import time

def get_factions():
    factions = requests.get('https://api.spacetraders.io/v2/factions')
    factions_response = factions.json()
    return factions_response

def filter_factions(tag):
    faction_list = get_factions()
    names_list = []
    print("FACTION LIST:\n\n")
    print(faction_list)
    for fac in faction_list['data']:
        if tag in fac:
            names_list.append(fac[tag])
    return names_list
