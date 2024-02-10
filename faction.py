# Cooper W | Spacetraders API
# Faction Logic

import requests
import json

def get_factions():
    factions = requests.get('https://api.spacetraders.io/v2/factions')
    factions_json = factions.json()
    factions_str = json.dumps(factions_json, indent=4)
    print(factions_str)
    return factions_json