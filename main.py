import requests
import json

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(pokemon: str) -> json:
    pokemon_url = f"{base_url}pokemon/{pokemon}"
    response = requests.get(pokemon_url)

    if response.status_code != 200:
        print(f"Could not get data for pokemon: {pokemon}, with error code {response.status_code}")
        return

    return response.json()


def get_pokemon_names() -> list:
    current_pokemons = 1025
    url = f"{base_url}pokemon?limit={current_pokemons}&offset=0"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error code given: {response.status_code}")
        return
    
    base_dictionary = response.json()
    pokemon_list = [pokemon['name'] for pokemon in base_dictionary["results"]]
    return pokemon_list


if __name__ == '__main__':
    # print(get_pokemon_names())
    # print(get_pokemon_info("pikachu"))
    pass