import json
from api_functions import get_pokemon_names, get_pokemon_types


def pokemon_dict_builder(pokemon_list: list) -> None:
    '''Builds a dictionary with all pokemons. 0 indexed'''
    pokemon_dict = {}
    for index, pokemon in enumerate(pokemon_list):
        pokemon_dict[index] = pokemon
    with open("pokemon_data/pokemons.json", "w") as file:
        json.dump(pokemon_dict, file, indent=4)


def temp() -> None:
    type_list = get_pokemon_types(type="list")
    
    


if __name__ == '__main__':
    pokemon_list = get_pokemon_names()
    pokemon_dict_builder(pokemon_list)
