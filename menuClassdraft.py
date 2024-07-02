# Abstract class of a menu item
class MenuItem:
    def __init__(self, name: str, description: str, cost: float) -> None:
        self.name = name
        self.description = description
        self.cost = cost

    def print_item(self) -> None:
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Cost: ${self.cost:.2f}")


# Create menu items
pepperoni = MenuItem("Pepperoni Pizza", "Delicious pepperoni pizza", 10.99)
hawaiian = MenuItem("Hawaiian Pizza", "Sweet and savory Hawaiian pizza", 12.99)

# Create a list of menu items for easier management
pizza_menu = [pepperoni, hawaiian]


if __name__ == "__main__":
    # Print each menu item
    print()
    for item in pizza_menu:
        item.print_item()
        print()
    
    
