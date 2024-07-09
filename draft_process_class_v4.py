from draft_menu_class import menu_list

# current_total = 0  # Initialize current_total to 0, Used for debugging


class ProcessMenu:
    """" """

    # Initializes
    def __init__(self, menu_items: list):
        self.menu_items = menu_items
        self.item_dict = {}

    def get_item_price(self, menu_item_index: int) -> float:
        """" """
        chosen_item = self.menu_items[menu_item_index]
        return chosen_item.cost

    def get_item_name(self, menu_item_index: int) -> str:
        """" """
        chosen_item = self.menu_items[menu_item_index]
        return chosen_item.name

    def add_to_item_dictionary(self, menu_item_index: int, amount: int = 1) -> dict:
        """" """
        # dict = {name: (price, amount)}
        name = self.get_item_name(menu_item_index)
        price = self.get_item_price(menu_item_index)

        if name in self.item_dict:
            # Adds the amount to the existing item in the dictionary.
            self.item_dict[name] = (price, self.item_dict[name][1] + amount)
        else:
            self.item_dict[name] = (price, amount)

        return self.item_dict

    def print_item_dictionary(self, dictionary):
        """Prints the name, price, and quantity for the item_dict."""
        for key, value in dictionary.items():
            print(f"{key}: {value[0]} x {value[1]}")

    def print_item_dictionary_without_amount(self, dictionary):
        """Prints the name, price for the item_dict"""
        for key, value in dictionary.items():
            print(f"{key}: {value[0]}")

    def calculate_total_cost(self, dictionary, current_total: float) -> float:
        """Calculates the total cost of all items in the dictionary."""
        for value in dictionary.values():
            current_total += value
        return current_total

    def calculate_total_cost_with_amount(self, dictionary, current_total: float) -> float:
        """Calculates the total cost of all items in the dictionary."""
        for value in dictionary.values():
            current_total += value[0] * value[1]
        return current_total

    def clear_item_dictionary(self):
        """Clears the item dictionary."""
        self.item_dict.clear()

    # For home delivery – a delivery fee of $8.00 is added to the final bill.
    # Orders exceeding $100, as well as those made by loyalty card members, are eligible for a 5% discount.
    def apply_discounts_and_fees(self, current_total: float, is_loyalty_member: bool, is_delivery: bool) -> float:
        """" """
        pass


if __name__ == "__main__":

    def test_process_multi_input():

        current_total = 0  # Initialize current_total to 0

        process_menu = ProcessMenu(menu_list)

        # adding single item to the dictionary
        process_menu.add_to_item_dictionary(0)

        # adding multiple of the same items to the dictionary
        process_menu.add_to_item_dictionary(1, 3)

        # checking if the dictionary is updated correctly
        process_menu.add_to_item_dictionary(1, 2)

        print()
        process_menu.print_item_dictionary(process_menu.item_dict)
        print()

        print(
            f"total cost: ${process_menu.calculate_total_cost_with_amount(
                process_menu.item_dict, current_total)}"
        )

        manual_total_cost = 10.99 + (12.99 * 5)
        print(f"manual_total_cost: ${manual_total_cost}")


test_process_multi_input()
