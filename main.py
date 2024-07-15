from typing import List
from ui_class import UiMenu
from menu_class import PizzaMenu, DrinksMenu
from process_order_class import ProcessOrder
from summary_class import Summary


def create_menu_list():
    return [
        PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00),
        PizzaMenu("Supreme Chicken of Gondor", "", 23.50),
        PizzaMenu("Bag-End BBQ Meatlovers", "", 25.50),
        PizzaMenu("Fellowship of the Four Cheeses", "", 22.50),
        PizzaMenu("Bree Ham & Pineapple", "", 19.00),
        PizzaMenu("Leaf of Lorien Margherita", "", 18.50),
    ]


def example_menu_list():
    """ " this is an example of how you could expand on the code with easy modularity to add different classes"""
    return [
    PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00),
    PizzaMenu("Supreme Chicken of Gondor ", "", 23.50),
    DrinksMenu("Hot Coffee", "", 7.50),
    DrinksMenu("Beer", "", 10.00),
]


menu_list = create_menu_list()


def main():
    order_receipts: List[dict] = []
    process_menu = ProcessOrder(menu_list)
    ui_menu = UiMenu(menu_list)

    while True:
        process_menu.clear_item_dictionary()

        while True:
            print()
            ui_menu.display_menu()
            choice = ui_menu.get_user_choice()
            amount = ui_menu.get_quantity()
            process_menu.add_item_to_order(choice, amount)

            # Ask if the user wants to continue ordering
            continue_order = ui_menu.continue_order()
            if not continue_order:
                break

        ui_menu.display_order_summary(process_menu.item_dict)
        total_cost = process_menu.calculate_total_cost_with_amount(process_menu.item_dict, 0)

        print()

        member = ui_menu.get_loyalty_member()
        delivery = ui_menu.get_delivery_option()

        total_cost_plus_discount_and_fees = process_menu.apply_discounts_and_fees(total_cost, member, delivery)
        total_cost_plus_gst = process_menu.apply_gst(total_cost_plus_discount_and_fees)

        ui_menu.display_total_cost(total_cost_plus_gst)
        ui_menu.display_thank_you_message()

        # Add current order to order_receipts list
        order_receipts.append(process_menu.item_dict.copy())

        # Ask if the user wants to process another order
        another_order = ui_menu.get_another_order()
        if not another_order:
            break
    
    # Create and print daily summary
    summary = Summary(order_receipts, menu_list)
    summary.create_daily_summary()
    summary.print_daily_summary()

if __name__ == "__main__":
    main()
