# Cooper W | Spacetraders API
# Game Start Logic
# https://docs.spacetraders.io/

# WE ARE ON LIVE SERVER NOW
# Agent park is our test dummy, he may be ruined
 

import logging
import requests
import json
import faction

logging.basicConfig(filename="history.log", encoding="utf-8", format="%(asctime)s | %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
current_player = {}

#View some global element such as announcements, server reset dates, player count, and leaderboards
def get_gameinfo():
    gameinfo_request = requests.get(url="https://stoplight.io/mocks/spacetraders/spacetraders/96627693/")
    gameinfo_response = gameinfo_request.json()
    return gameinfo_response

#Make sure servers are online
def get_status():
    status_json = get_gameinfo()['status']
    return(json.dumps(status_json, indent=4))

def get_announcements():
    announcement_json = get_gameinfo()['announcements']
    return(json.dumps(announcement_json, indent=4))

def get_agentcount():
    agentcount_json = get_gameinfo()['stats']['agents']
    return(json.dumps(agentcount_json, indent=4))


def post_newagent(callsign, faction):
    callsign_str = str.upper(callsign)
    faction_str = str.upper(faction)
    payload = {'symbol': "%s" % callsign_str, 'faction': "%s" % faction_str}
    newagent_response = requests.post(url="https://api.spacetraders.io/v2/register",
                                     headers={'Content-Type': "application/json"},
                                     json=payload)
    print(newagent_response.status_code)
    print(newagent_response.content)
    newagent_json = newagent_response.json()

    filename = "%s_data.json" % callsign 
    with open(filename, "w") as file:
        json.dump(newagent_json, file)

    logging.info("Agent File Created: %s" % filename)

# Logging in is simply selecting which access token all of our functions will target
def get_myagent(access_token):
    myagent_request = requests.get(url="https://api.spacetraders.io/v2/my/agent",
                                   headers={"Accept": "application/json", 
                                            "Authorization": "%s" % access_token}) 
    try:
        myagent_json = json.loads(myagent_request)
    except ValueError as e:
        logging.debug("Invalid login token: %s", access_token)
    logging.info("Successful Login: %s", access_token)
    print("Successful Login: %s", access_token)
    return myagent_json

def test_game():
    print("Enter new agent callsign: ")
    callsign_str = str(input())
    print(callsign_str)
    print("Choose a faction: ")
    selected_factions = faction.filter_factions("symbol")
    print("SELECTED FACTIONS: \n\n")
    print(selected_factions)
    faction_str = str(input())
    print(faction_str)
    post_newagent(callsign_str, faction_str)


test_game()