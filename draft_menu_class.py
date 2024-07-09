
# Abstract class representing a menu item
class MenuItem:
    """" """
    # Constructor method

    def __init__(self, name: str, description: str, cost: float) -> None:
        self.name = name
        self.description = description
        self.cost = cost


class PizzaMenu(MenuItem):
    """" """
    # Method to print the details of the menu item

    # This item is used as the bugging to check if Constructor method is working
    def print_item(self) -> str:
        """" """
        return f"Name: {self.name}\nDescription: {self.description}\nCost: ${self.cost:.2f}\n"

# This is an example of a extension of the menu class Which could be implemented With greater scope of the project


class DrinksMenu(PizzaMenu):
    """" """
    # Method

    def check_if_caffeinated(self) -> bool:
        """" """

    def check_if_alcoholic(self) -> bool:
        """" """


# Create menu items for Debugging
pepperoni = MenuItem("Pepperoni Pizza", "Delicious pepperoni pizza", 10.99)
hawaiian = MenuItem("Hawaiian Pizza", "Sweet and savory Hawaiian pizza", 12.99)


# Create a list of menu items for Debugging
menu_list = [pepperoni, hawaiian]

if __name__ == "__main__":
    # Print each menu item's details
    print()

    for item in menu_list:
        print(item.print_item())
