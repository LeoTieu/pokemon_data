import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/"


def get_pokemon_info(pokemon: str) -> dict:
    '''
    Get a lot of information of a specific pokemon.
    Very messy and currently hard to read the return.
    '''
    pokemon_url = f"{BASE_URL}pokemon/{pokemon}"
    response = requests.get(pokemon_url)

    if response.status_code != 200:
        print(f"Could not get data for pokemon: {pokemon}, with error code {response.status_code}")
        return

    return response.json()


def get_pokemon_names() -> list:
    '''
    Returns a list of all current pokemon names. 
    Must manually enter current pokemon amount manually. 
    Current pokemon amount also works as a limit of how many pokemons to get.
    '''
    CURRENT_POKEMONS_AMOUNT = 1025
    
    url = f"{BASE_URL}pokemon?limit={CURRENT_POKEMONS_AMOUNT}&offset=0"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error code given: {response.status_code}")
        return
    
    base_dictionary = response.json()
    pokemon_list = [pokemon['name'] for pokemon in base_dictionary["results"]]
    return pokemon_list


def get_pokemon_types(format: str = "dict") -> dict | list:
    '''
    Gets all current pokemon types and returns them in either a dict or a list.
    Dict format has key = type and value = api type link.
    List just has all current pokemon types.

    Pokémon type 'unknown' exists for some reason.
    '''
    url = f"{BASE_URL}type/"
    print(url)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error code given: {response.status_code}")
        return

    # Gets the all types in a list of dicts.
    list_of_dicts = response.json()["results"]

    if format == "dict":
        type_dict = {}
        for sub_dict in list_of_dicts:
            pokemon_type = sub_dict["name"]
            type_url = sub_dict["url"]
            type_dict[pokemon_type] = type_url
        return type_dict
    elif format == "list":
        type_list = [dict['name'] for dict in list_of_dicts]
        return type_list
    else:
        print(f"Format: {format} is not supported. Use 'list' or 'dict'")

    
if __name__ == '__main__':
    # print(get_pokemon_info("pikachu"))
    # print(get_pokemon_names())
    # print(get_pokemon_types())
    pass