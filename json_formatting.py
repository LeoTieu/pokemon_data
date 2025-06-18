from api_functions import get_pokemon_names


def pokemon_dict_builder(pokemon_list: list) -> None:
    pokemon_dict = {}
    for index, pokemon in enumerate(pokemon_list):
        pokemon_dict[index] = pokemon
    print(pokemon_dict)

if __name__ == '__main__':
    pokemon_list = get_pokemon_names()
    pokemon_dict_builder(pokemon_list)
    