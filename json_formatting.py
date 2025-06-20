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
            immunities_1 = singular_type_dict[element_1]["no_damage_from"]
            immunities_2 = singular_type_dict[element_2]["no_damage_from"]
            strengths_1 = singular_type_dict[element_1]["half_damage_from"]
            strengths_2 = singular_type_dict[element_2]["half_damage_from"]
            weaknesses_1 = singular_type_dict[element_1]["double_damage_from"]
            weaknesses_2 = singular_type_dict[element_2]["double_damage_from"] 

            # Immunities take priority over weaknesses and strengths
            combined_immunities = list(set(immunities_1 + immunities_2))
            dual_type_dict[dual_element]["no_damage_from"] = combined_immunities

            # Strength + Weakness -> 1× damage
            negated_1 = [element for element in strengths_1 if element in weaknesses_2]
            negated_2 = [element for element in strengths_2 if element in weaknesses_1]
            negations = list(set(negated_1 + negated_2))

            # Strength + Strength -> ¼× damage
            intersected_strengths = [element for element in strengths_1 if element in strengths_2]
            dual_type_dict[dual_element]["quarter_damage_from"] = combined_immunities

            # Weakness + Weakness -> 4× damage
            intersected_weaknesses = [element for element in weaknesses_1 if element in weaknesses_2]
            dual_type_dict[dual_element]["quadruple_damage_from"] = intersected_weaknesses

            # Regular double and halfs
            dual_type_dict[dual_element]["double_damage_from"] = list[set((strengths_1 + strengths_2) - negations)]
            dual_type_dict[dual_element]["half_damage_from"] = list[set((weaknesses_1 + weaknesses_2) - negations)]


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