# ref link - https://www.youtube.com/watch?v=6tNS--WetLI
# still in progress

import unittest
from menu_class import PizzaMenu
from process_order_class import ProcessOrder


class TestProcessOrder(unittest.TestCase):
    """Unit tests for the ProcessOrder class"""

    # Set up the test environment before each test method is run.
    pepperoni = PizzaMenu("Pepperoni Pizza", "Delicious pepperoni pizza", 10.99)
    hawaiian = PizzaMenu("Hawaiian Pizza", "Sweet and savory Hawaiian pizza", 12.99)
    menu_list = [pepperoni, hawaiian]
    process_order = ProcessOrder(menu_list)

    def test_get_item_price_and_name(self):
        """Test getting the price and name of a menu item"""
        name = self.process_order.get_item_name(0)
        price = self.process_order.get_item_price(0)
        self.assertEqual(price, 10.99)
        self.assertEqual(name, "Pepperoni Pizza")

    def test_add_to_item_dictionary(self):
        """Test adding items to the item dictionary"""
        menu_index = 0
        amount = 1
        self.process_order.add_to_item_dictionary(menu_index, amount)

        menu_index = 1
        amount = 2
        self.process_order.add_to_item_dictionary(menu_index, amount)

        self.assertEqual(
            self.process_order.item_dict,
            {"Pepperoni Pizza": [10.99, 1], "Hawaiian Pizza": [12.99, 2]},
        )

    def test_calculate_total_cost(self):
        """Test calculating the total cost of items in the item dictionary"""
        # makes sure the item.dict is clean
        self.process_order.clear_item_dictionary()

        # Adding items to the dictionary
        self.process_order.add_to_item_dictionary(0)
        self.process_order.add_to_item_dictionary(1, 3)

        # Calculating the total cost
        total_cost = self.process_order.calculate_total_cost_with_amount(self.process_order.item_dict, 0)

        # Manually calculating the total cost
        manual_total_cost = 10.99 + (12.99 * 3)

        # Checking if the calculated total cost matches the manually calculated total cost
        self.assertEqual(total_cost, manual_total_cost)


if __name__ == "__main__":
    unittest.main()
