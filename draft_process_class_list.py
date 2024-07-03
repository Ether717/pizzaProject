from draft_menu_class import pizza_menu

current_total = 0  # Initialize current_total to 0

""" converts a item object in a menu to a dictionary """


def get_item_price(menu_item, menu_item_index) -> float:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.cost


def get_item_name(menu_item, menu_item_index) -> str:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.name


def create_item_dictionary(name, cost) -> dict:
    # Create an empty dictionary and add the name and cost to it
    item_dict = {name: cost}
    return item_dict


""" Gets values out of the item dictionary """


# prints the key and values of a inputted dictionary
def print_item_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: ${value}")


# func to add all the cost inside the dict to a total
def calculate_total_cost(dictionary, total_cost) -> float:
    for value in dictionary.values():
        total_cost += value
    return total_cost


""" testing function """


def test_indices(indices):
    for index_num in indices:
        name = get_item_name(pizza_menu, index_num)
        print(f"Name: {name}")
        cost = get_item_price(pizza_menu, index_num)
        print(f"Cost: ${cost}")
        item_dict = create_item_dictionary(name, cost)
        print(f"item Dict: {item_dict}")
        print()


# for every arg/index given it prints the dict value of that index
def test_dictionary_for_indices(indices):
    for index_num in indices:
        name = get_item_name(pizza_menu, index_num)
        cost = get_item_price(pizza_menu, index_num)
        item_dict = create_item_dictionary(name, cost)
        print_item_dictionary(item_dict)


# tests func for add_cost_in_dict using sample data
def test_calculate_total_cost():
    # Create a sample dictionary
    sample_dict = {"item1": 10.0, "item2": 20.0, "item3": 30.0}
    calculate_total_cost(sample_dict, current_total )
    print(f"Total cost: ${calculate_total_cost(sample_dict, current_total ):.2f}")


if __name__ == "__main__":

    def test_functions():
        print()

        print("\nTesting get_item_price and get_item_name functions:")
        test_indices([0, 1])

        print("\nTesting create_item_dictionary function for multiple values:")
        test_dictionary_for_indices([0, 1])

        print("\nTesting calculate_total_cost function with sample data:")
        test_calculate_total_cost()

        print()

    # Call the test_functions function to run all the tests
    test_functions()
