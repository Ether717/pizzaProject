from draft_menu_class import pizza_menu

current_total = 0  # Initialize current_total to 0


class ProcessMenu:
    
    """Converts a menu item object to a dictionary."""

    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.item_dict = {}


    def get_item_price(self, menu_item_index) -> float:
        chosen_item = self.menu_items[menu_item_index]
        return chosen_item.cost


    def get_item_name(self, menu_item_index) -> str:
        chosen_item = self.menu_items[menu_item_index]
        return chosen_item.name


    def add_to_item_dictionary(self, name, cost) -> dict:
        self.item_dict[name] = cost
        return self.item_dict


    def print_item_dictionary(self, dictionary):
        """Prints the key and values for the item_dict."""
        for key, value in dictionary.items():
            print(f"{key}: {value}")


    def calculate_total_cost(self, dictionary, current_total) -> float:
        """Calculates the total cost of all items in the dictionary."""
        for value in dictionary.values():
            current_total += value
        return current_total


if __name__ == "__main__":

    def test_process_menu():
        process_menu = ProcessMenu(pizza_menu)
        process_menu.get_item_name(0)
        process_menu.get_item_price(0)
        process_menu.add_to_item_dictionary(
            process_menu.get_item_name(0), process_menu.get_item_price(0)
        )
        
        process_menu.print_item_dictionary(process_menu.item_dict)
        print(f"current_total ${process_menu.calculate_total_cost(process_menu.item_dict, current_total):.2f}")

    test_process_menu()
