import json
from api_functions import get_pokemon_names, get_pokemon_types, get_type_interaction


def pokemon_dict_builder(pokemon_list: list) -> None:
    '''Builds a dictionary with all pokemons. 0 indexed'''
    pokemon_dict = {}
    for index, pokemon in enumerate(pokemon_list):
        pokemon_dict[index] = pokemon
    with open("pokemon_data/pokemons.json", "w") as file:
        json.dump(pokemon_dict, file, indent=4)


def basic_type_interaction_generator() -> None:
    '''Generates all type interactions for single typed pokémon'''
    type_list = get_pokemon_types(format="list")
    simple_type_interaction_dict = {}
    for type in type_list:
        simple_type_interaction_dict[type] = get_type_interaction(type)
    
    with open("pokemon_data/single_type_interactions.json", "w") as file:
        json.dump(simple_type_interaction_dict, file, indent=4)
    print("done")



if __name__ == '__main__':
    # pokemon_list = get_pokemon_names()
    # pokemon_dict_builder(pokemon_list)
    basic_type_interaction_generator()
    pass