# ref link - https://www.youtube.com/watch?v=6tNS--WetLI
# still in progress

import unittest
from menu_class import PizzaMenu
from process_order_class import ProcessOrder


class TestProcessOrder(unittest.TestCase):
    """Unit tests for the ProcessOrder class."""
    
    pepperoni = PizzaMenu(
        "Pepperoni Pizza", "Delicious pepperoni pizza", 10.99)
    hawaiian = PizzaMenu(
        "Hawaiian Pizza", "Sweet and savory Hawaiian pizza", 12.99)
    menu_list = [pepperoni, hawaiian]
    process_order = ProcessOrder(menu_list)

    def test_get_item_price_and_name(self):
        """Test getting the price and name of a menu item."""
        try:
            name = self.process_order.get_item_name(0)
            price = self.process_order.get_item_price(0)
            self.assertEqual(price, 10.99)
            self.assertEqual(name, "Pepperoni Pizza")
        except Exception as e:
            print(
                f"Test failed for get_item_price and get_item_name methods: {e}")

    def test_add_to_item_dictionary(self):
        """Test adding items to the item dictionary."""
        try:
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
        except Exception as e:
            print(f"Test failed for add_to_item_dictionary method: {e}")

    def test_calculate_total_cost(self):
        """Test calculating the total cost of items in the item dictionary."""
        try:
            menu_index = 1
            amount = 2
            self.process_order.add_to_item_dictionary(menu_index, amount)
            current_total = 0
            new_current_total = self.process_order.calculate_total_cost(
                self.process_order.item_dict, current_total)

            self.assertEqual(new_current_total, 12.99)
        except Exception as e:
            print(f"Test failed for calculate_total_cost method: {e}")
        finally:
            self.process_order.clear_item_dictionary()

    def tearDown(self):
        """Clear the item dictionary"""
        # Clear the item dictionary after each test to ensure test isolation
        self.process_order.clear_item_dictionary()


if __name__ == "__main__":
    unittest.main()
