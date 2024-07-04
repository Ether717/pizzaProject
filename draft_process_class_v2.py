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
        print("\nTesting ProcessMenu class...")
        
        # Create an instance of the ProcessMenu class 
        process_menu = ProcessMenu(pizza_menu)
        
        # Add the first item to the item dictionary
        name = process_menu.get_item_name(0)
        price = process_menu.get_item_price(0)
        process_menu.add_to_item_dictionary(name, price)
        
        # Add the second item to the item dictionary
        name = process_menu.get_item_name(1)
        price =process_menu.get_item_price(1)
        process_menu.add_to_item_dictionary(name, price)
        
        # Test the get_item_price and get_item_name methods
        try: 
            assert process_menu.get_item_price(0) == 10.99
            assert process_menu.get_item_name(0) == "Pepperoni Pizza"
            assert process_menu.item_dict == {"Pepperoni Pizza": 10.99}
        except AssertionError:
            print("Test failed")
        
        # Print the item dictionary
        process_menu.print_item_dictionary(process_menu.item_dict)
        
       
        # Calculate and print the total cost
        print(f"current_total ${process_menu.calculate_total_cost(process_menu.item_dict, current_total):.2f}")

        # Test the calculate_total_cost method
        try:
            assert process_menu.calculate_total_cost(process_menu.item_dict, current_total) == 23.98
        except AssertionError:
            print("Test failed")
            
    test_process_menu()
