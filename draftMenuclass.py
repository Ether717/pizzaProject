# Abstract class representing a menu item
class MenuItem:

    # Constructor method
    def __init__(self, name: str, description: str, cost: float) -> None:
        self.name = name
        self.description = description
        self.cost = cost

    # Method to print the details of the menu item
    def print_item(self) -> None:
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Cost: ${self.cost:.2f}")

 
# Create menu items
pepperoni = MenuItem("Pepperoni Pizza", "Delicious pepperoni pizza", 10.99)
hawaiian = MenuItem("Hawaiian Pizza", "Sweet and savory Hawaiian pizza", 12.99)

# Create a list of menu items for easier  management and iteration
pizza_menu = [pepperoni, hawaiian]

if __name__ == "__main__":
    # Print each menu item's details
    print()
    
    for item in pizza_menu:
        item.print_item()
        print()
        
        
