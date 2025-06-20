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


def all_type_interactions() -> None:
    '''
    Generates all type interactions.
    Only takes incoming damage to consideration.
    Requires "pokemon_data/single_type_interactions.json" to be correct.
    '''
    with open("pokemon_data/single_type_interactions.json", "r") as file:
        singular_type_dict = json.load(file)
    dual_type_dict = {}


    type_list = get_pokemon_types()
    all_possible = []
    while len(type_list) != 0:
        current = type_list.pop()
        for element_2 in type_list:
            # For same dual types in different orders

            element_1 = current
            dual_element = tuple(sorted([current, element_2]))
            dual_type_dict[dual_element] = {}

            # Immunities take priority over weaknesses and strengths
            immunities_1 = singular_type_dict[element_1]["no_damage_from"]
            immunities_2 = singular_type_dict[element_2]["no_damage_from"]
            dual_type_dict[dual_element]["no_damage_from"] = list(set(immunities_1+ immunities_2))



            # Strength + Weakness -> 1× damage
            # Strength + Strength -> ¼× damage
            # Weakness + Weakness -> 4× damage

# Temporary example for easier lookup
# {
#     "normal": {
#         "double_damage_from": [
#             "fighting"
#         ],
#         "double_damage_to": [],
#         "half_damage_from": [],
#         "half_damage_to": [
#             "rock",
#             "steel"
#         ],
#         "no_damage_from": [
#             "ghost"
#         ],
#         "no_damage_to": [
#             "ghost"
#         ],
#         "quadruple_damage_from": []
#     },
# }

    


    



if __name__ == '__main__':
    # pokemon_list = get_pokemon_names()
    # pokemon_dict_builder(pokemon_list)
    all_type_interactions()
    pass