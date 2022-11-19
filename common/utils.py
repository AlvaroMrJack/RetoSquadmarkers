
import random
import requests
from resources.collections import ChistesCollection
from config import CHUCKNORRIS_URL, ICANHAZDADJOKE, LIST_POSSIBLE_VALUES

def get_random_chiste(path_param = None):
    try:
        payload={}
        headers = {}
        final_url = None
        final_data = None

        if path_param is None:
            api_election = random.choice(LIST_POSSIBLE_VALUES)
        elif path_param is not None:
            api_election = path_param

        if api_election == LIST_POSSIBLE_VALUES[0]:
            final_url = CHUCKNORRIS_URL
        elif api_election == LIST_POSSIBLE_VALUES[1]:
            final_url = ICANHAZDADJOKE
            headers = {
               'Accept': 'application/json'
            }

        response = requests.request("GET", final_url, headers=headers, data=payload)

        if response.ok:
            if api_election == LIST_POSSIBLE_VALUES[0]:
                final_data = response.json()['value']
            elif api_election == LIST_POSSIBLE_VALUES[1]:
                final_data = response.json()['joke']
        else:
            final_data = 'Error ocurrido al consumir API'

        return final_data
    except Exception as e:
        return 'Error: {}'.format(e)

def generate_new_id_to_collection():
    len_collection = None
    get_data = ChistesCollection.objects
    len_collection = len(get_data)
    new_id = len_collection + 1
    return new_id
