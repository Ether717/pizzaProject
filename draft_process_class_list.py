from draft_menu_class import pizza_menu

def calc_item_cost_list(menu_item, menu_item_index) -> float:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.cost

def calc_item_name_list(menu_item, menu_item_index) -> str:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.name

def item_to_dictionary(name, cost) -> dict:
    # Create an empty dictionary and add the name and cost to it
    item_dict = {name: cost}
    return item_dict

if __name__ == "__main__":

    def test_indices(indices):
        for index_num in indices:
            print()
            name = calc_item_name_list(pizza_menu, index_num)
            print(f"Name: {name}")
            cost = calc_item_cost_list(pizza_menu, index_num)
            print(f"Cost: ${cost}")
            item_dict = item_to_dictionary(name, cost)
            print(f"item Dict: {item_dict}")
            print()

    test_indices([0, 1])