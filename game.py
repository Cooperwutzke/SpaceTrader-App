# Cooper W | Spacetraders API
# Game Start Logic
# https://docs.spacetraders.io/

# MOCK SERVER - This way we don't register agents till we are ready to play
# https://stoplight.io/mocks/spacetraders/spacetraders/96627693/register
 

import logging
import requests
import json
import faction

logging.basicConfig(filename='history.log', encoding='utf-8', format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
current_player = {}

#View some global element such as announcements, server reset dates, player count, and leaderboards
def get_gameinfo():
    gameinfo_request = requests.get(url='https://stoplight.io/mocks/spacetraders/spacetraders/96627693/')
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
    newagent_request = requests.post(url='https://stoplight.io/mocks/spacetraders/spacetraders/96627693/register',
                                     headers='Content-Type: application/json',
                                     json={'symbol': callsign, 'faction': faction})
    newagent_response = newagent_request.json()
    print(json.dumps(newagent_response))

    with open('{callsign}_data.json', 'w') as file:
        json.dumps(newagent_response, file, indent=4)

    logging.info('Agent File Created: {file}')

# Logging in is simply selecting which access token all of our functions will target
def get_myagent(access_token):
    myagent_request = requests.get(url='https://stoplight.io/mocks/spacetraders/spacetraders/96627693/my/agent',
                                   headers='Authorization: {access_token}')
    try:
        myagent_json = json.loads(myagent_request)
    except ValueError as e:
        logging.debug('Invalid login token: %s', access_token)
    logging.info('Successful Login: %s', access_token)
    print('Successful Login: %s', access_token)
    return myagent_json

def test_game():
    print('Enter new agent callsign: ')
    callsign_str = str(input())
    print(callsign_str)
    print('Choose a faction: ')
    selected_factions = faction.filter_factions('name')
    print(selected_factions)
    faction_str = str(input())
    print('%s', faction_str)

test_game()