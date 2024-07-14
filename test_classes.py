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

    def test_add_to_item_dictionary_new_and_existing(self):
        """Test adding new and existing items to the item dictionary"""
        # Clear the dictionary before starting the test
        self.process_order.clear_item_dictionary()

        # Test adding a new item
        result = self.process_order.add_to_item_dictionary(0, 2)
        self.assertEqual(result, {"Pepperoni Pizza": [10.99, 2]})
        self.assertEqual(self.process_order.item_dict, {"Pepperoni Pizza": [10.99, 2]})

        # Test adding more of an existing item
        result = self.process_order.add_to_item_dictionary(0, 3)
        self.assertEqual(result, {"Pepperoni Pizza": [10.99, 5]})
        self.assertEqual(self.process_order.item_dict, {"Pepperoni Pizza": [10.99, 5]})

        # Test adding a different item
        result = self.process_order.add_to_item_dictionary(1, 2)
        expected_result = {"Pepperoni Pizza": [10.99, 5], "Hawaiian Pizza": [12.99, 2]}
        self.assertEqual(result, expected_result)
        self.assertEqual(self.process_order.item_dict, expected_result)

    def test_apply_discounts_and_fees(self):
        """Test applying discounts and fees based on various conditions"""

        # Test case 1: No discount, no delivery
        total = self.process_order.apply_discounts_and_fees(50.00, False, False)
        self.assertAlmostEqual(total, 50.00, places=2)

        # Test case 2: Discount due to order over $100, no delivery
        total = self.process_order.apply_discounts_and_fees(120.00, False, False)
        self.assertAlmostEqual(total, 114.00, places=2)  # 120 * 0.95 = 114

        # Test case 3: Discount due to loyalty, no delivery
        total = self.process_order.apply_discounts_and_fees(80.00, True, False)
        self.assertAlmostEqual(total, 76.00, places=2)  # 80 * 0.95 = 76

        # Test case 4: No discount, with delivery
        total = self.process_order.apply_discounts_and_fees(50.00, False, True)
        self.assertAlmostEqual(total, 58.00, places=2)  # 50 + 8 = 58

        # Test case 5: Discount due to order over $100, with delivery
        total = self.process_order.apply_discounts_and_fees(120.00, False, True)
        self.assertAlmostEqual(total, 122.00, places=2)  # (120 * 0.95) + 8 = 122

        # Test case 6: Discount due to loyalty, with delivery
        total = self.process_order.apply_discounts_and_fees(80.00, True, True)
        self.assertAlmostEqual(total, 84.00, places=2)  # (80 * 0.95) + 8 = 84

    def test_apply_gst(self):
        """Test applying GST to various totals"""

        # Test case 1: Apply GST to 0
        total = self.process_order.apply_gst(0.00)
        self.assertAlmostEqual(total, 0.00, places=2)

        # Test case 2: Apply GST to a whole number
        total = self.process_order.apply_gst(100.00)
        self.assertAlmostEqual(total, 110.00, places=2)

        # Test case 3: Apply GST to a decimal number
        total = self.process_order.apply_gst(75.50)
        self.assertAlmostEqual(total, 83.05, places=2)

        # Test case 4: Apply GST to a large number
        total = self.process_order.apply_gst(1000.00)
        self.assertAlmostEqual(total, 1100.00, places=2)

        # Test case 5: Apply GST to a small decimal
        total = self.process_order.apply_gst(0.99)
        self.assertAlmostEqual(total, 1.09, places=2)


if __name__ == "__main__":
    unittest.main()
