
from menu_class import menu_list 
from draft_process_class_v2 import ProcessMenu

def test_process_menu(process_menu):
    
        print("\nTesting ProcessMenu class...")
        
        # populate item dict
        name = process_menu.get_item_name(0)
        price = process_menu.get_item_price(0)
        process_menu.add_to_item_dictionary(name, price)
        
        # Test the get_item_price and get_item_name methods
        try: 
            assert process_menu.get_item_price(0) == 10.99
            assert process_menu.get_item_name(0) == "Pepperoni Pizza"
        except AssertionError:
            print("Test failed for get_item_price and get_item_name methods")
        else:
            print("Test passed for get_item_price and get_item_name methods")
        
        name = process_menu.get_item_name(1)
        price = process_menu.get_item_price(1)
        process_menu.add_to_item_dictionary(name, price)

        # Test the add_to_item_dictionary method
        try:
            # index 0 = Pepperoni Pizza: 10.99
            # index 1 = Hawaiian Pizza: 12.99
            
            # process_menu.print_item_dictionary(process_menu.item_dict) # used to check the dictionary
            
            assert process_menu.item_dict == {'Pepperoni Pizza': 10.99, 'Hawaiian Pizza': 12.99}
        except AssertionError:
            print(f"Test failed for print_item_dictionary method: {e}")
        else:
            print("Test passed for print_item_dictionary method")
        
        # test the calculate_total_cost method
        try:
            current_total = 0
            new_current_total = process_menu.calculate_total_cost(process_menu.item_dict, current_total)
            assert new_current_total == 23.98
        except AssertionError:
            print(f"Test failed for calculate_total method: {e}")
        else:
            print("Test passed for calculate_total method")
        
        # teardown
        process_menu.clear_item_dictionary() # clear the dictionary for the next test
        
        print("All tests passed for ProcessMenu class.\n")
        
        
# parsing the menu_list list to create a ProcessMenu object
process_menu = ProcessMenu(menu_list)


# test the ProcessMenu class
try: 
    test_process_menu(process_menu)
except Exception as e:
    print(f"test failed for process_menu error at: {e}")
    