# current_total = 0  # Initialize current_total to 0, Used for debugging


class ProcessOrder:
    """This class is used to process orders."""

    # Initializes
    def __init__(self, order_items: list):
        self.order_items = order_items
        self.item_dict: dict = {}

    def get_item_price(self, item_index: int) -> float:
        """Gets the price of the item at the given index in the menu"""

        chosen_item = self.order_items[item_index]
        return chosen_item.cost

    def get_item_name(self, item_index: int) -> str:
        """Gets the name of the item at the given index in the menu"""

        chosen_item = self.order_items[item_index]
        return chosen_item.name

    def add_item_to_order(self, item_index: int, amount: int = 1) -> dict:
        """Adds the item at the given index to the dictionary with the specified amount"""

        # dict = {name: [price, amount]}
        name = self.get_item_name(item_index)
        price = self.get_item_price(item_index)

        if name in self.item_dict:
            # Adds the amount to the existing item in the dictionary.
            self.item_dict[name] = [price, self.item_dict[name][1] + amount]
        else:
            self.item_dict[name] = [price, amount]
        return self.item_dict

    def calculate_total_cost(self, dictionary, current_total: float) -> float:  # Legacy code, used for debugging now
        """Calculates the total cost of all items in the dictionary"""

        for value in dictionary.values():
            current_total += value
        return current_total

    def calculate_total_cost_with_amount(self, dictionary, current_total: float) -> float:
        """Calculates the total cost of all items in the dictionary"""

        for value in dictionary.values():
            current_total += value[0] * value[1]
        return current_total

    def clear_item_dictionary(self):
        """Clears the item dictionary."""
        self.item_dict.clear()

    # For home delivery – a delivery fee of $8.00 is added to the final bill.
    # Orders exceeding $100, as well as those made by loyalty card members, are eligible for a 5% discount.
    def apply_discounts_and_fees(self, current_total: float, is_loyalty_member: bool, is_delivery: bool) -> float:
        """Applies discounts and fees based on loyalty membership and delivery status"""

        if current_total >= 100 or is_loyalty_member:
            current_total *= 0.95  # Apply a 5% discount

        if is_delivery:
            current_total += 8.00  # Add a delivery fee of $8.00

        return current_total

    # The total bill amount should include a Goods and Services Tax (GST) calculated at 10%
    # of the amount after applying any discounts and surcharges.
    def apply_gst(self, current_total: float) -> float:
        """Applies GST to the current total"""

        return current_total * 1.10

    def print_item_dictionary(self, dictionary):  # used for debugging
        """Prints the name, price, and quantity for the item_dict"""

        for key, value in dictionary.items():
            print(f"{key}: {value[0]} x {value[1]}")

    def print_item_dictionary_without_amount(self, dictionary):  # used for debugging
        """Prints the name, price for the item_dict"""

        for key, value in dictionary.items():
            print(f"{key}: {value[0]}")


if __name__ == "__main__":

    def test_process_multi_input():
        """Test function to process multiple inputs and validate the ProcessOrder class"""
        from main import menu_list

        current_total = 0  # Initialize current_total to 0

        process_menu = ProcessOrder(menu_list)

        # adding single item to the dictionary
        process_menu.add_item_to_order(0)

        # adding multiple of the same items to the dictionary
        process_menu.add_item_to_order(1, 3)

        # checking if the dictionary is updated correctly
        process_menu.add_item_to_order(1, 2)

        print()
        process_menu.print_item_dictionary(process_menu.item_dict)
        print()

        print(f"total cost: ${process_menu.calculate_total_cost_with_amount(process_menu.item_dict, current_total)}")

        manual_total_cost = 10.99 + (12.99 * 5)
        print(f"manual_total_cost: ${manual_total_cost}")

    test_process_multi_input()
