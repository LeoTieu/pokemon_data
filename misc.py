from api_functions import get_pokemon_names, get_pokemon_info, get_pokemon_types


def get_all_current_type_combinations():
    '''
    Running takes a lot of time because of 1300+ api calls.
    Don't run if you don't have to. Thanks!
    '''
    user_input = input("Are you sure you want to run? Y/N")
    if  user_input.lower != "y":
        return

    pokemon_list = get_pokemon_names()
    pokemon_set = set()
    counter = 0
    for pokemon in pokemon_list:
        if counter % 100 == 0:
            print(counter)
        pokemon_type = get_pokemon_info(pokemon)["types"]
        type_combination = [sub_dict["type"]["name"] for sub_dict in pokemon_type]
        type_combination = tuple(sorted(type_combination))
        pokemon_set.add(type_combination)
        counter += 1
    print(pokemon_set)
    print("done")


    

get_all_current_type_combinations()