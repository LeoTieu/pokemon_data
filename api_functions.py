import requests
import json


BASE_URL = "https://pokeapi.co/api/v2/"

def check_response(status_code):
    if status_code != 200:
        print("Could not get information required.")
        print(f"Error code given: {status_code}")
        raise SystemExit


def get_pokemon_info(pokemon: str) -> dict:
    '''
    Get a lot of information of a specific pokemon.
    Very messy and currently hard to read the return.
    '''
    pokemon_url = f"{BASE_URL}pokemon/{pokemon}"
    response = requests.get(pokemon_url)

    check_response(response.status_code)

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

    check_response(response.status_code)

    base_dictionary = response.json()
    pokemon_list = [pokemon['name'] for pokemon in base_dictionary["results"]]
    return pokemon_list


def get_pokemon_types(format: str = "list") -> dict | list:
    '''
    Gets all current pokemon types and returns them in either a dict or a list.
    Dict format has key = type and value = api type link.
    List just has all current pokemon types.

    Pokémon type 'unknown' exists for some reason.
    '''
    url = f"{BASE_URL}type/"
    response = requests.get(url)

    check_response(response.status_code)

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


def get_type_interaction(type: str) -> dict:
    '''
    Relies on function get_pokemon_types to be working correctly
    Returns a dictionary of the specific damage relations.

    {
        "double_damage_from" : [list of types]
        "double_damage_to" : [list of types]
        "half_damage_from" : [list of types]
        "half_damage_to" : [list of types]
        "no_damage_from" : [list of types]
        "no_damage_to" : [list of types]
        "quadrouple_damage_from" : [list of types]
    } 
    '''
    type_dict = get_pokemon_types()
    response = requests.get(type_dict[type.lower()])
    check_response(response.status_code)

    damage_relation_dict = response.json()['damage_relations']

    # Reformat of values because it's kinda ugly and not very usable
    for key in damage_relation_dict:
        damage_relation_dict[key] = [sub_dict["name"] for sub_dict in damage_relation_dict[key]]

    # For dual elemental weakness, letting them share same format. 
    damage_relation_dict["quadrouple_damage_from"] = []
    return damage_relation_dict


if __name__ == '__main__':
    # print(get_pokemon_info("pikachu"))
    # print(get_pokemon_names())
    # print(get_pokemon_types(format="list"))
    print(get_type_interaction("fighting"))
    pass