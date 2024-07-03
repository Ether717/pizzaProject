from draft_menu_class import pizza_menu

def get_item_cost(menu_item, menu_item_index) -> float:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.cost

def get_item_name(menu_item, menu_item_index) -> str:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.name

def item_to_dictionary(name, cost) -> dict:
    # Create an empty dictionary and add the name and cost to it
    item_dict = {name: cost}
    return item_dict


if __name__ == "__main__":

    def test_indices(indices):
        for index_num in indices:
            name = get_item_name(pizza_menu, index_num)
            print(f"Name: {name}")
            cost = get_item_cost(pizza_menu, index_num)
            print(f"Cost: ${cost}")
            item_dict = item_to_dictionary(name, cost)
            print(f"item Dict: {item_dict}")
            print()
    
    # prints the key and values of a inputted dictionary
    def print_dictionary(dictionary):
        for key, value in dictionary.items():
            print(f"{key}: ${value}")
    
    # for every arg/index given it print the dict value of that index 
    def print_dictionary_for_indices(indices): 
        for index_num in indices:
            name = get_item_name(pizza_menu, index_num)
            cost = get_item_cost(pizza_menu, index_num)
            item_dict = item_to_dictionary(name, cost)
            print_dictionary(item_dict)

    print( )
    print("Testing get_item_cost and get_item_name functions:")
    test_indices([0, 1])
    
    print("\nTesting item_to_dictionary function:")
    print_dictionary_for_indices([0, 1])
    
    print()
