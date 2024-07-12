from menu_class import MenuItem


class UiMenu:
    """
    This class represents the Command Line Interface (CLI) for the menu.
    """

    def __init__(self, menu_items: list):
        """
        Initializes the UiMenu class with a list of menu items.
        """
        self.menu_items = menu_items


    def display_menu(self):
        """
        Displays the menu items with their names and prices.
        """

        # goes each individual item in the list and prints the name and cost of the item
        index = 1
        for item in self.menu_items:
            print(f"{index + 1}. {item.name} - ${item.cost:.2f}")
            index += 1


    def get_user_choice(self):
        """
        Prompts the user to enter their choice and returns the index of the chosen menu item.
        """

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))

                if 1 <= choice <= len(self.menu_items):
                    return choice - 1  # subtract 1 to get the index of the list
                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a number.")


    def display_order_summary(self, order_dict):
        """
        Displays the order summary with the names, prices, and quantities of the ordered items.
        """

        print("\nOrder Summary:")
        for name, (price, quantity) in order_dict.items():
            print(f"{name} - ${price:.2f} x {quantity}")


    def display_total_cost(self, total_cost):
        """
        Displays the total cost of the order.
        """

        print(f"\nTotal Cost: ${total_cost:.2f}")


def main():
    pass


if __name__ == "__main__":
    main()
