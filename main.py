import requests
import json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):
    pokemon_url = f"{base_url}pokemon={pokemon}"
    response = requests.get(pokemon_url)

    if response.status_code != 200:
        print(f"Could not get pokemon:{pokemon} data with error code {response.status_code}")
        return

    return response.json()
    
def get_pokemon_names():
    current_pokemons = 1025
    url = f"{base_url}pokemon?limit={current_pokemons}&offset=0"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error code given: {response.status_code}")
        return
    
    return response.json()

if __name__ == '__main__':
    pokemons = get_pokemon_names()
    
    with open("pokemons.json", "w") as f:
        json.dump(pokemons, f, indent=4)

    