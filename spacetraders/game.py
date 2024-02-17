# Cooper W | Spacetraders API
# Game Start Logic
# https://docs.spacetraders.io/

# WE ARE ON LIVE SERVER NOW
# Agent park is our test dummy, he may be ruined
 

import logging
import requests
import json
import faction
import contracts
import ship

logging.basicConfig(filename="history.log", encoding="utf-8", format="%(asctime)s | %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
current_player_token = {}

#View some global element such as announcements, server reset dates, player count, and leaderboards
def get_gameinfo():
    gameinfo_request = requests.get(url="https://api.spacetraders.io/v2/")
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

def get_public_agent(agent_symbol):
    url = f"https://api.spacetraders.io/v2/agents/{agent_symbol}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get agent's details: (status code %s)" % response.status_code)
        logging.debug("Failed to get agent's details: (status code %s)" % response.status_code)
        return None

# Logging in is simply selecting which access token all of our functions will target
def get_my_agent(access_token):
    myagent_response = requests.get(url="https://api.spacetraders.io/v2/my/agent",
                                    headers={"Accept": "application/json", 
                                             "Authorization": "Bearer %s" % access_token}) 
    print(myagent_response.content)
    try:
        myagent_json = myagent_response.json()
    except ValueError as e:
        logging.debug("Invalid login token: %s" % access_token)
    logging.info("Successful Login Token Check: %s" % access_token)
    print("Successful Login Token Check: %s" % access_token)
    return myagent_json


def new_agent(callsign, faction):
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
