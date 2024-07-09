from menu_class import menu_list

class ProcessMenu:
    
    """Converts a menu item object to a dictionary."""

    # Initializes 
    def __init__(self, menu_items: list):
        self.menu_items = menu_items
        self.item_dict = {}


    def get_item_price(self, menu_item_index: int) -> float:
        chosen_item = self.menu_items[menu_item_index]
        return chosen_item.cost


    def get_item_name(self, menu_item_index: int) -> str:
        chosen_item = self.menu_items[menu_item_index]
        return chosen_item.name

    # option 1
    def add_to_item_dictionary(self, name: str, cost: float) -> dict:
        self.item_dict[name] = cost
        return self.item_dict
    
    
    # option 2
    def add_to_item_dictionary_function_calling(self, menu_item_index: int) -> dict:
        
        name: str = self.get_item_name(menu_item_index)
        price: float = self.get_item_price(menu_item_index)
        
        self.item_dict[name] = price
        return self.item_dict
    
    def print_item_dictionary(self, dictionary):
        """ Prints the key and values for the item_dict. """
        for key, value in dictionary.items():
            print(f"{key}: {value}")
        
if __name__  == "__main__":
    
    def testing_idea():
        process_menu = ProcessMenu(menu_list)
        
        # option 1
        name = process_menu.get_item_name(0)
        price = process_menu.get_item_price(0)
        process_menu.add_to_item_dictionary(name, price)
        print(process_menu.item_dict) 
        
        # option 2
        process_menu.add_to_item_dictionary_function_calling(1)
        print(process_menu.item_dict)
        
        # printing 
        # process_menu.print_item_dictionary(process_menu.item_dict) # debugging
        
    testing_idea()
    
    """ After re-reading the project goals and Looking online and using ChatGPT as a final check to make sure I've chosen options 2
    
        link to chatgpt prompt - https://chatgpt.com/share/3d96476a-0909-4989-abc7-3d3300e1d70e
    """
    
