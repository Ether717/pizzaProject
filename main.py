from ui_class import UiMenu
from menu_class import PizzaMenu, DrinksMenu
from process_order_class import ProcessOrder


def create_menu_list():
    precious_pepperoni = PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00)
    supreme_chicken_of_gondor = PizzaMenu("Supreme Chicken of Gondor ", "", 23.50)
    bag_end_bbq_meatlovers = PizzaMenu("Bag-End BBQ Meatlovers", "", 25.50)
    fellowship_of_the_four_cheeses = PizzaMenu("Fellowship of the Four Cheeses", "", 22.50)
    bree_ham_and_pineapple = PizzaMenu("Bree Ham & Pineapple", "", 19.00)
    leaf_of_lorien_margherita = PizzaMenu("Leaf of Lorien Margherita", "", 18.50)

    return [
        precious_pepperoni,
        supreme_chicken_of_gondor,
        bag_end_bbq_meatlovers,
        fellowship_of_the_four_cheeses,
        bree_ham_and_pineapple,
        leaf_of_lorien_margherita,
    ]


def example_menu_list():
    """ " this is an example of how you could expand on the code with easy modularity to add different classes"""
    precious_pepperoni = PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00)
    supreme_chicken_of_gondor = PizzaMenu("Supreme Chicken of Gondor ", "", 23.50)

    coffee = DrinksMenu("Hot Coffee", "", 7.50)
    beer = DrinksMenu("Beer", "", 10.00)

    return [precious_pepperoni, supreme_chicken_of_gondor, coffee, beer]


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

    print()
    member = ui_menu.check_loyalty_member()
    delivery = ui_menu.check_delivery_option()

    total_cost_plus_discount_and_fees = process_menu.apply_discounts_and_fees(total_cost, member, delivery)
    total_cost_plus_gst = process_menu.apply_gst(total_cost_plus_discount_and_fees)
    ui_menu.display_total_cost(total_cost_plus_gst)
    ui_menu.display_thank_you_message()

    # Clear the item dictionary for the next order
    process_menu.clear_item_dictionary()


if __name__ == "__main__":
    main()
