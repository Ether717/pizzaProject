class UiMenu:
    """This class represents the Command Line Interface (CLI) for the menu"""

    def __init__(self, menu_items: list):
        """Initializes the UiMenu class with a list of menu items"""
        self.menu_items = menu_items

    def display_menu(self):
        """Displays the menu items with their names and prices"""

        # goes each individual item in the list and prints the name and cost of the item
        index = 1
        for item in self.menu_items:
            print(f"{index}. {item.name} - ${item.cost:.2f}")
            index += 1

    def get_yes_no_input(self, prompt: str) -> bool:
        """Prompts the user with a yes/no question and returns True if they choose 'yes', False otherwise"""

        while True:
            user_input = (
                input(f"{prompt} (yes/no): ").strip().lower()
            )  # used llm to help with this part, as ive never used strip before
            if user_input == "yes":
                return True
            elif user_input == "no":
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def get_user_choice(self) -> int:
        """Prompts the user to enter their choice and returns the index of the chosen menu item"""

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))

                if 1 <= choice <= len(self.menu_items):
                    return choice - 1  # subtract 1 to get the index of the list
                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                # handle the case where the input is not a valid integer
                print("Invalid input. Please enter a number.")

    def display_order_summary(self, order_dict):
        """Displays the order summary with the names, prices, and quantities of the ordered items"""

        print("\nOrder Summary:")
        for name, (price, quantity) in order_dict.items():
            print(f"{name} - ${price:.2f} x {quantity}")

    def display_total_cost(self, total_cost):
        """Displays the total cost of the order"""

        print(f"\nTotal Cost: ${total_cost:.2f}")

    def continue_order(self) -> bool:
        """Prompts the user to continue ordering"""
        return self.get_yes_no_input("Do you want to add more items?")

    def get_quantity(self) -> int:
        """Prompts the user to enter the quantity of the chosen menu item and returns the quantity"""

        while True:
            try:
                quantity = int(input("Enter the quantity: "))
                if quantity > 0:
                    return quantity
                else:
                    print("Invalid quantity. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_thank_you_message(self):
        """Displays a thank you message to the user"""

        print("Thank you for your order!")

    def get_loyalty_member(self) -> bool:
        """Prompts the user to enter if they are a loyalty member"""

        return self.get_yes_no_input("Are you a loyalty member?")

    def get_delivery_option(self) -> bool:
        """Prompts the user to enter if they want delivery"""

        return self.get_yes_no_input("Do you want delivery?")

    def get_another_order(self) -> bool:
        """Prompts the user to enter if they want to make another order"""

        return self.get_yes_no_input("Do you want to make another order?")
