import requests  # To access our API
import constants # Holds all data
from operator import itemgetter  # Manipulates dicts inside lists

# API Links to PokeAPI
MAIN_URL = 'https://pokeapi.co/api/v2/'
API_URL = {
    'pokemon': MAIN_URL + 'pokemon/'
}


def get_pokemon():
    # Requests for Pokemon
    r = requests.get(API_URL['pokemon'])
    # Re-Requests for All Pokemon Using Count
    r = requests.get(API_URL['pokemon'] + "?limit=" + str(r.json()['count']))
    # Gets Results from API
    pokemon = r.json()['results']
    # Obtains all Name Values
    names = list(map(itemgetter('name'), pokemon))
    # Obtains all Urls Value
    urls = list(map(itemgetter('url'), pokemon))
    # Puts Nm
    return dict(zip(names, urls))


def get_pokemon_url(name):
    return constants.get_pokemon_list()[name]
