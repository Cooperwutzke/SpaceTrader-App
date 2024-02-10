# Cooper W | Spacetraders API
# Game Start Logic
# https://docs.spacetraders.io/

import logging
import requests
import json

#logging.basicConfig(filename='history.log', encoding='utf-8', format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def newagent(callsign, faction):
    newagent_request = requests.post(url='https://api.spacetraders.io/v2/register',
                                     headers='Content-Type: application/json',
                                     json={'symbol': callsign, 'faction': faction})
    newagent_response = newagent_request.json()
    print(newagent_response)

    with open('agent_data.json', 'w') as file:
        json.dump(newagent_response, file)

    logging.debug('Agent File Created: {file}')
    print("Agent File Created: {file}")

def gamelogin(access_token):
    logging.debug('Successful Login: %s', access_token)
    print('Successful Login: %s', access_token)

        