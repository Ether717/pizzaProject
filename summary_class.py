from menu_class import menu_list as menu


# providing a daily summary of the quantities sold for each pizza variety


class Summary:
    """ """

    # constructor
    def __init__(self, order_receipt_list, menu_list: list):
        # order_receipt_list is a list with objects inside to call methods

        # order_receipt_list = [{name:[price,quantity]},...]
        self.order_receipt_list = order_receipt_list

        # menu_list = [item,...]
        self.menu_list = menu_list

    # rest of the class methods...


# summary = Summary(order_receipt_list, menu)
