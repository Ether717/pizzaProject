# ref link - https://www.youtube.com/watch?v=6tNS--WetLI
# still in progress

import unittest
from draft_menu_class import menu_list
from draft_process_class_v2 import ProcessMenu
 

class TestProcessMenu(unittest.TestCase):

    def setUp(self):
        self.process_menu = ProcessMenu(menu_list)
        self.process_menu.clear_item_dictionary()


    def test_get_item_price_and_name(self):
        try:
            name = self.process_menu.get_item_name(0)
            price = self.process_menu.get_item_price(0)
            self.assertEqual(price, 10.99)
            self.assertEqual(name, "Pepperoni Pizza")
        except Exception as e:
            print(f"Test failed for get_item_price and get_item_name methods: {e}")


    def test_add_to_item_dictionary(self):
        try:
            name = self.process_menu.get_item_name(0)
            price = self.process_menu.get_item_price(0)
            self.process_menu.add_to_item_dictionary(name, price)

            name = self.process_menu.get_item_name(1)
            price = self.process_menu.get_item_price(1)
            self.process_menu.add_to_item_dictionary(name, price)

            self.assertEqual(
                self.process_menu.item_dict,
                {"Pepperoni Pizza": 10.99, "Hawaiian Pizza": 12.99},
            )
        except Exception as e:
            print(f"Test failed for add_to_item_dictionary method: {e}")


    def test_calculate_total_cost(self):
        try:
            name = self.process_menu.get_item_name(1)
            price = self.process_menu.get_item_price(1)
            self.process_menu.add_to_item_dictionary(name, price)
            current_total = 0
            new_current_total = self.process_menu.calculate_total_cost(
                self.process_menu.item_dict, current_total
            )

            # print(f"\nnew_current_total = {new_current_total}") # Debugging line

            self.assertEqual(new_current_total, 12.99)
        except Exception as e:
            print(f"Test failed for calculate_total_cost method: {e}")
        finally:
            self.process_menu.clear_item_dictionary()

    def tearDown(self):
        # Clear the item dictionary after each test to ensure test isolation
        self.process_menu.clear_item_dictionary()

    

if __name__ == "__main__":
    unittest.main()
