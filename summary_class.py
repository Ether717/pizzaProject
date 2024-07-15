class Summary:
    """A class to provide a daily summary of the quantities sold for each pizza variety"""

    def __init__(self, order_receipt_list: list, menu_list: list):
        self.order_receipt_list = order_receipt_list
        self.menu_list = menu_list
        self.daily_summary: dict = {}

    def create_daily_summary(self):
        """Creates the daily summary by aggregating all orders"""

        # Initialize daily_summary with all menu items set to 0
        for item in self.menu_list:
            self.daily_summary[item.name] = 0

        # Iterate through all order receipts
        for order in self.order_receipt_list:
            for product_name, [_, quantity] in order.items():
                if product_name in self.daily_summary:
                    self.daily_summary[product_name] += quantity
                else:
                    # Handle case where product is not in menu but was ordered
                    self.daily_summary[product_name] = quantity

    def print_daily_summary(self):
        """prints the daily summary"""

        for name, quantity in self.daily_summary.items():
            print(f"{name}: {quantity}")


if __name__ == "__main__":

    def test_summary():
        # create a list of menu items
        from main import menu_list

        # precious_pepperoni = PizzaMenu("Precious Pepperoni", "Delicious pepperoni pizza", 21.00)
        # supreme_chicken_of_gondor = PizzaMenu("Supreme Chicken of Gondor ", "", 23.50)
        # bag_end_bbq_meatlovers = PizzaMenu("Bag-End BBQ Meatlovers", "", 25.50)
        # fellowship_of_the_four_cheeses = PizzaMenu("Fellowship of the Four Cheeses", "", 22.50)
        # bree_ham_and_pineapple = PizzaMenu("Bree Ham & Pineapple", "", 19.00)
        # leaf_of_lorien_margherita = PizzaMenu("Leaf of Lorien Margherita", "", 18.50)

        # menu_list = [
        #     precious_pepperoni,
        #     supreme_chicken_of_gondor,
        #     bag_end_bbq_meatlovers,
        #     fellowship_of_the_four_cheeses,
        #     bree_ham_and_pineapple,
        #     leaf_of_lorien_margherita,
        # ]

        # create a list of order receipts
        # order receipts = [[{name: [price, amount]}, ...], ...]
        sample_data = [
            {"Precious Pepperoni": [21.00, 2], "Bree Ham & Pineapple": [19.00, 1]},
            {"Fellowship of the Four Cheeses": [22.50, 3], "Leaf of Lorien Margherita": [18.50, 2]},
            {"Bag-End BBQ Meatlovers": [25.50, 1], "Supreme Chicken of Gondor": [23.50, 2]},
            {"Precious Pepperoni": [21.00, 1], "Fellowship of the Four Cheeses": [22.50, 1]},
        ]

        sample_data_2 = [
            {"Precious Pepperoni": [21.00, 1], "Bree Ham & Pineapple": [19.00, 1]},
            {"Fellowship of the Four Cheeses": [22.50, 3], "Leaf of Lorien Margherita": [18.50, 2]},
        ]

        order_receipts = [sample_data, sample_data_2]

        summary = Summary(order_receipts, menu_list)
        summary.create_daily_summary()
        summary.print_daily_summary()

    test_summary()
