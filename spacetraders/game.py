# Cooper W | Spacetraders API
# Game Start Logic
# https://docs.spacetraders.io/

# WE ARE ON LIVE SERVER NOW
# Agent park is our test dummy, he may be ruined
 

import logging
import requests
import json
import glob
import os

logging.basicConfig(filename="history.log", encoding="utf-8", format="%(asctime)s | %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)

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

# This should update our agent data file to reflect recent changes
def get_my_agent(access_token):
    agent_file = select_agent_file()
    myagent_response = requests.get(url="https://api.spacetraders.io/v2/my/agent",
                                    headers={"Accept": "application/json", 
                                             "Authorization": "Bearer %s" % access_token}) 
    if myagent_response.status_code == 200:
        myagent_json = myagent_response.json()
        print("Successful Login Token Check: %s" % access_token)
        logging.info("Successful Login Token Check: %s" % access_token)
        with open(agent_file, "w") as file:
            json.dump(myagent_json, file)
        return myagent_json

    return myagent_json


def new_agent(callsign, faction):
    callsign_str = str.upper(callsign)
    faction_str = str.upper(faction)
    payload = {'symbol': "%s" % callsign_str, 'faction': "%s" % faction_str}
    newagent_response = requests.post(url="https://api.spacetraders.io/v2/register",
                                     headers={'Content-Type': "application/json"},
                                     json=payload)
    newagent_json = newagent_response.json()

    filename = "/agents/%s_data.json" % callsign 
    with open(filename, "w") as file:
        json.dump(newagent_json, file)

    logging.info("Agent File Created: %s" % filename)

def select_agent_file():
    directory = '/agents/'
    json_files = glob.glob(os.path.join(directory, '*_data.json'))

    if json_files:
        print("Select a file by entering its number:")

        # Display the files in a numbered list
        for num, file in enumerate(json_files, start=1):
            print(f"{num}: {os.path.basename(file)}")

        # Take user input (note: input is 1-indexed by humans)
        try:
            selection = int(input("Enter number: ")) - 1  # Convert to 0-indexed
            if 0 <= selection < len(json_files):
                selected_file = json_files[selection]
                print(f"You selected: {os.path.basename(selected_file)}")
                return selected_file
            else:
                print("Invalid selection. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        return -1
