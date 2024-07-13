from ui_class import UiMenu
from menu_class import MenuItem, PizzaMenu, DrinksMenu
from process_order_class import ProcessOrder


def create_menu_list():
    precious_pepperoni = PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00)
    supreme_chicken_of_gondor = PizzaMenu("Supreme Chicken of Gondor ", "", 23.50)

    return [precious_pepperoni, supreme_chicken_of_gondor]


def example_menu_list():
    """ " this is an example of how you could expand on the code with easy modularity to add different classes"""
    precious_pepperoni = PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00)
    supreme_chicken_of_gondor = PizzaMenu("Supreme Chicken of Gondor ", "", 23.50)

    coffee = DrinksMenu("Hot Coffee", "", 7.50)

    return [precious_pepperoni, supreme_chicken_of_gondor, coffee]


menu_list = create_menu_list()


def main():
    process_menu = ProcessOrder(menu_list)
    ui_menu = UiMenu(menu_list)

    while True:
        ui_menu.display_menu()
        choice = ui_menu.get_user_choice()
        amount = ui_menu.choose_amount()
        process_menu.add_to_item_dictionary(choice, amount)

        # Ask if the user wants to continue ordering
        continue_order = ui_menu.continue_order()
        if not continue_order:
            break

    ui_menu.display_order_summary(process_menu.item_dict)
    total_cost = process_menu.calculate_total_cost_with_amount(process_menu.item_dict, 0)
    ui_menu.display_total_cost(total_cost)


if __name__ == "__main__":
    main()
